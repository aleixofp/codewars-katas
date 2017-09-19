# Test module for the challenges

# Describe the test you're gonna do
def describe(message):
    print(message)

# Assert the values
def assert_equals(input, expected):
    print("%s and %s test:\n%s" % (str(input), str(expected), "Correct" if input == expected else "Incorrect"))
