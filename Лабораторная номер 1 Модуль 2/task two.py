import doctest


 class Pepperpot:
     def __init__(self, pepper: float, capacity_of_the_pepper_pot: float):
        """
        Создание и подготовка к работе объекта "Перечница"
        :param pepper: кол-во перца в кг
        :param capacity_of_the_pepper_pot: вместимость перечницы в л
        Примеры:
        >>> pepper_pot = Pepperpot(0.42, 0.57)  # инициализация экземпляра класса
        """
        if not isinstance(pepper, (int, float)):
            raise TypeError("Кол-во перца должно быть типа int или float")
        if pepper <= 0:
            raise ValueError("Кол-во перца должно быть положительным числом")
        self.pepper = pepper

        if not isinstance(capacity_of_the_pepper_pot, (int, float)):
            raise TypeError("Вместимость перечницы должна быть int или float")
        if capacity_of_the_pepper_pot < 0:
            raise ValueError("Вместимость перечницы может быть отрицательным числом")
        self.capacity_of_the_pepper_pot = capacity_of_the_pepper_pot

     def is_empty_pepperpot(self) -> bool:
         """
         Функция которая проверяет является ли перечницы пустой
         :return: Является ли перечницы пустой
         Примеры:
         >>> pepper_pot = Pepperpot(0.4, 0.6)
         >>> pepper_pot.is_empty_pepperpot()
         """
         ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации