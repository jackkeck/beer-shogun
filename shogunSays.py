#! /usr/bin/python
# coding=utf-8

from datetime import datetime
import time
import math
import random 
import copy 


beerStyleProps="beerStyles.properties"


def chooseBeerStyle():	
	with open(beerStyleProps) as beerStyleProp:
		beerStyles = beerStyleProp.readlines()

	randomIndex = generateRandomIndex(beerStyles)
	print randomIndex
	print beerStyles[randomIndex]
	

def generateRandomIndex(list):
	# IF LIST HAS LESS THAN 10 ITEMS
	# Limiting to four loops over random generated numbers:
	# 	- We grab list of random generated numbers 
	#	- Check if list contains a number less than length 
	#	  of list If number less than length, return that 
	#	  number to be used as index
	#	- If number is not in the generated list, then sleep  
	#	  for a second and continue looping up to four times. 	
	if (len(list) < 10):
		loopCount = 0
		while ( loopCount < 4 ):
			randomNumbers = generateRandomNumbers() 
			print randomNumbers
			for number in randomNumbers:
				if (number < len(list)):
					print "found one "+str(number) 
					return number
				else:
					continue
			loopCount+=1
			time.sleep(1)
		# After four attempts, we will just take the first or last 
		# index of the list, depending on even or odd length
		if (isEven(len(list))):
			print "four attempts.."
			return len(list)-1
		else:
			print "four attempts.."
			return 0

	# IF LIST HAS MORE THAN TEN ITEMS
	# Limiting to four loops over random generated numbers:
	# 	- We grab list of random generated numbers 
	#	- We grab the max tens place then prefix the existing
	#	  random numbers with the unique tens place, alternating
	#	- We then shuffle the list at random and search for the number. 
	#	- If number is not in the generated list, then sleep  
	#	  for a second and continue looping up to four times.
	else:
		loopCount = 0
		while ( loopCount < 4 ):
			randomNumbers = generateRandomNumbers()
			randomListLength = len(randomNumbers)-1
			randomLengthToList = [int(number) for number in str(randomListLength)]
			baseNumber = randomLengthToList[0]
			randomNumbers.extend(generateAppendedNumbers(baseNumber=baseNumber, list=randomNumbers))

			shuffledRandomNumbers = shuffle(list=randomNumbers)

			for number in shuffledRandomNumbers:
				if (number < len(list)):
					print "found one in tenns "+str(number)
					print number 
					return number
				else:
					continue
			loopCount+=1
			time.sleep(1)
		# After four attempts, we will just take the first or last 
		# index of the list, depending on even or odd length
		if (isEven(len(list))):
			print "four attempts.. in tennns"
			return len(list)-1
		else:
			print "four attempts.. in tennns"
			return 0

def generateRandomNumbers():
	dt = datetime.now()
	microsecond = dt.microsecond
	if (isEven(microsecond)):
		microsecond /= 50
	else:
		microsecond /= 770

	second = dt.second
	if (isEven(second)):
		second += 33
	else:
		second += 62

	minute = dt.minute
	if (isEven(minute)):
		minute += 77
	else: 
		minute += 33

	randomNumber = microsecond/second+(minute*second)
	randomNumberList = [int(number) for number in str(randomNumber)]
	return randomNumberList

def isEven(number):
	if (number % 2 == 0):
		return 1
	else:
		return 0
	return 666

def generateAppendedNumbers(baseNumber, list):
	prefixList = []
	listLength = len(list)-1
	baseNumberDecrement = baseNumber

	while  (listLength >= 0):
		if (baseNumberDecrement > 1): 
			baseListconcat = [integerConcatenation(numberOne=baseNumberDecrement,numberTwo=list[listLength])]
			prefixList.extend(baseListconcat)	
			baseNumberDecrement -=1
			listLength -=1 
		else: 
			baseListconcat = [integerConcatenation(numberOne=baseNumberDecrement,numberTwo=list[listLength])]
			prefixList.extend(baseListconcat)	
			baseNumberDecrement = baseNumber
			listLength -=1
	return prefixList

def integerConcatenation(numberOne,numberTwo):
    return int(str(numberOne)+str(numberTwo))

def shuffle(list):
	listLength = len(list)-1
	numberToShuffle = listLength/4 
	randomIndexes = random.sample(range(listLength), numberToShuffle)
	randomIndexesToSwap = random.sample(range(listLength), numberToShuffle)
	numberToShuffle-=1
	while (numberToShuffle > 0):
		for index in randomIndexes:
			originalIndexValue = list[index]
			list[index] = randomIndexesToSwap[numberToShuffle]
			list[randomIndexesToSwap[numberToShuffle]]=originalIndexValue
 			numberToShuffle-=1
	
	dt = datetime.now()
	if (isEven(dt.second)):
		firstIndexValue = list[0]
		list[0] = list[listLength]
		list[listLength] = firstIndexValue
	else:
		firstIndexValue = list[0]
		list[0] = list[listLength/2]
		list[listLength/2] = firstIndexValue
	return list

chooseBeerStyle()
# listing=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
# print "checking.."
# print listing[0]
# print ".."
# shuffle(listing)



# generateRandomIndex(list=listing)

#randoms = generateRandomNumbers()
#generateAppendedNumbers(baseNumber=(2),list=listing)

