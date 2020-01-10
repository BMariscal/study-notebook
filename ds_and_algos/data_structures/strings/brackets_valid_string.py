def valid_brackets_string(s):
  stacked = []
  open_brackets = ["[", "(", "{"]
  for i in s:
    if i in open_brackets:
      stacked.append(i)
    else:
      if len(stacked) <= 0:
        return False
      open_bracket = stacked.pop()
      if open_bracket == "[" and i != "]":
        return False
      elif open_bracket == "(" and i != ")":
        return False
      elif open_bracket == "{" and i != "}":
        return False

  return True

print("Valid brackets: ")
s = "{()}}]"
print(valid_brackets_string(s))