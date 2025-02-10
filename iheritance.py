class Dad:
    def football (self):
        print("dad likes watching football")


class Mum:
    def cooking(self):
        print("mom likes cooking")


class Boy(Dad):
    def Boyage(self):
        print("The boy is 15 years")
my_boy=Boy()
my_boy.football()
my_boy.Boyage()

class Girl(Mum):
    def Girlook(self):
        print("The girl is pretty")
my_girl=Girl()
my_girl.cooking()
my_girl.Girlook()