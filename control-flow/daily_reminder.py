Task = input("Describe your task: ")
Priority = input("What's the task priority? (high, medium, low) ")
Time_Bound = input("Is this task time_bound? (yes or no) ")

match Priority:
    case "high":
        if Time_Bound== "yes":
            print(f"'{Task}' is a {Priority} priority task that requires immediate attention today!")
        elif Time_Bound == "no":
            print(f"'{Task}' is a {Priority} task and does not need immediate attention")
        else:
            print(f"Does not recognize {Time_Bound} as a time_bound")
    case "medium":
        if Time_Bound == "yes":
            print(f"'{Task}' is a {Priority} priority task that requires attention today but not immediate!")
        elif Time_Bound == "no":
            print(f"'{Task}' is a {Priority} task and does not need attention at the moment")
        else:
            print(f"Does not recognize {Time_Bound} as a time_bound")
    case "low":
        if Time_Bound == "yes":
            print(f"'{Task}' is a {Priority} priority task that requires attention some other day!")
        elif Time_Bound == "no":
            print(f"'{Task}' is a {Priority} task and does not need attention")
        else:
            print(f"Does not recognize {Time_Bound} as a time_bound")
    case _:
        print(f"Does not recognize {Priority} as required input")


