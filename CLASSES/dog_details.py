class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def sit(self):
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        print(f"{self.name} is now rolling !!")
        
        
y=input("Enter the name:")
z=int(input("Enter the age:"))
        
        
    
my_dog = dog(y , z)
my_dog.sit()
my_dog.roll_over()
 