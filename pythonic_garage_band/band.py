
from unicodedata import name


class Musician():
    def __init__(self, name):
        self.name = name
    def play_solo(self):
        print("{self.name} is playing.")

class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is {self.name} and I play guitar"
    def __repr__(self):
        return "Guitarist instance. Name = {self.name}"
    def get_instrument():
        return 'guitar'
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is {self.name} and I play bass"
    def __repr__(self):
        return "Bassist instance. Name = {self.name}"
    def get_instrument():
        return 'bass'
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "My name is {self.name} and I play drums"
    def __repr__(self):
        return "Drummer instance. Name = {self.name}"
    def get_instrument():
        return 'drums'
    def play_solo(self):
        return "rattle boom crash"

class Band():
    def __init__(self, name, members):
        self.name = name
        self.members = members
    def play_solos(self):
        for member in self.members:
            member.play_solo()