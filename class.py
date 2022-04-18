# definition
class People:
    """People class"""
    name = ""
    age = 0

    def __init__(self, n, a):
        """initialization"""
        self.name = n
        self.age = a

    def speak(self):
        """self-intro"""
        print("I'm", self.name, "of", self.age)


Jack = People("Jack", 20)
Jack.speak()


# inheritance
class Cops(People):
    """inheritance of People"""
    cop_id = 0000

    def __init__(self, n, a, c):
        People.__init__(self, n, a)
        self.cop_id = c

    def speak(self):
        print("I'm police officer", self.cop_id)


Jack = Cops("Jack", 20, 2222)
Jack.speak()


class Rookie(Cops):
    """inheritance of People and Cops"""
    rookie_id = 101

    def __init__(self, n, a, c, d):
        """initialization"""
        People.__init__(self, n, a)
        Cops.__init__(self, n, a, c)
        self.rookie_id = d

    def speak(self):
        """self-intro"""
        print("I'm a new cop", self.rookie_id)


Jack = Rookie("Jack", 20, 1111, 21)
Jack.speak()
