import unittest

def romano_a_entero(romano):
    lista= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    entero=0

    for i in range(len(romano)):
        if i > 0 and lista[romano[i]]>lista[romano[i-1]]:
            entero += lista[romano[i]] - 2* lista[romano[i-1]]
        else:
            entero += lista[romano[i]]

    return entero


class TestDecimalToRoman(unittest.TestCase):

    
    def test_2(self):
        roman_number = romano_a_entero('II')
        self.assertEqual(roman_number, 2)

        
    def test_12(self):
        roman_number = romano_a_entero('XII')
        self.assertEqual(roman_number, 12)

        
    def test_18(self):
        roman_number = romano_a_entero('XVIII')
        self.assertEqual(roman_number, 18)

        
    def test_50(self):
        roman_number = romano_a_entero('L')
        self.assertEqual(roman_number, 50)

        
    def test_57(self):
        roman_number = romano_a_entero('LVII')
        self.assertEqual(roman_number, 57)

        
    def test_82(self):
        roman_number = romano_a_entero('LXXXII')
        self.assertEqual(roman_number, 82)

        
    def test_44(self):
        roman_number = romano_a_entero('XLIV')
        self.assertEqual(roman_number, 44)

        
    def test_75(self):
        roman_number = romano_a_entero('LXXV')
        self.assertEqual(roman_number, 75)

        
    def test_249(self):
        roman_number = romano_a_entero('CCXLIX')
        self.assertEqual(roman_number, 249)

        
    def test_283(self):
        roman_number = romano_a_entero('CCLXXXIII')
        self.assertEqual(roman_number, 283)

        
    def test_366(self):
        roman_number = romano_a_entero('CCCLXVI')
        self.assertEqual(roman_number, 366)

        
    def test_500(self):
        roman_number = romano_a_entero('D')
        self.assertEqual(roman_number, 500)

        
    def test_1366(self):
        roman_number = romano_a_entero('MCCCLXVI')
        self.assertEqual(roman_number, 1366)
    
   


if __name__ == '__main__':
    unittest.main() 