from random import randint

def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) != 15:
        num = [randint(-10, 10) for _ in range(15)]
        for i in num:
            if i not in list_:
                list_.append(i)
        return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
