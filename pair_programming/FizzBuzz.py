#FizzBuzz

def fizzbuzz():
	for x in range(1, 100):
		if x%3 == 0 and x%5 == 0: 
			print("FizzBuzz")
			continue
		if x%3 == 0: 
			print("Fizz")
			continue
		if x%5 == 0: 
			print("Buzz")
			continue
		if x%3 != 0 or x%5 != 0:
			print(x)

fizzbuzz()