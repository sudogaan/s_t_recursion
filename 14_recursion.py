# Fibonacci Sequence
# 1,1,2,3,5,8,13...
# our goal is to write a function to return nth term of Fibonacci Sequence

def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
                return 2
        elif n > 2:     
                return fibonacci(n-1)+fibonacci(n-2)
 
for n in range(1, 11):
        print(n, ":", fibonacci(n))

# the output 
#1 : 1
#2 : 2
#3 : 3
#4 : 5
#5 : 8
#6 : 13
#7 : 21
#8 : 34
#9 : 55
#10 : 89

#the values slow down when we try to get the first 100 fibonacci numbers. We can fix it by using memoization

# Memoization

fibonacci_cache = {}

def fibonacci(n):
#if we have cached value, then return it 
        if n in fibonacci_cache:
                return fibonacci_cache[n]
 #compute the nth term
        if n == 1:
                value = 1
        elif n == 2:
                value = 1
        elif n > 2:
                value = fibonacci(n-1)+fibonacci(n-2)
 #cache the value and return it
	fibonacci_cache[n] = value
	return value

for n in range (1, 101):
print(n, ":", fibonacci(n))

# There is an easier way to achieve that

from functools import lru_cache

@Lru_cache(maxsize = 1000) # we write this line to use this before the function
#the number in the paranthesis is the number of values to cache, by default python will cache the 128 most recently used values so if you do not specify a maxsize you will still see benefits.  

def fibonacci(n):
	#check that the input is a positive integer
	if type(n) != int:
		raise TypeError("n must be a positive int")
	if n < 1:
		raise ValueError("n must be a positive int")

	if n == 1:
		value = 1
        elif n == 2:
                value = 1
        elif n > 2:
                value = fibonacci(n-1)+fibonacci(n-2)

for n in range (1, 101):
print(n, ":", fibonacci(n))





