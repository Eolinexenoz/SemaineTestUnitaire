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
        else:
            return 1

    def parse_space(self, enteredstring):
        osef = enteredstring.split(" ")
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
            tmp = string.split("d")
            for char in tmp:
                if isinstance(int(char), int):
                    continue
                else:
                    return 0




