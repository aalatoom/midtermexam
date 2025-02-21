
def days_since_birthday(birthday):
    """
    Calculates how many days have passed since the birth year
    (excluding the birth year and current year), including leap years.

    :param birthday: A string in "DD-MM-YYYY" format.
    :return: Number of days passed.
    """
    birth_year = int(birthday[-4:])
    current_year = int(input("Enter the current year: "))
    whole_years = current_year - birth_year - 1
    leap_years = 0
    for year in range(birth_year + 1, current_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    total_days = (whole_years * 365) + leap_years

    return total_days
birthday = "17-10-2005"
print("Days passed:", days_since_birthday(birthday))