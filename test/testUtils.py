import unittest
from src import utils as ut

class TestUtilsMethods(unittest.TestCase):

  def test_get_ascii_letters(self):
    letters = ut.getAsciiLetters()
    self.assertEqual(len(letters), 256)
    self.assertEqual('a', letters[97])

if __name__ == '__main__':
  unittest.main()