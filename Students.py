import json
list_ = []
with open("data.json", 'r', encoding="utf-8") as f:
    data = json.load(f)
    for student in data:
        list_.append(student)
class Student:
    def __init__(self, name, age, gender):
        self.姓名 = name
        self.年龄 = age
        self.学号 = gender
def menu():
    while True:
        print("-" * 42)
        print("1.添加 2.删除 3.修改 4.检索 5.列出全部 6.保存")
        print("-" * 42)
        try:
            n = int(input("输入功能编号:\n"))
            if n == 1:
                add_()
            elif n == 2:
                del_()
            elif n == 3:
                revise_()
            elif n == 4:
                find_()
            elif n == 5:
                list_s()
            elif n == 6:
                save_()
                break
        except ValueError:
            print("input error")

def add_(lists=list_):
    n = input("输入姓名:\n")
    for i in lists:
        if i["姓名"] == n:
            print("该生已存在")
            return
    nn = int(input("输入年龄:\n"))
    nnn =input("输入学号:\n")
    lists.append(Student(n,nn,nnn).__dict__)
def del_(lists=list_):
    flag = False
    n = input("输入姓名:\n")
    for i in range(len(lists)):
        if lists[i]["姓名"] == n:
            del lists[i]
            flag = True
            break
    if flag == False:
        print('没这个人欸')
def revise_(lists=list_):
    flag = False
    nn = input("修改谁的:\n")
    n = int(input("你要修改什么:1.姓名 2.年龄 3.学号\n"))
    for i in range(len(lists)):
        if lists[i]["姓名"] == nn:
            if n == 1:
                for i in range(len(lists)):
                    if lists[i]["姓名"] == nn:
                        flag = True
                        lists[i]["姓名"] =input("输入姓名:\n")
                        break
            elif n == 2:
                for i in range(len(lists)):
                    if lists[i]["姓名"] == nn:
                        flag = True
                        lists[i]["年龄"] = int(input("输入年龄:\n"))
                        break
            elif n == 3:
                for i in range(len(lists)):
                    if lists[i]["姓名"] == nn:
                        flag = True
                        lists[i]["学号"] = input("输入学号:\n")
                        break
    if flag == False:
        print("没这个人欸")
def find_(lists=list_):
    flag = False
    n = input("输入要查找的人:\n")
    for i in lists:
        if i['姓名'] == n:
            flag = True
            print(i)
            break
    if flag == False:
        print("没这个人欸")
def list_s(lists=list_):
    for i in lists:
        print(i)
def save_(lists=list_,path="./data.json"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(lists, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    lists = [{"姓名":"1","年龄":1,"学会":"001"}]
    add_(lists)