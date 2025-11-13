day = input("Enter a day of the week(Monday-Sunday):").lower()

match day:
    case "monday":
        print("Ugh! It's Mondays....!")
    case "tuesday":
        print("Just another Workday.")
    case "wednesday":
        print("Hump day! We're halfway through the week.")
    case "thursday":
        print("Almost there! Just one more day to Friday.")
    case "friday":
        print("TGIF! The weekend is just around the corner.")
    case "saturday" | "sunday":
        print("Yay! It's the weekend, time to relax!") 
    case _:
        print("Invalid day entered. Please enter a valid day of the week.")