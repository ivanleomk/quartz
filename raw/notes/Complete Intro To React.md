---
title: "Complete Intro To React"
last-updated: "2022-05-08"
---

You can take this course at [Frontend Masters](https://frontendmasters.com/courses/complete-react-v6/)

# Introduction

## What is React?

> React is a frontend user-interface library

React challenges the traditional separation of concerns and mashes everything together into a single component. 

Under the hood, when we write code with [[JSX]] we are actually compiling our javascript code into multiple React.createElement calls. (eg.)

```js
const Pet = ({ name, animal, breed }) => {
  return React.createElement("div", {}, [
    React.createElement("h2", {}, name),
    React.createElement("h3", {}, animal),
    React.createElement("h3", {}, breed),
  ]);
};

const App = () => {
  return React.createElement("div", {}, [
    React.createElement("h1", {}, "Adopt Me!"),
    React.createElement(Pet, {
      name: "Luna",
      animal: "Dog",
      breed: "Havanese",
    }),
    React.createElement(Pet, {
      name: "Salt",
      animal: "Cat",
      breed: "Siamnese",
    }),
    React.createElement(Pet, {
      name: "Rosa",
      animal: "Guinea Pig",
      breed: "Papa New Guinea Pig",
    }),
  ]);
};

ReactDOM.render(React.createElement(App), document.getElementById("root"));

```

## How does React respond

React, much like how it's named, aims to react to user input events. When it detects that something has changed, it re-runs its rendering cycle.


## Hooks
> Hooks are just a way of managing state in our frontend app


Because hooks are built in specifically to work with react's rendering, they cannot be called conditionally. As a general rule, if a variable affects the rendering cycle, we want to keep it in state. If not, we can store it in a singleton.

We can enforce this using `eslint` by updating our eslint config as 

```json
{
  "extends": [
    "eslint:recommended",
    "plugin:import/errors",
    "plugin:react/recommended",
    "plugin:jsx-a11y/recommended",
    %%This is the part to add%%
    "plugin:react-hooks/recommended",
    "prettier"
  ],
  "rules": { "react/prop-types": 0, "react/react-in-jsx-scope": 0 },
  "plugins": ["react", "import", "jsx-a11y"],
  "parserOptions": {
    "ecmaVersion": 2021,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "env": {
    "es6": true,
    "browser": true,
    "node": true
  },
  "settings": {
    "react": {
      "version": "detect"
    }
  }
}
```


## useState

A classic example is that of the `useState` hook. 

```js
import { useState } from "react";
const SearchParams = () => {
  const [location, setLocation] = useState("Seattle, WA");

  return (
    <div className="search-params">
      <form>
        <label htmlFor="location">
          location
          <input
            onChange={(e) => setLocation(e.target.value)}
            id="location"
            value={location}
            placeholder="Location"
          />
        </label>
        <button>Submit</button>
      </form>
    </div>
  );
};

export default SearchParams;
```

## useEffect

```js
useEffect(()=>{
//some cool code
},[//dependencies])


```

`useEffect` can be used to trigger changes when certain variables have changed. In the event that we are using certain timeout functions, we can use a cleanup function to ensure we prevent any memory leaks.

```js
useEffect(()=>{
const timer = setTimeout(()=>{
  console.log("hi!")
},3000)

return () => clearTimeout(timer)
},[])
```


# Useful things to Note

1. When we can set NODE_ENV = development in order to make sure we only get debugging messages printed in prod
2. React strict_mode is a way for the react team to phase out APIs by forcing developers to only work on stable APIs


# Class Components

We can see an example of a class component below

```js
class Details extends Component {
  constructor() {
    super();
    this.state = {
      loading: true,
    };
  }

  async componentDidMount() {
    const res = await fetch(
      `http://pets-v2.dev-apis.com/pets?id=${this.props.match.params.id}`
    );
    const json = await res.json();
    this.setState({
      ...this.state,
      loading: false,
      ...json.pets[0],
    });
    console.log(this.state);
  }

  render() {
    const { animal, breed, city, state, description, name } = this.state;
    return (
      <div>
        <h1>{name}</h1>
        <h2>{`${animal}-${breed}-${city},${state}`}</h2>
        <button>Adopt me!</button>
      </div>
    );
  }
}
```

If we update babel, we can effectively simplify the constructor method by using the following instead

```js
state = {
	loading:true
}
```

This brings us back to our original idea of state as a self-contained pair of values and props as one-directional flows of data from a parent component to a child component.

## Error Boundaries
One of the benefits of using a class component is that we can have use error boundaries.



