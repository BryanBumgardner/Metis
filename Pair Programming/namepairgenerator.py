
#a pair generator 

def get_pairs(names):
	#find the length
	n = len(names)
	#check to make sure the lists are even
	assert n % 2 == 0
# makes sure that list are same size
	#split the lists
	first = names[:n/2]
	second = names[n/2:]
	
	result = []
	
	for _ in range(n-1):
		results.append(zip(first, second))
		second.append(first.pop())
		first.insert(1, second.pop(0))
	
	return result 
