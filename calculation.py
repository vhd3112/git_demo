import math 

def cal_rectangle_perimeter(a, b):
    return 2*(a + b)
def cal_rectangle_area(a, b):
    return a*b

if __name__ == '__main__':
  f = int(input("choose function: \n\
        0. cal_rectangle_perimeter: \n\
        1. cal_rectangle_area: "))
  if f == 0:
    a = int(input("Input value a: "))
    b = int(input("Input value b: "))
    result = cal_rectangle_perimeter(a, b)
  else f == 1:
    a = int(input("Input value a: "))
    b = int(input("Input value b: "))
    result = cal_rectangle_area(a, b)
  else:
    result = "Wrong input"
  print("\nResult: {}".format(result))
    
