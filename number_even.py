#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".

# var_int = 1112

# fourthDigit = var_int // 1000 #4
# value = var_int % 1000 #5 68
# threeDigit = value // 100 # 5
# value2 = value % 100 # 68
# twoDigit = value2 // 10 # 6
# oneDigit = value2 % 10 # 8
# sum = 0
# sum = fourthDigit % 2 + threeDigit % 2 + twoDigit % 2 + oneDigit % 2
# result = 4 - sum
# print(result)

print(145//10)