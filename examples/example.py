#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import time
import random

from jk_timest import *



# for our test: how long should the process run?
PROCESS_DURATION_STEPS = 30

# initialize the time estimation object
te = TimeEstimator(PROCESS_DURATION_STEPS, 0, 5, 5)

# now simulate our process
for i in range(PROCESS_DURATION_STEPS):

	# now do something; we simulate this by just sleeping for about a second
	time.sleep(1 + random.random() * 0.4 - 0.2)

	# inform estimation object that we did something
	te.tick()

	# estimate remaining time and print it
	print(te.getETAStr())



