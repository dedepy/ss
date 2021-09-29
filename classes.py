
class Chelik():
    def __init__ (self, age,weight,height,skin,name):
        self.age=age
        self.weight=weight
        self.height=height
        self.skin=skin
        self.name = name
    def go(self):
        print(self.name," go forward")
    def gol(self):
        print(self.name," ")
    def gor(self):
        print(self.name," go right")
    def info(self):
        print(self.age,self.weight,self.height,self.skin,self.name)
Jan=Chelik(13,420,1337,"gold","yan")
Egor_bugor=Chelik(000,69,228,"carbon","Egor_bugor")
Dead_Misha=Chelik(993,986,979,"Kanneji","Dead_Misha")

Jan.go()
Egor_bugor.gol()
Dead_Misha.gor()
Dead_Misha.info()






