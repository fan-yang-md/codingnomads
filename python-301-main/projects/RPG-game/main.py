import time
import random
from characters import Hero, Monster, NPC, Pet

def main():
    print_welcome()
    play_game()

def print_welcome():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~
    Here you are! We have heard much of you! Indeed you are quite the sight to behold!
    We hear you have traveled here from the farthest corner of Barren Sea,
    an immensely impressive feat in itself, a tale that we must hear over many ales soon!
    For now, time is of the uttmost essence! As you know, monsters lurk in the forests...
    beyond our village's weak defenses. What they are and how many...that we do not know.
    They are venturing closers and closer to our village to feed...if...if...
    
    Please help us!
    ~~~~~~~~~~~~~~~~~~~~~
""")

def play_game():
    interactions = [
        NPC(name='NPC', goods={'armor repair': 10, 'weapon repair': 10, 'health potion':5}),
        Pet(name='Dragon', level=10, damage=100, defense=100),
        Pet(name='Wolf', level=5, damage=50, defense=30),
        Pet(name='Panda Bear', level=1, damage=1,defense=1),
        Pet(name='German Shepherd', level=5, damage=40, defense=40),
        Pet(name='Aussie', level=4, damage=30, defense=30),
        Monster(name='Gargoyle', level=50, damage=500,defense=500,treasure={'armor':100, 'gold':10}),
        Monster(name='Gargoyle', level=50, damage=500,defense=500,treasure={'armor':100, 'gold':10}),
        Monster(name='The Toad Prince', level=40, damage=400, defense=400, treasure={'armor':80, 'gold':5}),
        Monster(name='The Toad Prince', level=40, damage=400, defense=400, treasure={'armor':80, 'gold':5}),
        Monster(name='Fiend', level=20, damage=200, defense=100, treasure={'armor':10, 'sword':10, 'gold':2}),
        Monster(name='Basilisk', level=10, damage=100, defense=100, treasure={'armor':5, 'sword':5, 'gold':1}),
        Monster(name='Werewolf', level=20, damage=200, defense=300, treasure={'armor':30, 'gold':2}),
        Monster(name='Vampire', level=30, damage=300, defense=200, treasure={'sword':50, 'gold':3}),
        Monster(name='Vampire', level=30, damage=300, defense=200, treasure={'sword':50, 'gold':3}),
        Monster(name='Vampire', level=30, damage=300, defense=200, treasure={'sword':50, 'gold':3}),
        Monster(name='Giant Centipede', level=5, damage=50, defense=100, treasure={'armor':5}),
        Monster(name='Giant Centipede', level=5, damage=50, defense=100, treasure={'armor':5}),
        Monster(name='Lost Soul', level=1, damage=10, defense=0, treasure={'gold':1}),
        Monster(name='Lost Soul', level=1, damage=10, defense=0, treasure={'gold':1}),
        Monster(name='Lost Soul', level=1, damage=10, defense=0, treasure={'gold':1}),
        Monster(name='Lost Soul', level=1, damage=10, defense=0, treasure={'gold':1}),
        Monster(name='Lost Soul', level=1, damage=10, defense=0, treasure={'gold':1})
    ]

    hero = Hero(name=input("Please enter our hero's name:  "), hp=500,level=30,pet_name='',pet_level=0,damage=300,defense=300,gold=0)
    time.sleep(1)
    print(f'Welcome {hero.name}!!! We await your good news! Please take care!')

    time.sleep(1)

    print("So you head directly for the depth of the forest...")
    time.sleep(2)

    while True:
        #randomly interacts with a game character, NPC(), monster(), or pet().
        current_interaction = random.choice(interactions)
        choice = input(f'{current_interaction.name} appears in the distance. \
Would you like to get closer?\nEnter "y" to interact, any other key to avoid:  ').lower()
        
        if choice == 'y':
            if isinstance(current_interaction, Monster):
                print("It is a scary monster!")
                print(current_interaction)
                choice = input(f'Would you like to attack?\nEnter "y" to attack, or any other key to retreat:  ').lower()
                if choice == 'y':
                    hero_slays = hero.hero_attack(current_interaction)
                    if hero_slays == True:
                        interactions.remove(current_interaction)

                        # for character in interactions:
                        #     if isinstance(character, Monster):
                        #         return True # there are still monsters out there
                        # return False # no monsters left
                else:
                    print("You are a cautious one! Let's see what else is out here!")
                    time.sleep(2)

            if isinstance(current_interaction, Pet):
                print(f"Look it's a pet {current_interaction.name}!!")
                print(current_interaction)
                choice = input(f'Would you like to adopt?\nEnter "y" to adopt, or any other key to walk away:  ').lower()
                if choice == 'y':
                    hero.adopt(current_interaction)

            if isinstance(current_interaction, NPC):
                print(current_interaction)
                choice = input(f'Would you like to enter the shop?\nEnter "y" to enter, or any other key to walk away:  ').lower()
                if choice == 'y':
                    current_interaction.sell(hero)

if __name__ == '__main__':
    main()