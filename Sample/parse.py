class InputParser():

    #Parameted Constructor
    def __init__(self):
        input = ""

    def check(self, enteredstring):
        listwithoutspace = self.parse_space(enteredstring)
        if self.test_d(listwithoutspace) == 0:
            return 0
        else:
            listwithoutd = self.parse_d(listwithoutspace)
        print(listwithoutd)
        return 1

    def parse_space(self, enteredstring):
        osef = str(enteredstring.split(" "))
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

    def parse_d(self, listwithoutspace):
        for var in listwithoutspace:
            listwithoutd = var.split("d")
        return listwithoutd
