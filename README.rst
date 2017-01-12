jk_timest
=========

Introduction
------------

This python module aids in estimating the remaining
time of a (long running) process. For that purpose
it provides the following class:
* TimeEstimation

How to use the TimeEstimation class
-----------------------------------

In order to use the time estimation class first create a properly initialized instance. You at least have
to tell the object how many processing steps you will have. (This information is required in order to
be able to calculate the remaining time during processing.)

Then - during processing - call _tick()_ whenever you completed a processing step.

In order to estimate the remainig time call _getETAStr()_ and print the result.

License
-------

Apache Software License 2.0



