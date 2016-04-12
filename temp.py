# Takes in degrees celsius and returns degrees Fahrenheit
def CtoF(degC):
  return ((9.0/5.0) * degC) +32.0

# Takes in degrees Fahrenheigt and returns degrees Celsius
def FtoC(degF):
  return (5.0/9.0) * (degF - 32.0)


print(CtoF(0)  == 32)
print(CtoF(-1) == 30.2)
print(CtoF(1)  == 33.8)
print(CtoF(100) == 212)

print(abs(FtoC(0) - -17.7778) < 0.01)
print(abs(FtoC(-1) - -18.3333) < 0.1)
print(abs(FtoC(1) - -17.2222) < 0.01)
print(abs(FtoC(100) - 37.77778) < 0.01)

def leapYearQ(year):
  if (((year % 4) == 0) and not(year % 100 == 0)) or (year % 400 == 0):
    return True
  else:
    return False


print(leapYearQ(1992))
print(leapYearQ(1996))
print(not(leapYearQ(1900)))
print(not(leapYearQ(1903)))
print(leapYearQ(0))
print(leapYearQ(2000))


