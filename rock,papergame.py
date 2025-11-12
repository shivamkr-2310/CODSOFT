#rock,paper&scissor game
import random

#computer choice
def get_computer_choice():
    return random.choice(['rock','paper','scissor'])

#determine winner
def determine_winner(user,computer):
    if user == computer:
        return "tie"
    elif(user == 'rock' and computer == 'scissor') or \
        (user == 'scissor' and computer == 'paper') or \
        (user == 'paper' and computer == 'rock'):
      return "win"
    else:
      return "lose"

#main    
def main():
   user_score = 0
   comp_score = 0
   print("Welcome to Rock-Paper-scissor")
   while True:
      user = input("choose rock,paper, or scissor: ").lower()
      if user not in ['rock','paper','scissor']:
         print("Invalid choice. try again.")
         continue
      comp = get_computer_choice()
      print(f"You chose: {user}")
      print(f"Computer choose: {comp}")
      result = determine_winner(user,comp)
      if result == "win":
         print("You win this round!")
         user_score += 1
      elif result == "loose":
         print("You lose this round.")
         comp_score += 1
      else:
         print("it's a tie.")
      print(f"score - You: {user_score} | Computer: {comp_score}")
      again = input("Play again? (y/n): ").lower()
      if again != 'y':
         print("Thanks for playing")
         break
      
if __name__ == "__main__":
     main()