'''here we define a class in which we build characters of the game: Hero(), Monster().

Hero() is user-controlled.
Monster() is met at random and can be fought; if Heor() wins, treasure() can be collected from Monster().

Hero() and Monster() have the following stats: 
    - HP
    - Level
    - Damage
    - Defense
    - Gold / treasure

Pet() is met at random and you can adopt() to increase your Damage and Defense.
NPC() is met at random and can be interacted with to purchase() things. 

'''
import random
import time

class Hero:
    def __init__(self, name, hp, level, pet_name, pet_level, damage, defense, gold) -> None:
        self.name = name
        self.hp = hp
        self.level = level
        self.pet_name = pet_name
        self.pet_level = pet_level
        self.damage = damage
        self.defense = defense
        self.gold = gold
    
    def __str__(self):
        return f'Hero info:\n  Name: {self.name}\n  HP: {self.hp}\n  Level: {self.level}\
\n  Damage: {self.damage}\n  Defense: {self.defense}\n  Gold: {self.gold}'

## HERO ATTACK FUNCTION
    def hero_attack(self, monster):
        # battle commences...hero has the surprise advantage.
        print(f'You sneak up and attack {monster.name}!!\n... ...')
        time.sleep(2)
        hero_dice_roll = random.randint(5, 10) * self.level + self.damage + random.randint(1, 5) * self.pet_level
        monster_dice_roll = random.randint(1, 10) * monster.level + monster.defense

        if hero_dice_roll > monster_dice_roll: # hero wins the battle
            print(f'You slay the monster {monster.name}!!\n... ...')
            time.sleep(2)
            print(f'and find {monster.treasure} on their body.')
            time.sleep(1)
            if 'armor' in monster.treasure:
                self.defense += monster.treasure['armor']
            if 'sword' in monster.treasure:
                self.defense += monster.treasure['sword']
            if 'gold' in monster.treasure:
                self.gold += monster.treasure['gold']

            if monster.level - self.level > 2:
                self.level += 2
                print(f'You have leveled up to: Level {self.level}! Strong work!')

            elif monster.level - self.level >= 0:
                self.level += 1
                print(f'You have leveled up to: Level {self.level}! Strong work!')

            time.sleep(2)
            print(self)

            time.sleep(2)
            return True #return true only if hero slays monster.

        else: # hero doesn't slay and monster counter attacks
            print(f'A heroic effort, however the monster stands and has become enraged...and counter attacks!')
            time.sleep(2)
            # 2nd round commences. This time the monster holds the advantage.
            hero_dice_roll = random.randint(1, 10) * self.level + self.damage + random.randint(1, 5) * self.pet_level
            monster_dice_roll = random.randint(5, 10) * monster.level + monster.defense

            if hero_dice_roll > monster_dice_roll:
                print(f'You finally slay the monster {monster.name}!!\n... ...')
                time.sleep(2)
                print(f'and find {monster.treasure} on their body.')
                time.sleep(1)
                if 'armor' in monster.treasure:
                    self.defense += monster.treasure['armor']
                if 'sword' in monster.treasure:
                    self.defense += monster.treasure['sword']
                if 'gold' in monster.treasure:
                    self.gold += monster.treasure['gold']

                if monster.level - self.level > 2:
                    self.level += 2
                    print(f'You have leveled up to: Level {self.level}! Strong work!')

                elif monster.level - self.level >= 0:
                    self.level += 1
                    print(f'You have leveled up to: Level {self.level}! Strong work!')

                time.sleep(2)
                print(self)

                time.sleep(2)
                return True #return true only if hero slays monster.
            
            # if self.defense < monster.damage:
            #     self.hp = self.hp + self.defense - monster.damage
            #     if self.hp > 0:
            #         print(f'You have {self.hp} HP remaining...\n')
            #         time.sleep(2)
            #     else:
            #         print(f'You have succumbed to your wounds...\nGOOD GAME!')
            #         time.sleep(2)
            #         exit()
            # else:
            #     print("There is not a scratch on you! Next time you'll have no trouble with it!")
            #     time.sleep(2)
            
            # return False ##return false if the monster still lives.

    
