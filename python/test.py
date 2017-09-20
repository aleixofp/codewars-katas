# Test module for the challenges

# Describe the test you're gonna do
def describe(message):
    print("----- " + message + " -----")

# Assert the values
def assert_equals(inp, expected, msg=""):
    if msg: print(msg)
    print("Correct" if inp == expected else "Incorrect")
