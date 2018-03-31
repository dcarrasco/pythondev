from functools import reduce

class Collection:
    def __init__(self, items):
        self.items = list()
        for item in items:
            self.items.append(item)

    def all(self):
        return self.items

    def __str__(self):
        return str(self.items)

    def dump(self):
        return "DUMP:" + str(self.items)

    def map(self, function):
        self.items = list(map(function, self.items))
        return self

    def flatmap(self, function):
        # return self.all()
        self.items = reduce(list.__add__, self.map(function).all())
        return self

    def sort(self, function):
        self.items = sorted(self.items, key=function)
        return self

