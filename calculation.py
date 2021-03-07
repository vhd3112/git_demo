import math 

def cal_rectangle_perimeter(a, b):
    return 2*(a + b)

if __name__ == '__main__':
  f = int(input("choose function: \n\
        0. cal_rectangle_perimeter: "))
  if f == 0:
    a = int(input("Input value a: "))
    b = int(input("Input value b: "))
    result = cal_rectangle_perimeter(a, b)
  else:
    result = "Wrong input"
  print("\nResult: {}".format(result))
    
