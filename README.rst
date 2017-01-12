jk_timest
=========

Introduction
------------

This python module aids in estimating the remaining time of a (long running) process. For that purpose
it provides the following class:
* TimeEstimation

How to Use the Time Estimation Class
------------------------------------

In order to use the time estimation class first create a properly initialized instance. You at least have
to tell the object how many processing steps you will have. (This information is required in order to
be able to calculate the remaining time during processing.)

Example:

```python
# initialize the time estimation object
te = TimeEstimator(PROCESS_DURATION_STEPS, 0, 5, 5)
```

The arguments have the following meaning:

1. (required) The maximum number of steps your task will require.
2. (optional) The current position. This will be interesting for you if you resume processing and therefor
   start at a specific position and not at zero.
3. (optional) The minimum number of seconds we want to have data collected until we can do a reasonable estimation.
4. (optional) The minimum number of data values we want to have collected until we can do a reasonable estimation.

Then - during processing - call `tick()` whenever you completed a processing step.

```python
# inform the estimation object that we did something
te.tick()
```

In order to estimate the remainig time call `getETAStr()` and print the result.

Example:

```python
# estimate remaining time and print it
print(te.getETAStr())
```

Estimation Output
-----------------

The method `getETAStr()` provides the following arguments:

* `EnumTimeEstimationOutputStyle mode` : Select the output mode. (See below.)
* `bool bSmooth` : This value is `True` by default and therefor enables smoothing by default. (See below.)
* `str default` : A default string to output if no time estimation can be given (yet). Here `None` is the default.

This method supports the following estimation output styles:

* `EnumTimeEstimationOutputStyle.EASY` : Print either something like "X days Y hours" or something like "HH:MM:SS"
   indicating hours, minutes and seconds. (This is the default.)
* `EnumTimeEstimationOutputStyle.FORMAL` : Print the remaining time in a strict format: "DD:HH:MM:SS"

Smoothing will result in averaging over the last 20 estimation values calculated. This is a very simple
implementation but it works quite well and reduces fluctuations of values if the individual processing
steps vary too much in their duration.

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: j.knauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

Apache Software License 2.0



