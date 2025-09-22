from mylib import tee

#สร้าง object ของ class
my_obj = tee()
x = int(input(" How many turns you want to run :"))
for num1 in range(1, x+1):
      num2 = 'x'
      result= my_obj.myfunc(num1, num2)
      print(result)