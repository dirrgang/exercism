def leap_year(year: int):
    # The tricky thing here is that a leap year in the Gregorian calendar occurs:
    # on every year that is evenly divisible by 4
    #   except every year that is evenly divisible by 100
    #     unless the year is also evenly divisible by 400
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
