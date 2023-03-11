class Song:

    """Класс для песни"""

    def __init__(self, name: str, length_in_sec: int, musician: list):
        """Конструктор, в который передается название, длина песни и список музыкантов"""
        self.name = name
        self.length_in_sec = length_in_sec
        self.is_listened = False
        self.musician = musician

    def __repr__(self) -> str:
        """Возвращает длину песни"""
        return str(self.length_in_sec) + " секунд"

    def __str__(self) -> str:
        """Дает информацию о музыкальной песне"""
        return 'Название песни: ' + self.name + ', длина песни: ' + repr(self)

    def set_listened(self):
        """Устанавливает значение, что музыкальная песня прослушана"""
        self.is_listened = True

    def print_musician(self):
        """Выводит список музыкантов"""
        print('Музыканты:')
        for musician in self.musician:
            print(musician)



class Neoclassik(Song):

    """Класс для неоклассической песни"""

    def __init__(self, name: str, is_for_boys: bool):
        """Конструктор, в который передается название неоклассической песни и информация, подходят ли она для мужчин"""
        self.name = name
        self.is_for_boys = boys

    def __repr__(self) -> str:
        """Возвращает текстовое значение для переменной is_for_boys"""
        if self.is_for_boys:
            return 'подходит для мужчин'
        else:
            return 'не подходит для мужчин'

    def __str__(self) -> str:
        """Выводит основную информацию о неоклассической песне"""
        return 'Название неоклассической песне: ' + self.name + ', ' + repr(self)

    def print_limitation(self):
        """В названии отсутствуют запрещенные слова, следовательно можно использовать в детских передачах"""
        print('Отсутствуют запрещенные слова')


song = song("В комарово", 203, ["Игорь Скляр"])
print(song)
print(repr(Song))
print("Песня прослушана: " + str(song.is_listened))
song.set_listened()
print("Песня прослушана: " + str(song.is_listened))
song.print_performers()

print()

Neoclassik = Neoclassik("Choice", False)
print(Neoclassik)
print(repr(Neoclassik))
Neoclassik.print_limitation()

