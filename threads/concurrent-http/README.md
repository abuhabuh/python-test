# Overview

Demonstrate different python application server (e.g. gunicorn) runtime
configurations to achieve concurrency making IO bound calls to 3rd parties.

The `proxy` represents the application server. The `proxy` makes http
requests to a simulated `third_party` service with a built in response delay.

todo: write about client testing if any
todo: prove there is no request bottle neck associated with actual http calls out from gevents

# Installation

1. pip install requirements


# Reference

* Docker CPU constraints
** https://docs.docker.com/engine/reference/run/#cpuset-constraint

* Gunicorn concurrency post
https://medium.com/@genchilu/brief-introduction-about-the-types-of-worker-in-gunicorn-and-respective-suitable-scenario-67b0c0e7bd62
