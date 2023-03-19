player1 = str(input("Whats your move? "))
player2 = str(input("Whats your move? "))

if((player1.lower() == "rock" and player2.lower() == "scissors") or (player1.lower() == "scissors" and player2.lower()=="paper") or  (player1.lower() == "paper" and player2.lower()=="rock")):
    print("Player 1 wins!")
elif((player2.lower() == "rock" and player1.lower() == "scissors") or (player2.lower() == "scissors" and player1.lower()=="paper") or  (player2.lower() == "paper" and player1.lower()=="rock")):
    print("Player 2 wins!")
else:
    print("Tie!")