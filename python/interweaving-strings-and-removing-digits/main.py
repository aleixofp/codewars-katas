def test(expected, actual):
  print("Expected: " + expected + ", Actual: " + actual)
  return expected == actual

def interweave(s1, s2):    
    
    if len(s1+s2) % 2 != 0: s2 += " "
    message = ""
    for first, second in zip(s1, s2):
        message += (first if not first.isdigit() else "") + (second if not second.isdigit() else "")
    
    return message.strip(" ")
    
# Tests

print(test("hello", interweave("hlo", "el")))
print(test("hello", interweave("h3lo", "el4")))
print(test("hello world", interweave("hlowrd", "el ol")))
