while True:
    try:
        age = int(input('How old are you? '))
        break
    except ValueError:
        print('Please enter a whole number')

print('Your age is: ' + str(age))

if age>18:
        print("you are mature guy")
else:
        print("you are in learning phase, concentrate on learning")