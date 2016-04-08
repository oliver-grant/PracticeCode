from math import log

a = []
for i in range(5):
  a.append(str(i) + "cat")

a.reverse()
a.sort()
print(a)

class MyClass:
  i = 0
  tricks = []
  def f(self):
    return "f this"
  def __init__(self, i, lst):
    self.i = i
    self.tricks = lst
  


x = MyClass(15, [1,2,3])

print(x.f())
print(x.i)
print(x.tricks)


def myCrazyFunc(x):
  return x * 3 -2 + 100

def myCrazyBoolFunc(x):
  return (x % 3) == 0

print(filter(myCrazyBoolFunc, range(25)))



def bin(n):
  x = int(n)
  ret_str = ""
  loop_lst = range(int(log(x,2)) + 1)
  loop_lst.reverse()
  for i in loop_lst:
    if (x / (2 ** i)) % 2 == 1:
      ret_str += "1"
    else:
      ret_str += "0"
  return ret_str


print("8: " + bin(8))
print("7: " + bin(7))
