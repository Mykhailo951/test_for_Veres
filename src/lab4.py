class ArtificialTree:

    expiration_date = 12
    color = 'Green'


    def __init__(self, manufacturer = 'Unknown', height = 210, price = 2500, material = 'Plastic'):
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material


    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_manufacturer(self):
        return self.__manufacturer


    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height


    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


    def set_material(self, material):
        self.__material = material

    def get_material(self):
        return self.__material


    def __str__(self):
        return f'Виробник: {self.__manufacturer}, Висота: {self.__height} см, Ціна: {self.__price} грн., Матеріал: {self.__material}'


    def __repr__(self):
        return f'ArtificialTree({self.__manufacturer}, {self.__height}, {self.__price}, {self.__material})'


    def __del__(self):
        print(f'Видалений: {self.__manufacturer}')


def main():
    tree1 = ArtificialTree('GreenWorld', 190, 2000, 'Plastic')
    tree2 = ArtificialTree('CleanWorld', 160, 1500, 'Recycled')
    tree3 = ArtificialTree('GreenSpace', 170, 1900, 'PVC')

    print(tree1)
    print(tree2)
    print(tree3)

if __name__ == '__main__':
    main()






