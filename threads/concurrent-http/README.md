# Overview

Demonstrate different python application server (e.g. gunicorn) runtime
configurations to achieve concurrency making IO bound calls to 3rd parties.

The `proxy` represents the application server. The `proxy` makes http
requests to a simulated `third_party` service with a built in response delay.

# Setup

Current setup (see `docker_compose.yml`) has 2 proxies and 1 third party.
* proxy-sync: runs 4 worker processes that take 1 request each
* proxy-async: runs 4 worker processes that use gevent to do async execution
of blocked requests
* third_party: runs 4 worker processes that use gevent to do async execution

Response time of services:
* Third party has 2 endpoints - one fast, one slow
* Both proxies have 2 endpoints that hit the fast and slow third party
endpoints

Expected load testing results:
* Load testing the sync proxy against the fast third party endpoint will be
fast because total round trip is fast
* Load testing the sync proxy against slow third party will limit parallel
requests to the number of sync proxy workers (currently 4) so will be slow
* Load testing the async proxy against fast third party endpoint also fast
* Load testing the async proxy against slow third party will not limit
parallelism to number of workers so will be "fast" as in, many more requests
will run and complete in parallel

# Installation

1. pip install requirements

# Reference

* Docker CPU constraints
** https://docs.docker.com/engine/reference/run/#cpuset-constraint
* Gunicorn concurrency post
** https://medium.com/@genchilu/brief-introduction-about-the-types-of-worker-in-gunicorn-and-respective-suitable-scenario-67b0c0e7bd62
* Gunicorn gevent external C library dependency issues
** https://tech.wayfair.com/2018/07/blocking-io-in-gunicorn-gevent-workers/
* Example siege command for load test:
** siege -c 16 -t 5s http://localhost:5000/fast-third-party | grep -v HTTP*
