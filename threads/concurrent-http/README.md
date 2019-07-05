# Overview

## Problem

We are building a python backend server that has two endpoints. One
is slower and network IO bound. One is a fast static string response. We do
not want the slower IO bound endpoint to block the fast one for a large number
of concurrent requests. We want to handle as many concurrent requests as
possible.

# Installation

1. pip install requirements
2. brew install siege

# Reference

* Docker CPU constraints
** https://docs.docker.com/engine/reference/run/#cpuset-constraint

* Gunicorn concurrency post
https://medium.com/@genchilu/brief-introduction-about-the-types-of-worker-in-gunicorn-and-respective-suitable-scenario-67b0c0e7bd62

# Todo

* Prove there is no request bottle neck associated with actual http calls out from gevents
