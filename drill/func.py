def check_pos(number:int) -> int:
    """ Check if number is a positive , negative or a zero"""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def check_evn(number:int)-> int:
    """ Check if a nummber is even or odd"""
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd"

def check_div(number:int)-> int:
    """ Check if a number is divisible by 5"""
    if number % 5 == 0:
        return "Divisible"
    return "Not Divisible"

def check_both(number:int) -> int:
    """ Check if a number is divisible by both 3 and 5"""
    if number % 3 == 0 and number % 5 == 0:
        return "Divisible by both"
    return "Not Divisible by both"

def leap_yr(year:int) -> int:
    """Check if a number is a leap year or not"""
    if year % 4 == 0:
        # century year
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    return False 

if __name__ == "__main__":
    print(check_pos(-5))
    print(check_evn(4))
    print(check_div(10))
    print(check_both(15))
    print(leap_yr(2024))