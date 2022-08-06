#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".


var_int = 202

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

fourthDigit -= 1
fourthDigit %= 2

threeDigit -= 1
threeDigit %= 2

twoDigit -= 1
twoDigit %= 2

oneDigit -= 1
oneDigit %= 2

result = fourthDigit * a + threeDigit * b + twoDigit * c + oneDigit * d
print(result)