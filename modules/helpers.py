# Function that takes a day of the week formatted as a string
# and returns an integer, 0 = Monday, 6 = Sunday
def day_to_int(day):
    if day.lower() == "monday":
        return 0
    elif day.lower() == "tuesday":
        return 1
    elif day.lower() == "wednesday":
        return 2
    elif day.lower() == "thursday":
        return 3
    elif day.lower() == "friday":
        return 4
    elif day.lower() == "saturday":
        return 5
    elif day.lower() == "sunday":
        return 6
    else:
        return None

