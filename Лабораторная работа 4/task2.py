dict_ = {}
DEFAULT_COUNT = 0

def get_count_char(str_):
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha():
            dict_[symbol] = dict_.get(symbol, DEFAULT_COUNT) + 1
    return dict_

def get_char(dict_):
    count = sum(dict_.values())
    for letter in dict_:
        dict_[letter] = round(dict_[letter] / count * 100, 1)
        return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
