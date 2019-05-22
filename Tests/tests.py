import unittest
import re

enteredstring = input("Entrez les des a lancer  : ")


class Tests(unittest.TestCase):

    def test_modifierseul(self):
        modifbool = False
        modifnb = 0
        tab = enteredstring.split()
        for var in tab:
            for var2 in var:
                if var2 == '+' or var2 == '-':
                    modifnb += 1
            if modifbool == 0 or modifbool == 1:
                modifbool = True
            self.assertTrue(modifbool)

    def test_dseul(self):
        dbool = False
        dnb = 0
        tab = enteredstring.split()
        for var in tab:
            for var2 in var:
                if var2 == 'd':
                    dnb += 1
            if dnb == 1:
                dbool = True
            self.assertTrue(dbool)

    def test_isnumber(self):
        tab = enteredstring.split()
        for var in tab:
            tab2 = var.split('d')
            for var2 in tab2:
                self.assertIsInstance(int(var2), int)

    def test_isinrange(self):
        # Test non fonctionnel la REGEX ne passe pas
        tab = enteredstring.split()
        for var in tab:
            tab2 = re.split("|\+|-", var)[0]
            for var2 in tab2:
                x = var2.split('d')[0]
                self.assertTrue(0 < int(x) <= 100)

    def test_isinrange(self):
        # Test non fonctionnel la REGEX ne passe pas
        tab = enteredstring.split()
        for var in tab:
            tab2 = re.split("|\+|-", var)[0]
            for var2 in tab2:
                y = var2.split('d')[0]
                self.assertTrue(2 < int(y) <= 100)

    def test_modifisinrange(self):
        #Test non fonctionnel la REGEX ne passe pas
        tab = enteredstring.split()
        for var in tab:
            modif = re.split("|\+|-", var)[1]
            self.assertTrue(-100 < int(modif) <= 100)


unittest.main()