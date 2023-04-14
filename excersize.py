# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
newnum = int(two_digit_number)
first_digit = newnum // 10
second_digit = newnum % 10
sum = first_digit + second_digit
print(str(first_digit) + " + " + str(second_digit) + " = " + str(sum))
print(sum)