from numb3rs import validate
import unittest



class TestNumbers(unittest.TestCase):

    def test_validate(ip):
        assert validate("1.1.1.1") == True
        assert validate("255.255.255.255") == True
        assert validate("127.0.0.1") == True
        assert validate("456.678.567.789") == False
        assert validate("cat") == False
        assert validate("0.0.0.1000") == False
        assert validate("56.67,67.45") == False
        assert validate("256.255.67.45") == False
        assert validate("64.128.256.512") == False
        assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False


if __name__ == "__main__":
    unittest.main()

