def threetostr(num):
	tens = {2:"twenty", 3: "thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
	ones = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
		11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
	out = []
	if num//100:
		out.append(f"{ones[num//100]} hundred")
	num %= 100
	try:
		out.append(ones[num])
	except KeyError:
		out.append(tens[num//10])
		out.append(ones[num%10])
	while "" in out:
		out.remove("")
	return " ".join(out)


def mults(num):
	a = num
	out = []
	multipliers = ("", "thousand", "million", "billion")
	numbs = []
	for i in range(4):
		numbs.append(a%1000)
		a //= 1000
	for i,j in zip(numbs, multipliers):
		if i:
			out.append(f"{threetostr(i)} {j}".strip())
	if a:
		out.append(f"{mults(a)} trillion")
	return " ".join(out[::-1])
	