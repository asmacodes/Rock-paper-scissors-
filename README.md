# Rock-paper-scissors-
This code is a simple Rock, Paper, Scissors game implemented in Python. The program allows the user to play against the computer.

The code starts by printing a welcome message and informing the user about the opponent being the computer.

The game revolves around three choices: rock, paper, and scissors. These choices are defined in the choices list. The outcomes dictionary maps each choice to its possible outcomes against the computer's choice. The outcomes are stored as strings, indicating whether the user wins, loses, or the game ends in a tie.

The program keeps track of the user's score and the computer's score using the variables user_score and computer_score, respectively.

The game runs in a continuous loop until the user decides to quit. In each iteration, the current scores are displayed. The user is prompted to enter their choice (rock, paper, or scissors) or "quit" to exit. If the user enters an invalid choice, they are prompted to try again.

The computer's choice is generated randomly using the random.choice() function.

The program then determines the outcome by accessing the outcomes dictionary based on the user's and computer's choices. The outcome is stored in the outcome variable.

The program displays the user's choice, the computer's choice, and the outcome of the round. If the user wins, their score is incremented. If the computer wins, its score is incremented. If it's a tie, no scores are changed.

The game continues until the user decides to quit. At the end of each round, the scores are displayed, and the user can make another choice or quit the game.
