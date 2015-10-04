import unittest
from DiceRoller import OctaDie
from DiceRoller import Throw

class TestDiceRoller(unittest.TestCase):

    def test_defendOctaDie(self):
        self.assertTrue(str(OctaDie(False).roll()) in ['Evade', 'Focus', 'Blank'])

    def test_attackOctaDie(self):
        self.assertTrue(str(OctaDie(True).roll()) in ['Hit', 'Critical Hit', 'Focus', 'Blank'])

    def test_octaDieRepr(self):
        self.assertTrue(isinstance(eval(repr(OctaDie(True))), OctaDie))

    def test_engagementRepr(self):
        self.assertTrue(isinstance(eval(repr(Throw(True, 3))), Throw))

if __name__ == '__main__':
    unittest.main()
