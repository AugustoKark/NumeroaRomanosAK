import unittest


def convert_decimal_to_roman(decimal_number):
    roman_number = ''
    decimal_number = int(decimal_number)
    if decimal_number < 1 or decimal_number > 3999:
        return 'out of range'
    else:
        while decimal_number > 0:
            for roman, decimal in (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
             ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5),
             ('IV', 4), ('I', 1)):
                while decimal_number >= decimal:
                    roman_number += roman
                    decimal_number -= decimal
        return roman_number
    '''roman1 = ''
    roman2 = ''
    roman3 = ''
    decimal_number_units = decimal_number%10
    decimal_number_decenas = (decimal_number%100-decimal_number%10)//10
    decimal_number_centenas= decimal_number%1000//100

    if decimal_number_centenas:
         for digit in range(decimal_number_centenas):
            if decimal_number_centenas<4:
                roman3 += 'C'
            if decimal_number_centenas==4:
                roman3 = 'CD'
            if decimal_number_centenas==5:
                roman3 = 'D'
            if 5<decimal_number_centenas<9:
                restcen= decimal_number_centenas-5
                roman3 = 'D'+ 'C'*restcen
            if decimal_number_centenas==9:
                roman3 = 'CM'
            
        
    
    if decimal_number:
        for digit in range(decimal_number_decenas):
            if decimal_number_decenas<4:
                roman1 += 'X'
            if decimal_number_decenas == 4:
                roman1= 'XL'
            if decimal_number_decenas == 5:
                roman1= 'L'
            if 5< decimal_number_decenas <9:
                restdec= decimal_number_decenas-5
                roman1= 'L'+ 'X'*restdec
            if decimal_number_decenas == 9:
                roman1 = 'XC'


        for digit in range(decimal_number_units):
            if decimal_number_units < 4:
                roman2 += 'I'
            if decimal_number_units == 4:
                roman2 = 'IV'
            if decimal_number_units == 5:
                roman2 = 'V'
            if 5< decimal_number_units <9:
                restuni=decimal_number_units-5
                roman2 ='V' + 'I'*restuni
            if decimal_number_units == 9:
                roman2= 'IX'



    roman = roman3 + roman1 + roman2

    return roman '''

class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')

    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, "III")

    def test_5(self):
        roman_number = convert_decimal_to_roman(5)
        self.assertEqual(roman_number, "V")

    def test_7(self):
        roman_number = convert_decimal_to_roman(7)
        self.assertEqual(roman_number, "VII")

    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, "X")

    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual(roman_number, "XI")

    def test_12(self):
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual(roman_number, "XII")

    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, "XX")

    def test_21(self):
        roman_number = convert_decimal_to_roman(21)
        self.assertEqual(roman_number, "XXI")

    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual(roman_number, "XXIII")

    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, "XXX")

    def test_35(self):
        roman_number = convert_decimal_to_roman(35)
        self.assertEqual(roman_number, "XXXV")

    def test_37(self):
        roman_number = convert_decimal_to_roman(37)
        self.assertEqual(roman_number, "XXXVII")

    def test_47(self):
        roman_number = convert_decimal_to_roman(47)
        self.assertEqual(roman_number, "XLVII")

    def test_53(self):
        roman_number = convert_decimal_to_roman(53)
        self.assertEqual(roman_number, "LIII")
    
    def test_89(self):
        roman_number = convert_decimal_to_roman(89)
        self.assertEqual(roman_number, "LXXXIX")

    def test_126(self):
        roman_number = convert_decimal_to_roman(126)
        self.assertEqual(roman_number, "CXXVI")
    

    def test_474(self):
        roman_number = convert_decimal_to_roman(474)
        self.assertEqual(roman_number, "CDLXXIV")
    



if __name__ == '__main__':
    unittest.main()