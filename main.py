import random 

class Character():
  def __init__(self, name, health="100", attack="20", mana="100", stamina="50"):
    self.name = name
    self.hp = health 
    self.ap = attack
    self.mp = mana
    self.stamina = stamina

  def take_dmg(self, dmg):
    self.hp -= dmg
    if self.hp < 0:
      self.hp = 0
    return self.hp

  def get_atk(self, defense_roll):
    atk = random.randint(0, self.ap)
    print(atk)
    if atk < defense_roll:
      atk = 0
    else:
      atk -= defense_roll 
    return atk 

  def is_dead(self):
    if self.hp < 1:
      self.hp = 0
      return True
    else:
      return False 



class StoryTeller():
  def __init__(self):
    print("welcome to the dark tower")
    self.new_game()

  def new_game(self):
    self.create_character()

  def create_character(self):
    pc_name = input("before you enter here you must give me your name: \n-> ")
    pc = Character(pc_name)

  def outside_the_tower(self):
    print("you stand before the great Dark tower. you have come here for a reason")
    print("Many have come here before. None have returnd")
    print("you know what must be done. you must enter the tower or you will perish")

    pc_input = input("dare you enter the Dark Tower? \n-> ")

    if pc_input == "yes":
      pass
    else:
      pass



new_game = StoryTeller()
