#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".



var_int = 103

fourthDigit = var_int // 1000 #4
a = fourthDigit
value = var_int % 1000 #5 68
threeDigit = value // 100 # 5
b = threeDigit
value2 = value % 100 # 68
twoDigit = value2 // 10 # 6
c = twoDigit
oneDigit = value2 % 10 # 8
d = oneDigit

fourthDigit %= 2

threeDigit %= 2

twoDigit %= 2

oneDigit %= 2

result = fourthDigit * a + threeDigit * b + twoDigit * c + oneDigit * d
print(result)