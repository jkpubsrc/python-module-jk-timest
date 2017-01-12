#!/usr/bin/env python3
# -*- coding: utf-8 -*-





import sh
import os
import sys
from enum import Enum
import time

from .EnumTimeEstimationOutputStyle import EnumTimeEstimationOutputStyle





def currentTimeMillis():
	return int(time.time() * 1000)





#
# This class estimates the time necessary to complete some kind of process.
#
class TimeEstimator(object):

	#
	# Constructor
	#
	# @param	int expectedMaximum		The expected maximum of the progress.
	# @param	int currentPosition		The current position of the progress. If you continue some processing, specify the current position here.
	# @param	int minDataSeconds		The minimum number of seconds we want to have data collected until we can do a reasonable estimation.
	# @param	int minDataValues		The minimum number of data values we want to have collected until we can do a reasonable estimation.
	#
	def __init__(self, expectedMaximum, currentPosition = 0, minDataSeconds = 10, minDataValues = 10):
		self.__max = expectedMaximum
		self.__pos = currentPosition
		self.__buffer = []
		self.__minDataSeconds = minDataSeconds
		self.__minDataValues = minDataValues
		self.__smoothBuffer = []



	#
	# Perform a "tick": Call this method whenever a progressing step happened. This will indicate some progress on whatever
	# process this object models.
	#
	def tick(self):
		self.__buffer.append(currentTimeMillis())
		self.__pos += 1

		if len(self.__buffer) < self.__minDataValues * 100:
			return
		dtime = (self.__buffer[len(self.__buffer) - 1] - self.__buffer[0]) / 1000
		if dtime < self.__minDataSeconds * 100:
			return
		del self.__buffer[0]



	#
	# Return the average time a single processing step took recently.
	# @return		float		Returns the time in seconds.
	#
	def getSpeed(self):
		if len(self.__buffer) < self.__minDataValues:
			# not enough data
			return None
		# calculate delta
		dtime = (self.__buffer[len(self.__buffer) - 1] - self.__buffer[0]) / 1000
		if dtime < self.__minDataSeconds:
			# too early
			return None
		return (len(self.__buffer) - 1) / dtime



	def getSpeedStr(self, default = None, bFractions = False):
		speed = self.getSpeed()
		if speed == None:
			return str(default)
		else:
			if bFractions:
				return str(speed)
			else:
				return str(int(speed))



	#
	# Return the time in seconds expected until completion
	#
	# @param	boolean bSmooth		Smooth the value that is about to be returned before passing it to the caller.
	# @return	int		The number of seconds to expect until completion or <c>None</c> otherwise.
	#
	def getETA(self, bSmooth = True):
		if len(self.__buffer) < self.__minDataValues:
			return None
		dtime = (self.__buffer[len(self.__buffer) - 1] - self.__buffer[0]) / 1000
		if dtime < self.__minDataSeconds:
			return None
		eticksLeft = self.__max - self.__pos
		if eticksLeft == 0:
			return 0
		dticks = len(self.__buffer) - 1
		avgStepDuration = dtime / dticks
		etime = eticksLeft * avgStepDuration

		self.__smoothBuffer.append(etime)
		if len(self.__smoothBuffer) > 20:
			del self.__smoothBuffer[0]

		if bSmooth:
			mysum = 0
			for v in self.__smoothBuffer:
				mysum += v
			return mysum / len(self.__smoothBuffer) - len(self.__smoothBuffer) * avgStepDuration / 2 + avgStepDuration
		else:
			return etime



	#
	# Return the time expected until completion as a string
	#
	# @param	EnumTimeEstimationOutputStyle mode		The type of return string to produce.
	# @param	boolean bSmooth							Smooth the value that is about to be returned before passing it to the caller.
	# @param	any default								A default value to return if no output could be produced (because of insufficient data)
	# @return	string		Returns a string depending on <c>mode</c>:
	#						* "02:13:03:58" if mode FORMAL is selected
	#						* "2 day 4 hours" or "02:29:33" if mode EASY is selected
	#
	def getETAStr(self, mode = EnumTimeEstimationOutputStyle.EASY, bSmooth = True, default = None):
		secondsLeft = self.getETA()
		if secondsLeft == None:
			return str(default)

		minutesLeft = int(secondsLeft / 60)
		secondsLeft = secondsLeft - (minutesLeft * 60)
		hoursLeft = int(minutesLeft / 60)
		minutesLeft = minutesLeft - (hoursLeft * 60)
		daysLeft = int(hoursLeft / 24)
		hoursLeft = hoursLeft - (daysLeft * 24)
		secondsLeft = int(secondsLeft)

		if mode == EnumTimeEstimationOutputStyle.FORMAL:
			return self.__toStrWithZero(daysLeft) + ":" + self.__toStrWithZero(hoursLeft) + ":" \
				+ self.__toStrWithZero(minutesLeft) + ":" + self.__toStrWithZero(secondsLeft)
		elif mode == EnumTimeEstimationOutputStyle.EASY:
			if daysLeft == 0:
				return self.__toStrWithZero(hoursLeft) + ":" +  self.__toStrWithZero(minutesLeft) + ":" + self.__toStrWithZero(secondsLeft)
			else:
				return str(daysLeft) + " days " + hoursLeft + " hours"



	def __toStrWithZero(self, s):
		if s < 10:
			return "0" + str(s)
		else:
			return str(s)




