# a=10
# b=20
# print(a+b)

# a="fristbit"
# b="solution"
# print(a+b)




class Time:
    def __init__(self,hr,min,sec):
       self.hr= hr
       self.min=min
       self.sec= sec

    def _str_(self):
      return f"{self.hr}:{self.min}:{self.sec}"



t1 = Time(1, 2, 33)
print(t1)

# print (t1+t2) 
