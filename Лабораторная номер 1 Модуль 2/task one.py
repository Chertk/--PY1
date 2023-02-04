import doctest


 class Sofa:
     def __init__(self, legs_: int, number_of_people_sitting: int):
         """
         Создание и подготовка к работе объекта "Диван"
         :param legs_: Количество ножек у дивана
         :param number_of_people_sitting: Кол-во людей, которые могут сесть на диван полностью одновременно
         Примеры:
         >>> sofa = Sofa(3, 1)  # инициализация экземпляра класса
         """
         if not isinstance(legs_, int):
             raise TypeError("Кол-во ножек должно быть типа int")
         if legs_ < 2:
             raise ValueError("Кол-во ножек не может быть меньше 2")
         self.legs_ = legs_

         if not isinstance(number_of_people_sitting, (int)):
             raise TypeError("Кол-во людей, которые могут сесть на диван полностью одновременно должно быть типа int")
         if number_of_people_sitting > 1:
             raise ValueError("Людям будет больно")
         self.number_of_people_sitting = number_of_people_sitting

     def is_occupied_sofa(self) -> bool:
         """
         Функция которая проверяет сидит ли кто-нибудь на диване
         :return: Свободен ли диван
         Примеры:
         >>> sofa = Sofa(3, 0)
         >>> sofa.is_occupied_sofa()
         """
         ...

     def add_guest_to_sofa(self, guest: int) -> None:
         """
         Приглашение гостя присесть.
         :param guest: Кол-во гостей
         :raise ValueError: Если количество гостей превышает 1, то вызываем ошибку
         Примеры:
         >>> sofa = Sofa(3, 0)
         >>> sofa.add_guest_to_soofa(1)
         """
         if not isinstance(guest, int):
             raise TypeError("Кол-во гостей должно быть типа int")
         if guest > 1:
             raise ValueError("Людям будет больно")
         ...



 if __name__ == "__main__":
     doctest.testmod()  # тестирование примеров, которые находятся в документации