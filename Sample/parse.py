import re


class InputParser():

    #Parameted Constructor
    def __init__(self):
        input = ""

    def check(self, enteredstring):
        listwithoutspace = self.parse_space(enteredstring)
        if self.test_d(listwithoutspace) == 0:
            return 0
        elif self.test_number(listwithoutspace) == 0:
            return 0
        elif self.test_range(listwithoutspace) == 0:
            return 0
        elif self.test_modifier(listwithoutspace) == 0:
            return 0
        elif self.test_modifier_number(listwithoutspace) == 0:
            return 0
        elif self.test_modifier_range(listwithoutspace) == 0:
            return 0
        else:
            return 1

    def parse_space(self, enteredstring):
        osef = enteredstring.split(" ")
        print(osef)
        return osef

    def test_d(self, listwithoutspace):
        for var in listwithoutspace:
            i = 0
            for var2 in var:
                if var2 == "d":
                    i += 1
                if i > 1:
                    return 0
        return 1

    def test_number(self, listwithoutspace):
        for string in listwithoutspace:
            params_xy = re.split('(\+|-)', string)[0]
            tmp = params_xy.split("d")
            print(tmp)
            for char in tmp:
                if isinstance(int(char), int):
                    continue
                else:
                    return 0

    def test_range(self, listwithoutspace):
        for string in listwithoutspace:
            params_xy = re.split('(\+|-)', string)[0]
            tmp = params_xy.split("d")
            if 0 < int(tmp[0]) <= 100:
                print("")
            else:
                return 0
            if 2 <= int(tmp[1]) <= 100:
                print("")
            else:
                return 0

    def test_modifier(self, listwithoutspace):
        for string in listwithoutspace:
            i = 0
            for char in string:
                if char == "+" or char == "-":
                    i += 1
                if i > 1:
                    return 0
        return 1

    def test_modifier_number(self, listwithoutspace):
        for string in listwithoutspace:
            params_xy = re.split('(\+|-)', string)[2]
            if isinstance(int(params_xy), int):
                continue
            else:
                return 0

    def test_modifier_range(self, listwithoutspace):
        for string in listwithoutspace:
            params_xy = re.split('(\+|-)', string)[2]
            print(params_xy)
            if -100 <= int(params_xy) <= 100:
                continue
            else:
                return 0
