#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".

var_int = 4875

fourthDigit = var_int // 1000 #4
value = var_int % 1000 #875
threeDigit = value // 100 #8
value2 = value % 100 # 75
twoDigit = value2 // 10 # 7
oneDigit = value2 % 10 # 5
sum = 0
sum = fourthDigit % 2 + threeDigit % 2 + twoDigit % 2 + oneDigit % 2
result = 4 - sum
print(result)

