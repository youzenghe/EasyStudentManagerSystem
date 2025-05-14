# from Students import menu as m
# m()
import json
list_ = []
with open("data.json", 'r', encoding="utf-8") as f:
    data = json.load(f)
    for student in data:
        list_.append(student)
print(list_[0])