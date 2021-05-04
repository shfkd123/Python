class Animal:
    def __init__(self):
        self.fullness = 0
        
    def eat(self):
        self.fullness += 1
    
    def manddang(self):
        self.fullness = 10
        
    
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.flag_cook = False
        
    def gotoHakwon(self):
        self.flag_cook = True
    
        
hum = Human()
print(hum.fullness)
hum.eat()
print(hum.fullness)
hum.manddang()
print(hum.fullness)

print(hum.flag_cook) 
hum.gotoHakwon()
print(hum.flag_cook)
