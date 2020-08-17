import math

probability = 1
total = 1000
numerator = 994
denominator = 998
count = 1
greatest_chance = 0
print()
print("1 Degree Away:")
for i in range(5):
	for j in range(4):
		probability = probability * (numerator/denominator)
		numerator -= 1
		denominator -= 1
		print("Probability of", str(count), "User(s):", str(round(probability * 100, 2))+"%", "\tAverage Users:", math.ceil(count*probability))
		count += 1	
count_2 = 1
print()
print("2 Degrees Away:")
for i in range(20):
	for j in range(4):
		probability = probability * (numerator/denominator)
		numerator -= 1
		denominator -= 1
		print("Probability of", str(count_2), "User(s):", str(round(probability * 100, 2))+"%", "\tAverage Users:", math.ceil(count_2*probability))
		count_2 += 1
count_3 = 1
print()
print("3 Degrees Away:")
for i in range(80):
	for j in range(4):
		probability = probability * (numerator/denominator)
		numerator -= 1
		denominator -= 1
		print("Probability of", str(count_3), "User(s):", str(round(probability * 100, 2))+"%", "\tAverage Users:", math.ceil(count_3*probability))
		count_3 += 1
# count_4 = 1
# print()
# print("4 Degrees Away:")
# for i in range(320):
# 	for j in range(4):
# 		probability = probability * (numerator/denominator)
# 		numerator -= 1
# 		denominator -= 1
# 		print(str(count_4)+": Probability:", probability * 100, "Users:", count_4*probability)
# 		count_4 += 1