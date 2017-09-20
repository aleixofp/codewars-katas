# Python 3.4        
# Check DESCRIPTION.md for the problem's full description.

import test

def interweave(s1, s2):    
    
    if len(s1+s2) % 2 != 0: s2 += " "
    message = ""
    for first, second in zip(s1, s2):
        message += (first if not first.isdigit() else "") + (second if not second.isdigit() else "")
    
    return message.strip(" ")
    
# Tests

test.describe("Tests")

msg1 = "hello"
msg2 = "hello world"

test.assert_equals(interweave("hlo", "el"), msg1, "['hlo', 'el'] should equal 'hello': ")
test.assert_equals(interweave("hlowrd", "el ol"), msg2, "['hlowrd', 'el ol'] should equal 'hello world': ")

