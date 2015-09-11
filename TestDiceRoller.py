import unittest
import DiceRoller

class TestDiceRoller(unittest.TestCase):

  def test_octaDie(self):
      self.assertTrue(DiceRoller.octaDie() in range(8))

  def test_defendOctaDie(self):
      self.assertTrue(DiceRoller.defendOctaDie() in ['Evade', 'Focus', 'Blank'])

  def test_attackOctaDie(self):
      self.assertTrue(DiceRoller.attackOctaDie() in ['Hit', 'Critical Hit', 'Focus', 'Blank'])

if __name__ == '__main__':
    unittest.main()
