class Car: 
    __name="" 
    __maxspeed=0
    def __init__(self): 
        self.__name="verna" 
        self.__maxspeed=100 
        print(self.__name) 
        print(self.__maxspeed) 
 
    def drive(self): 
        self.__maxspeed=200 
        print("Driving") 
        print(self.__name) 
        print(self.__maxspeed) 
 
c=Car() 
#c.__maxspeed=200 #maxspeed will not change 
c.drive() 