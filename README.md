# Orbital Elements

[![unit tests](https://img.shields.io/github/workflow/status/dmitri-mcguckin/python3-orbital-elements/Unit%20Tests?label=unit%20tests)](https://github.com/dmitri-mcguckin/python3-orbital-elements/actions?query=workflow%3A%22Unit+Tests%22)
[![build](https://img.shields.io/github/workflow/status/dmitri-mcguckin/python3-orbital-elements/Deploy%20to%20PyPi)](https://github.com/dmitri-mcguckin/python3-orbital-elements/actions?query=workflow%3A%22Deploy+to+PyPi%22)
[![issues](https://img.shields.io/github/issues/dmitri-mcguckin/python3-orbital-elements/bug)](https://github.com/dmitri-mcguckin/python3-orbital-elements/labels/bug)
[![docs](https://img.shields.io/readthedocs/python3-orbital-elements)](https://python3-orbital-elements.readthedocs.io)

A simple utility for calculating orbits from [TLE's](https://en.wikipedia.org/wiki/Two-line_element_set) and plotting them with matplotlib.

This is a fork of this [repo](https://github.com/Elucidation/OrbitalElements), rewritten for Python 3.

***

# Installation

`$` `pip install orbital-elements`

***

# Example Plots

**ISS and Dragon CRS2:**
![Orbits of the ISS and Dragon CRS3](http://i.imgur.com/pNmEbRh.png "ISS and Dragon CRS2")

**Some Military Satellites:**
![Military Satellites](http://i.imgur.com/jR8ZMN2.png "Military Satellites")

**Stations, Military and Geostationary satellites:**
![Multiple Satellites](http://i.imgur.com/iQC3i2c.png "Multiple Satellites")

***

# Development and Contribution

### Install Locally

This creates a sym-link to your development environment, so there's no need to install more than once for local testing

`$` `pip install -e .[dev]`

### Run

`$` `orbital-elements <tle-path>`
