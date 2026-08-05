class Student:  
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def Avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print('hello',self.name,'your average score is ',sum/3)
    

s1=Student("karan",[98,97,96])
print(s1.Avg())

