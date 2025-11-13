age = int(input('Enter your age: '))

match age:
    case 18 | 19:
        if age>= 18 and has_id(user): # Assuming has_id is a function that checks for valid ID
            print("You are eligible to vote.")
        else:
            print('You need a valid id to vote.')
    case _:
        print("You are not eligible to vote.")