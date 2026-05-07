from datetime import date

def leap_year(year):
    try:
        date(year, 2, 29)
        return True
    except ValueError:
        return False