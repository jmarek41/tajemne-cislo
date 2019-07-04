# -*- coding: utf-8 -*-
#
#  tajemne-cislo
#
#
#  Created by Jakub Marek on 01/07/2019.
#
#  Cílem této úlohy je najít číslo a to ne jen tak ledajaké...
#  ===========================================================
#  Pravidla:
#
#  Nalezněte způsob, jak vygenerovat číslo, které má následující vlastnosti:
#
#      - Číslo obsahuje 6 číslic
#      - Pokud číslo vynásobím čísly 2, 3, 4, 5, nebo 6, výsledné číslo bude mít stejné číslice, jako původní šestimístné číslo. Mohou se lišit pouze pozice daných číslic.
#
#  Při řešení této úlohy NESMÍ být použity tyto programovací jazyky:
#
#      - Java, Kotlin
#      - Objective C, Swift
#      - PHP, Ruby
#
#  Pří řešení této úlohy je zakázáno použít klíčové slovo if.
#

# Helper functions
# ----------------

def getNumbersSet(number):
    return set(map(int, str(number)))

def filterNumbersSets(taskNumber, numberSet):
    originalValueNumbers = getNumbersSet(numberSet)
    multipliedValueNumbers = getNumbersSet(numberSet * taskNumber)
    return originalValueNumbers == multipliedValueNumbers

# Task
# ----

# Inputs
magnitude = 5
taskNumbers = {2, 3, 4, 5, 6}

# Computation
lowerBoundary = pow(10, magnitude)
upperBoundary = pow(10, magnitude + 1) / max(taskNumbers)
numbersSet = set(range(lowerBoundary, upperBoundary))

for taskNumber in taskNumbers:
    numbersSet = filter(lambda numberSet: filterNumbersSets(taskNumber, numberSet), numbersSet)

print(next(iter(numbersSet), None) or "Hledané číslo neexistuje")
