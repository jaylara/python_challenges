def fizzbuzz(num):
	for i in range(1,num+1):
		tmp = ""
		if i % 3 == 0:
			tmp = tmp + "fizz"
		if i % 5 == 0:
			tmp = tmp + "buzz"
		if len(tmp) == 0:
			tmp = str(i)
		print(tmp)
	
fizzbuzz(100)
