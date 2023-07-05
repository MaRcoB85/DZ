from facade_patern.choose_personage import ChoosePersonage
from facade_patern.choose_clothes import ChooseClothes
from facade_patern.choose_superpower import ChooseSuperpower


class Authorization:

    def __init__(self):
        self.change_personage = ChoosePersonage()
        self.change_clothes = ChooseClothes()
        self.change_superpower = ChooseSuperpower()

    def coins_less100(self):
        self.change_personage.personage_group1()
        self.change_clothes.clothes_group1()
        self.change_superpower.superpower_group1()

    def coins_from101_to200(self):
        self.change_personage.personage_group2()
        self.change_clothes.clothes_group1()
        self.change_superpower.superpower_group1()

    def coins_from201_to400(self):
        self.change_personage.personage_group2()
        self.change_clothes.clothes_group2()
        self.change_superpower.superpower_group2()

    def coins_from401_to600(self):
        self.change_personage.personage_group3()
        self.change_clothes.clothes_group2()
        self.change_superpower.superpower_group2()

    def coins_from601_to800(self):
        self.change_personage.personage_group3()
        self.change_clothes.clothes_group3()
        self.change_superpower.superpower_group2()

    def coins_more801(self):
        self.change_personage.personage_group3()
        self.change_clothes.clothes_group3()
        self.change_superpower.superpower_group3()


if __name__ == '__main__':
    a = input("Enter your name: ")
    b = input("Do you want to invite friends? yes or no: ")
    c = input("Do you want to see ads? yes or no: ")
    d = input("Do you want to link a credit card to the account? yes or no: ")


    def get_coins():
        coins = []
        if a:
            coins.append(100)
        if b == "yes":
            coins.append(100)
        if c == 'yes':
            coins.append(300)
        if d == 'yes':
            coins.append(400)
        return coins

    coins = get_coins()

    authorization = Authorization()
    coins_amount = sum(coins)

    if coins_amount <= 100:
        authorization.coins_less100()
    elif 101 <= coins_amount <= 200:
        authorization.coins_from101_to200()
    elif 201 <= coins_amount <= 400:
        authorization.coins_from201_to400()
    elif 401 <= coins_amount <= 600:
        authorization.coins_from401_to600()
    elif 601 <= coins_amount <= 800:
        authorization.coins_from601_to800()
    else:
        authorization.coins_more801()
