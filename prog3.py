from functools import reduce

##Part 4
def product(int_pair_list):
	return list(map(lambda x, : x[0]*x[1], int_pair_list))

##Part 5
def minimum(real_list):
	return reduce(lambda a,b : a if (a<b) else b, real_list)

##Part 6
def between(real_list):
	return list(filter(lambda a : a>=3.0 and a <=4.0, real_list))

pairs = [(1,2),(2,3),(3,4)]
pairs2 = [(3,6),(-54,-2),(3,5),(3,-7),(34,32)]
reals = [1.2,3.2,4.2,1.3,5.5,5.3,6.1,5.5,54.5,34.0]
reals2 = [1.5,3.2,3.6,4.3,6.7,-5.0,4.0,43.2,3.0,-3.1,34.5,66.5,4.4]

print("test product")
print("input1: " + str(pairs))
print("output1: " +  str(product(pairs)) + "\n")
print("input2: " + str(pairs2))
print("output2: " +  str(product(pairs2)) + "\n")

print("test minimum")
print("input1: " + str(reals))
print("output1: " +  str(minimum(reals)) + "\n")
print("input2: " + str(reals2))
print("output2: " +  str(minimum(reals2)) + "\n")

print("test between")
print("input1: " + str(reals))
print("output1: " +  str(between(reals)) + "\n")
print("input2: " + str(reals2))
print("output2: " +  str(between(reals2)) + "\n")

