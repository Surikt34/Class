# class Evengers:
 # ниже по 1 табу атрибуты класса, которые будут распространяться на все экземпляры класса.
 # Менять их не принято
 #    name = 'some_name'
 #    power = 0
 #    energy = 100
 #    hands = 2
# tor = Evengers() # Тор - это экземляр класса
# tor.name = 'Tor Odinson'
# tor.power = 100
# tor.alias = 'Tor'
# print(tor.name)
# print(tor.power)
# print(tor.energy)
# print(tor.hands)
# print(tor.alias)

# bruce = Evengers() # Брюс - это экземпляр класса
# bruce.name = 'Bruce Benner'
# bruce.power = 80
# bruce.alias = 'Hulk'
# print(bruce.name)
# print(bruce.power)
# print(bruce.energy)
# print(bruce.hands)
# print(bruce.alias)

# ниже метод соданный внутри класса. Все функции созданные внутри класса - это методы
# self - ссылается на конкретный экземпляр класса (который еще не создан). можно называть как хочется,
#но принято называть self
class Evengers:
    name = 'some_name'
    power = 0
    energy = 100
    hands = 2
    def eat(self, food): # на вход поступает еда
        if self.energy < 100: # если энергия <100
            self.energy += food # то энергия увеличивается на кол-во еды
        else:
            print('Not hungry') # иначе персонаж говорит что он не голоден


    def do_exercise(self, hours): # персонаж тренеруется
        if self.energy > 0: # если энергия больше 0
            self.energy -= hours * 2 # то его энергия падает по формуле часов тренировки
            self.power += hours * 2 # и его сила растет по кол-ву часов тренировки
        else:
            print('Too tired') # иначе персонаж говорит что он устал

bruce = Evengers()
bruce.name = 'Bruce Benner'
bruce.power = 85
print(bruce.alias)

