"""Return 1 if brackets match correctly and 0 if not matched correctly"""

def BracketMatcher(str):
  str=input("Enter text with brackets: ")
  count = 0
  for c in str:
    if c == '(':
      count += 1
    elif c == ')':
      count -= 1
    # if count < 0: return 0

  return 1 if count == 0 else 0

print(BracketMatcher(str))