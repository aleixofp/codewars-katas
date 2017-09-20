# Problem: https://www.codewars.com/kata/580435ab150cca22650001fb
# Title: Find the lucky numbers
# Level: 7 kyu
# Python 3.4
# Check DESCRIPTION.md for the problem's full description.

import test

def filter_lucky(lst):
    return [lucky_number for lucky_number in lst if "7" in str(lucky_number)]

test.describe("Correct tests")

test.it("First test")
l = [1, 2, 4, 6, 7, 12, 30, 50, 60, 65, 70, 68, 69, 77, 80]
test.assert_equals([7, 70, 77], filter_lucky(l))

test.it("Second test")
l = [1, 2, 3, 4, 5, 6, 7, 17, 27, 50]
test.assert_equals([7, 17, 27], filter_lucky(l))
