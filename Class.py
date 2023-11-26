class MyClass:
    def __init__(self, name : str, hp : int) -> None:
        self.name = name
        self.hp = hp
        
    @staticmethod
    def PrintName(self):
        print(f'name : {self.name} is created.')
        
    def __str__(self) -> str:
        return f"Name : {self.name}"    
    
class MyClass2:
    def __init__(self, name : str, hp : int) -> None:
        self.name = name
        self.hp = hp
    
mc1 = MyClass('mc1', 100)
mc2 = MyClass2('mc2', 200)

mc1.hp = mc2.hp

print(id(mc1.hp))
print(id(mc2.hp))
del mc2
print(mc1.hp)

