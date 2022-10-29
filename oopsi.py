class student:
    def __init__(self,n=0,m=1):
        self.name=n
        self.roll=m
    def display(self):
        print(self.name)
        print(self.roll)
s=student('hi',13)# here we the values
s.display()
