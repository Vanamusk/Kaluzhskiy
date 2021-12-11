from abc import ABC, abstractmethod
from random import randint
from string import ascii_letters

class Nucleotides(ABC):
    bases = {x: y for (x, y) in zip(list(ascii_letters), list(ascii_letters))}
    def __init__(self, order: str):
        if not isinstance(order, str):
            raise ValueError("order must be str")

        for nuc in order:
            if nuc not in self.bases:
                raise ValueError(f"unexpected sign {nuc} in order")
        self.order = order.upper()
            
    def Complimentary(self):
        new_string = ""
        for i in self.order:
            new_string += self.bases[i]
        return new_string
    
    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self.order + other.order)
        elif isinstance(self, type(other)):
            return type(other)(self.order + other.order)
        else:
            return NotImplemented
    def __mul__(self, other):
        if isinstance(other, type(self)):
            _type = type(self)
        elif isinstance(self, type(other)):
            _type = type(other)
        else:
            return NotImplemented

        new_string = ""
        for pair in zip(self.order, other.order):
            new_string += pair[randint(0, 1)]
        new_string += (self.order[len(new_string):]
                    if len(self.order) > len(other.order)
                    else other.order[len(new_string):])

        return _type(new_string)

    def __str__(self):
        return f"{type(self).__name__} : \n {self.order}"

    def __getitem__(self, item):
        return self.order[item]

    def __eq__(self, other):
        if isinstance(self, type(other)) and isinstance(other, type(self)):
            return self.order == other.order
        else:
            raise ValueError(f"can't compare {type(self)} with {type(other)}")

class RNA(Nucleotides):
    bases = {'A': 'T',
             'U': 'A',
             'G': 'C',
             'C': 'G'}

    def __init__(self, order):
        super().__init__(order)

    def to_DNA(self):
        return DNA(self.Complimentary())

class DNA(RNA):
    bases = {'A': 'T',
             'T': 'A',
             'G': 'C',
             'C': 'G'}

    def __init__(self, order):
        super().__init__(order)

    def __getitem__(self, item):
        return [self.order[item], self.Complimentary[self.order[item]]]

    def __str__(self):
        return f"{type(self).__name__}: \n {self.order} \n {self.Complimentary()}"
