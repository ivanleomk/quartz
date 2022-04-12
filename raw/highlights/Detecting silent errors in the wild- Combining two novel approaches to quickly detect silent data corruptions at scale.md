## Metadata
* URL: [https://engineering.fb.com/2022/03/17/production-engineering/silent-errors/](https://engineering.fb.com/2022/03/17/production-engineering/silent-errors/)
* Published Date: 2022-03-17
* Author: [[Harish Dattatraya Dixit]]

## Highlights
* Sources of corruptions include datapath dependencies, temperature variance, and age, among other silicon factors. These errors do not leave any record or trace in system logs. As a result, silent errors stay undetected within workloads and can propagate across several services. In this paper, we describe testing strategies
  * **Note**: Interesting problem that I didn’t think was actually a problem
* However, once the components go through to a production fleet, it becomes really challenging to implement testing at scale. As
* Every iteration of a test takes time away from production workloads. Out-of-production testing has a ramp-up and ramp-down between switching from test to production workloads. In-production testing can leave residual configs that might adversely affect workload performance.
* With out-of-production testing, the challenge is utilizing downtimes from production effectively without affecting other maintenance tasks.
* We’ve observed that in-production testing can, within 15 days, detect 70 percent of the fleet data corruptions that opportunistic testing may take about 6 months to detect.
* We implement this mechanism using Fleetscanner, an internal facilitator tool for testing SDCs opportunistically.
* Opportunistic testing allows for tests to have longer runtimes (on the order of minutes), enabling a more intrusive nature of detection.
* There are fine-grained controls to enable more frequent opportunistic testing cadences on tiers and services that are sensitive.
* Because the testing here “ripples” through our infrastructure, the test times are 1,000x lower than the opportunistic test runtimes. Ripple tests are typically in the order of hundreds of milliseconds within the fleet. They are scheduled based on workload behavior and can be switched on and off per workload.