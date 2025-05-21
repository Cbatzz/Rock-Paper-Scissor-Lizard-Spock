import random

player = 0
computer =  random.randint(1,5)

emojis = ["","✊","✋","✌️","🦎","🖖"]




# Title section of the game

print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

user = int(input("Pick a number: "))


# Rock casing
if user == 1 and computer == 2:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!")
elif user == 1 and computer == 3:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!")
elif user == 1 and computer == 4:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!")
elif user == 1 and computer == 5:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!")

# Paper Casing
elif user == 2 and computer == 1:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!")
elif user == 2 and computer == 3:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!")
elif user == 2 and computer == 4:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!")
elif user == 2 and computer == 5:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 

# Scissor Casing
elif user == 3 and computer == 1:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!")
elif user == 3 and computer == 2:  
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 
elif user == 3 and computer == 4:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 
elif user == 3 and computer == 5:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!")

# Lizard Casing
elif user == 4 and computer == 1:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!") 
elif user == 4 and computer == 2:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 
elif user == 4 and computer == 3:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!") 
elif user == 4 and computer == 5:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 

# Spock Casing

elif user == 5 and computer == 1:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 
elif user == 5 and computer == 2:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!") 
elif user == 5 and computer == 3:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player wins!") 
elif user == 5 and computer == 4:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Player loses!") 
else:
    print(f'You chose: {emojis[user]}')
    print(f'CPU chose: {emojis[computer]}')
    print("Tie")
