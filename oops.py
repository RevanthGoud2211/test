#the simple program for the oops concept
class student:
    def __init__(self):#constructor
        self.name="ravi"
        self.roll=123#instance variables
        self.marks=97.87
    def display(self):#instance method
        print(self.name+"garu")
        print(self.roll+2)
        print(self.marks+23)
s=student()
s.display()


    