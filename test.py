import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test(self):
        nam='Madhuban'
        upper_name=to_upper(name)
        self.assertEqual(upper_name,'MADHUBAN')

if __name__ == '__main__':
    unittest.main()