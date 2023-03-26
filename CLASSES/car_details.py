class car:
    def __init__(self,model,year,make):
        self.model=model
        self.year=year
        self.make=make
        self.odometer_reading=0
        
    def get_descriptive_name(self):
        long_name=f"{self.year},{self.model},{self.make}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
        
        
    def odometer_update(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you cannot rollback odometer!")
        
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
        
   
my_car=car('maruti',2003,'a4')
print(my_car.get_descriptive_name())
my_car.odometer_update(25)
my_car.increment_odometer(25_500)
my_car.read_odometer()


