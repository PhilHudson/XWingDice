import random

def octaDie():
  """ Randomly picks a number from 0-7 """
  return random.randint(0,7)

rollInterpretationsAttack = {
  0:'Hit', 1:'Hit', 2:'Hit', 3:'Critical Hit', 4: 'Focus', 5:'Focus', 6:'Blank', 7:'Blank'
}

rollInterpretationsDefend = {
  0:'Evade', 1:'Evade', 2:'Evade', 3:'Focus', 4: 'Focus', 5:'Blank', 6:'Blank', 7:'Blank'
}

def interpretRoll(dictionary):
  """Return the value in the given dictionary for a random key."""
  myRoll = octaDie()
  myResult = dictionary.get(myRoll)
  return myResult

def attackOctaDie():
  """Rolls a hit (37.5% probability), crit (12.5%), focus (25%) or blank (25%)"""
  return interpretRoll(rollInterpretationsAttack)

def defendOctaDie():
  """Rolls an evade (37.5% probability), focus (25%) or blank (37.5%)"""
  return interpretRoll(rollInterpretationsDefend)

def multiRollOctaDie(count, function):
  return [ function() for x in range(count) ]

def multiRollDefendOctaDie(count):
  return multiRollOctaDie(count, defendOctaDie)

def multiRollAttackOctaDie(count):
  return multiRollOctaDie(count, attackOctaDie)

if __name__ == '__main__':
  attackCount = input("Number of attack dice: ")

  defendCount = input("Number of defence dice: ")
  print
  print "Attacker:"
  print multiRollAttackOctaDie(attackCount)
  print
  print "Defender:"
  print multiRollDefendOctaDie(defendCount)
