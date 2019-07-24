number = int(input("Please Enter any Number: "))
Sum = 0

while(number > 0):
    Reminder = number % 10
    Sum = Sum + Reminder
    number = number //10

print("Sum of the digits of Given Number =",Sum)