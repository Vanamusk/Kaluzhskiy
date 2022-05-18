def author(name):
    def decor(func):
        func._author = name
        return func
    return decor

@author("Dany Longo")
def add2(num: int) -> int:
    return num + 2
