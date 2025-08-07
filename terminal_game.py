import random

Hero = input('Enter your hero name: ')
main_char = Hero
hp = 100
print('Your health is', hp)
attack = 10
print('Your attack is', attack)
heal = 5
print('Your healing is', heal)

enemy = random.randint(1, 3)

if enemy == 1:
    print('You are fighting a Goblin!')
    enemy = 'Goblin'
elif enemy == 2:
    print('You are fighting a Troll!')
    enemy = 'Troll'
elif enemy == 3:
    print('You are fighting a Dragon!')
    enemy = 'Dragon'




ehp = 200
print('Enemy health is', ehp)
eattack = 5
print('Enemy attack is', eattack)



while hp > 0 and ehp > 0:
 random_event = random.randint(1, 5)
 

 print('Choose your move: ')
 print('1. Attack')
 print('2. Heal')

 print('Choose between 1 or 2:')
 choice = int(input())

 if choice == 1:
     dmg = attack * random_event
     ehp -= dmg
     print(f"You dealt {dmg} damage to the {enemy}")
     print(f'Enemy HP is now {ehp}')

     edmg = eattack * random_event
     hp -= edmg
     print(f'The {enemy} attacked you for {edmg} damage!')
     print(f'Your health is now {hp}')

 elif choice == 2:
     healing = heal * random_event
     hp += healing
     print(f"You healed for {healing} your hp now is {hp}")

     edmg = eattack * random_event
     hp -= edmg
     print(f'The {enemy} attacked you for {edmg} damage!')
     print('Your health is now {hp}')

 else:
  print('Invalid choice')
    
if hp <= 0:
    print("You died. Game over.")
elif ehp <= 0:
    print(f"You defeated the {enemy}! You win!")