import random
from collections import Counter
# >>> dict((x,l.count(x)) for x in set(l))

class OctaDie(object):
    """An eight-sided die (octahedron) instantiated for either attack or defence.

    In attack, the faces of the die are, with their associated probability:
        Hit          (3 of 8, 37.5% probability)
        Critical Hit (1 of 8, 12.5%)
        Focus        (2 of 8, 25%)
        Blank        (2 of 8, 25%)

    In defence, the faces of the die are:
        Evade        (3 of 8, 37.5%)
        Focus        (2 of 8, 25%) 
        Blank        (3 of 8, 37.5%)
        
    Attributes:
        attacking: boolean determining whether this die is an attack die or a
            defence die.
        faces: Dictionary of available faces from which to select at random the
            showing face.
        faceShowing: The face which is showing after a roll of the die.
    """

    attackFaces = [
        'Hit', 'Hit', 'Hit', 'Critical Hit', 'Focus', 'Focus', 'Blank', 'Blank'
    ]

    defenceFaces = [
        'Evade', 'Evade', 'Evade', 'Focus', 'Focus', 'Blank', 'Blank', 'Blank'
    ]

    def __init__(self, attacking, faceShowing='Blank'):
        """Return an OctaDie object.

        The OctaDie is for attack if *attacking* is True, or for defence 
        otherwise, with the *faceShowing* face (a blank, by default) showing."""
        self.attacking = attacking
        if attacking:
            self.faces = OctaDie.attackFaces
        else:
            self.faces = OctaDie.defenceFaces
        self.faceShowing = faceShowing

    def roll(self):
        """Return a new freshly rolled OctaDie."""
        return OctaDie(self.attacking, random.choice(self.faces))

    def __str__(self):
        return self.faceShowing

    def __repr__(self):
        return "OctaDie(%s, '%s')" % (str(self.attacking), self.faceShowing)
      
class Throw(object):
    """A simultaneous throw of one or more OctaDie objects.

    Attributes:
        attacking: boolean determining whether this Throw is an attack or
            defence.
        octaDieCount: The number of dice to roll.
        dice: List of OctaDie dice making up the throw, each with a face showing. 
    """

    def __init__(self, attacking, diceCount=1, preRolledDice=None):
        """Return a Throw object with *diceCount* dice.
        
        The throw is an attack if *attacking* is True or a defence otherwise. If
        *preRolledDice* is not None, for instance if re-creating or copying a 
        Throw object, then its length must be *diceCount*."""
        self.attacking = attacking;
        self.diceCount = diceCount;
        if preRolledDice == None:
            self.dice = [ OctaDie(attacking) for ignoredValue in range(diceCount) ]
        else:
            assert len(preRolledDice) == diceCount
            for die in preRolledDice:
                assert isinstance(die, OctaDie)
            self.dice = preRolledDice

    def throw(self):
        """Return a new Throw with all the dice from this Throw freshly rolled."""
        return Throw(self.attacking, self.diceCount,
                     [ die.roll() for die in self.dice ])
    
    def tally(self):
        """ Return a Counter object tallying the faces of the dice in this Throw."""
        return Counter([ die.faceShowing for die in self.dice ])
    
    def __str__(self):
        return str([str(die) for die in self.dice])

    def __repr__(self):
        return "Throw(%s, %s, [%s])" % \
            (str(self.attacking), str(self.diceCount), \
             ', '.join([repr(die) for die in self.dice]))

if __name__ == '__main__':
    attackCount = input("Number of attack dice: ")
    
    defendCount = input("Number of defence dice: ")
    print
    print "Attacker:"
    print Throw(True, attackCount).throw().tally()
    print
    print "Defender:"
    print Throw(False, defendCount).throw().tally()
