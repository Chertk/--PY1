import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",") -> list[dict]:
     with open(filename) as file:
         listok = []
         x1 = [file.readline()]
         x1 = x1[0].split(delimiter)

         y1 = [file.read()]
         y1 = y1[0].split()

         for i in range(0, len(y1)):
             line = y1[i].split(delimiter)
             dict_ = {x1[i]: line[i] for i in range(0, len(line))}
             listok.append(dict_)
             print(dict_)
     return listok

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
