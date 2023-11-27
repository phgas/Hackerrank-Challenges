def dayOfProgrammer(year: int) -> str:
    """
    This function takes an integer year as input.
    It returns a string representing the date of the 256th day of the year given.

    :param year: Given year. (integer)
    :return: Date in the format dd.mm.yyyy. (string)
    """

    # Time complexity: O

    # Transition year
    if year == 1918:
        formatted_date = "26.09.1918"

    # Julian calendar
    elif year < 1918:
        if year % 4 == 0:
            formatted_date = f"12.09.{year}"  # Leap year
        else:
            formatted_date = f"13.09.{year}"  # Non-leap year

    # Gregorian calendar
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            formatted_date = f"12.09.{year}"  # Leap year
        else:
            formatted_date = f"13.09.{year}"  # Non-leap year

    return formatted_date


if __name__ == "__main__":
    year = 2700
    print(dayOfProgrammer(year))
