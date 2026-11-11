class Avenger:
    def __init__(self,name,age,gender,super_power,weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        
    def get_info(self):
        print("\n-----Avenger Information-----")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Super_power:",self.super_power)
        print("Weapon:",self.weapon)
    
    def is_leader(self):
        if self.name == "Captain America":
            print(self.name,"is the leader")
        else:
            print(self.name,"is not the leader")
            
captain = Avenger("Captain America",100,"Male","Super Strength","Shield")
ironman = Avenger("Iron Man",48,"Male","Technology","Armor")
blackwidow = Avenger("Black Widow", 35, "Female","Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male","Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male","Super Energy", "Mjolnir")
hawkeye = Avenger("Hawkeye", 45, "Male","Fighting skills", "Bow and Arrows")
avengers = [captain,ironman,blackwidow,hulk,thor,hawkeye]

for hero in avengers:
    hero.get_info()
    hero.is_leader( )