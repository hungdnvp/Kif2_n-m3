class Map: 
    hp =500
    def __init__(self, iterate= None): 
        self.list = [] 
        # self.__cafedev(iterate) 
    def cafedev(self, iterate): 
        for item in iterate: 
            self.list.append(item) 
    @classmethod
    def rehp(cls):
        Map.hp = 10000
    @staticmethod
    def die():
        Map.hp =0
a = Map()
b = Map()
Map.rehp()
print(a.hp)
Map.die()
print(a.hp)