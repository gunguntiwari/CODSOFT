import random
alternative = ("rock","paper","scissors")
contestant = input("Enter rock, paper or scissors: ").lower()
machine = random.choice(alternative)




if contestant  not in alternative:
    print("unfounded input, please enter rock, paper, or scissors.")


else:
    

 print("computer chose:",machine)


if contestant  == machine:
    print("it's a draw!")
elif (
     (contestant  == "rock" and machine == "scissors")or 
     (contestant  == "scissors" and machine == "paper") or
     (contestant  == "paper" and machine == "rock")  
     ) :
     print(" you're a winner!") 
else:
  print("better luck next time!") 
                
                  

