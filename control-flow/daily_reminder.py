task = input("Describe your task: ")
priority = input("What's the task priority? (high, medium, low) ")
time = input("Is this task time_bound? (yes or no) ")
yes = True
no = False

match priority:
    case "high":
        if time == "yes":
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a {priority} task and does not need immediate attention")
        else:
            print(f"Does not recognize {time} as a time_bound")
    case "medium":
        if time == "yes":
            print(f"'{task}' is a {priority} priority task that requires attention today but not immediate!")
        elif time == "no":
            print(f"'{task}' is a {priority} task and does not need attention at the moment")
        else:
            print(f"Does not recognize {time} as a time_bound")
    case "low":
        if time == "yes":
            print(f"'{task}' is a {priority} priority task that requires attention some other day!")
        elif time == "no":
            print(f"'{task}' is a {priority} task and does not need attention")
        else:
            print(f"Does not recognize {time} as a time_bound")
    case _:
        print(f"Does not recognize {priority} as required input")


