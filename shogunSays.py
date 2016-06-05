#! /usr/bin/python
# coding=utf-8

from datetime import datetime

beerStyleProps="beerStyles.properties"

def chooseBeerStyle():
	with open(beerStyleProps) as beerStyleProp:
		beerStyles = beerStyleProp.readlines()

	for beerStyle in beerStyles:
		beerStyle.strip()

def generateRandomIndex(list):
	print list
	print generateRandomNumber()
	##youre here. Need to add length

def generateRandomNumber():
	microsecond = datetime.now().microsecond
	if (microsecond % 2 == 0):
		microsecond = microsecond/50
	else:
		microsecond = microsecond/770

	second = datetime.now().second
	if (second % 2 == 0):
		second = second+33
	else:
		second = second+62

	minute = datetime.now().minute
	if (minute % 2 == 0):
		minute = minute+77
	else: 
		minute = minute+33

	random = microsecond/second+(minute*second)
	return random

chooseBeerStyle()
listing=[1,2]
generateRandomIndex(list=listing)