## ADPOT A PET
    def adopt(self, pet):
        if self.pet_level > 0:
            pet_choice = input(f'You already have a pet. Would you like to replace\
 {self.pet_name} with {pet.name}? Enter "y" to replace, or any other key to keep {self.pet_name}.')
            if pet_choice.lower() == "y":
                self.pet_name = pet.name
                self.pet_level = pet.level
                pet.boost(self)
                print('Wonderful! Now you have a new pet!')
                print(self)
                print(pet)
        else:
            print('Congrats! Now you have a pet! What a wonderful surprise from the forest!')
            self.pet_name = pet.name
            self.pet_level = pet.level
            pet.boost(self)
            print(self)
            print(pet)
        
        time.sleep(2)

class Monster:
    def __init__(self, name, level, damage, defense, treasure) -> None:
        self.name = name
        self.level = level
        self.damage = damage
        self.defense = defense
        self.treasure = treasure
    
    def __str__(self):
        return f'\
    Monster: {self.name}\n\
    Level: {self.level}\n\
    Damage: {self.damage}\n\
    Defense: {self.defense}\n\
'

    def counter_attack(self, hero):

        print(f'{self.name} makes an counter-attack at You!!\n... ...')
        time.sleep(2)
        monster_dice_roll = random.randint(1, 10) * self.level + self.damage
        hero_dice_roll = random.randint(1, 10) * hero.level + hero.defense

        if hero_dice_roll > monster_dice_roll:
            print(f'You finally slat the monster {self.name}!!\n... ...')
            time.sleep(2)
            print(f'and find {self.treasure} on their body.')

            if 'armor' in self.treasure:
                hero.defense += self.treasure['armor']
            if 'sword' in self.treasure:
                hero.defense += self.treasure['sword']
            if 'gold' in self.treasure:
                hero.gold += self.treasure['gold']

            time.sleep(1)

            if hero.level - self.level > 2:
                hero.level += 2
                print(f'You have leveled up to: Level {hero.level}! Strong work!')

            elif hero.level - self.level >= 0:
                hero.level += 1
                print(f'You have leveled up to: Level {hero.level}! Strong work!')

            time.sleep(1)
            print("Let's see what else lurks in the forest!")
            time.sleep(1)
            return True #returns true when hero slays monster

        else:
            print(f'Monster retreats into the darkness to lick its wounds...next time no doubt!')
            time.sleep(2)

            if hero.defense < self.damage:
                hero.hp = hero.hp + hero.defense - self.damage
                if hero.hp > 0:
                    print(f'You have {hero.hp} HP remaining...\n')
                else:
                    print(f'You have succumbed to your wounds...\nGOOD GAME!')
                    exit()
            time.sleep(1)

            return False #returns false if the monster still lives.

class Pet:
    def __init__(self, name, level, damage, defense) -> None:
        self.name = name
        self.level = level
        self.damage = damage
        self.defense = defense

    def boost(self, hero):
        hero.damage += self.damage
        hero.defense += self.defense
        hero.pet_level = self.level

    def __str__(self):
        return f'Pet info:\n  Name: {self.name}\n  Level: {self.level}\n\
  Damage: {self.damage}\n  Defense: {self.defense}'


class NPC:
    def __init__(self, name, goods) -> None:
        self.name = name
        self.goods = goods
    def __str__(self):
        return f'NPC info:\n  Name: {self.name}\n  Goods for sale: {self.goods}'
    def sell(self, hero):
        while True:
            purchase = input(f'Our hero has {hero.gold} gold pieces. What would you like to pay for? Enter 1 for "Armor Repair",\
 2 for "Weapon Repair", 3 for "Health Potion", or 4 to leave shop.')
            if purchase == '1':
                item = 'armor repair'
            elif purchase == '2':
                item == 'weapon repair'
            elif purchase == '3':
                item == 'health potion'
            elif purchase == '4':
                return False
            if hero.gold >= self.goods[item]:
                hero.gold -= self.goods[item]
                if item == 'armor repair':
                    hero.defense += 100
                if item == 'weapon repair':
                    hero.damage += 100
                if item == 'health potion':
                    hero.hp += 500
                return True
            else:
                print("That is not enough gold, you poor bastard! Now get out!")
                return False
        print("Let's see what else is out there.")
        time.sleep(2)