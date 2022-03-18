import math

password = input('Please enter the password: ')
passLeng = len(password)
n = 0
isAlpha = False
isAlNum = False
isDigit = False
isLower = False
isUpper = False
isSpecial = False


for c in password:

  if c.islower():
      isLower = True
  elif c.isupper():
      isUpper = True
  elif c.isdigit():
    isDigit = True
  else :
    # We'll assume if it's nothing else it's a special character
    isSpecial = True

# Gates to make alphanumeric or alphabetic true
if isLower and isUpper:
  isAlpha = True
if isDigit and (isUpper or isLower):
  isAlNum = True

if isAlpha and isAlNum and isSpecial:
  n = 94
elif isAlpha and isSpecial:
  n = 84
elif isAlNum and isSpecial:
  n = 68
elif isAlpha and isAlNum:
  n = 62
elif isAlpha:
  n = 52
elif isDigit and isSpecial:
  n = 42
elif isAlNum:
  n = 36
elif isSpecial:
  n = 32
elif isLower or isUpper:
  n = 26
elif isDigit:
  n = 10
print('\tThere are', n**passLeng, 'combinations')
print('\tThat is equivalent to a key of', math.floor(math.log2(n**passLeng)), 'bits')