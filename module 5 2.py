class House:
    def __init__(self, name, nof):
        self.name = name
        self.number_of_floors = nof
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'"{self.name}", количество этажей - {self.number_of_floors}.'
    # def go_to(self, new_floor):
    #     print(f'"{self.name}", количество этажей - {self.number_of_floors}.')
    #     if new_floor >= 1 and new_floor <= self.number_of_floors:
    #         for floor in range(1, new_floor+1):
    #             print(floor)
    #     else:
    #         print('Такого этажа не существует.')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)
# h2.go_to(10)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))