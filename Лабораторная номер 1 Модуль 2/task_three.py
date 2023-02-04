import doctest


 class Box:
     def __init__(self, number_of_box: int, number_of_wrist_watch: int):
         """
         Создание и подготовка к работе объекта "Ящик"
         :param number_of_box: Кол-во ящиков
         :param number_of_wrist_watch: Кол-во наручных часов, которое нужно сложить в ящики
         Примеры:
         >>> box = Box(8, 8)  # инициализация экземпляра класса
         """
         if not isinstance(number_of_box, int):
             raise TypeError("Кол-во ящиков должно быть типа int или float")

        if number_of_box <= 0:
         raise ValueError("Если число ящиков < 0, то складывать некуда")
        self.number_of_box = number_of_box

        if not isinstance(number_of_box, int):
         raise TypeError("Кол-во наручных часов, которое нужно сложить в ящики должно быть типа int")
        if number_of_wrist_watch < 0:
         raise ValueError("Если число наручных часов < 0, то класть нечего")
        if number_of_wrist_watch > number_of_wrist_watch:
         raise ValueError("Если число наручных часов > числа ящиков, то класть лишние наручные часы некуда")
        self.number_of_wrist_watch = number_of_wrist_watch


    def remove_wrist_watch_from_Box(self, estimate_wrist_watch: int) -> None:
        """
        Извлечь наручные часы из ящика.
        :param estimate_wrist_watch: Кол-во извлеченных наручных часов
        :raise ValueError: Если количество извлеченных наручных часов превышает количество наручных часов в ящике,
        то возвращается ошибка.
        :return: Объем реально извлеченных наручных часов
        Примеры:
        >>> box = Box(8, 8)
        >>> box.remove_wrist_watch_from_Box(3)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации