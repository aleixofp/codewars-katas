# Problem: https://www.codewars.com/kata/580435ab150cca22650001fb
# Title: Find the lucky numbers
# Level: 7 kyu
# Python 3.4
# Check DESCRIPTION.md for the problem's full description.

def filter_lucky(lst):
    return [lucky_number for lucky_number in lst if "7" in str(lucky_number)]

