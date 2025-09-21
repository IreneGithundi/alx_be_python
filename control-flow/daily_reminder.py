task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task}' is a {priority} task and does not need immediate attention")
        else:
            print(f"Does not recognize {time_bound} as a time_bound")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that requires attention today but not immediate!")
        elif time_bound == "no":
            print(f"'{task}' is a {priority} task and does not need attention at the moment")
        else:
            print(f"Does not recognize {time_bound} as a time_bound")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a {priority} priority task that requires attention some other day!")
        elif time_bound == "no":
            print(f"'{task}' is a {priority} task and does not need attention")
        else:
            print(f"Does not recognize {time_bound} as a time_bound")
    case _:
        print(f"Does not recognize {priority} as required input")


