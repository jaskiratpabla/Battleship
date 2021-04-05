# Battleship
A game of battleship in Python, full documentation and testing is included.
The function battleship(deployments) consumes a nested list deployments and returns a natural number corresponding to the number of valid guesses made. The consumed list is a list of lists of integers. The five inner lists provide the positions on the gameboard for each ship type (carrier, battleship, destroyer, submarine, and patrol boat), these inner lists will be of the following lengths: 5, 4, 3, 3, 2. 

Each integer in the inner lists is the number of a cell in a 10 by 10 grid where cells are numbered as shown below:

![image](https://user-images.githubusercontent.com/67871488/113637364-6c111980-9642-11eb-82fc-8687fcba4fea.png) 
 
The function behaves as follows:
- Read input from the keyboard with the prompt: Enter a guess:
- Checks for valid input (a number between 1 and 100). If the input is not valid, the function will output: You must enter a number between 1 and 100!. It will then re-prompt the user to enter a guess.
- If the input is a 'miss' meaning it missed all of the ships, the function will output: Miss!. It will then re-prompt the user to enter a guess.
- If the input is a 'hit' meaning it hit one of the ships, the function will output: Hit!.
- If not all ships have been sunk, it will re-prompt the user to enter a guess.
- If all ships have been sunk, then it will output: Game Over!. Then it will output the game board as described below.
- If the input was already guessed, Hit! or Miss! is reported as above as though the user had not already guessed the value already.

When printing the gameboard, the character for a cell is:
- the string "C" to represent the carrier, which spans 5 cells on the game grid
- the string "B" to represent the battleship, which spans 4 cells on the game grid
- the string "D" to represent the destroyer, which spans 3 cells on the game grid
- the string "S" to represent the submarine, which spans 3 cells on the game grid
- the string "P" to represent the patrol boat, which spans 2 cells on the game grid
- a "." (period) otherwise.

A single space between characters is printed on a line. That is, each line includes exactly 9 space characters and 10 characters that are ".", "C", "B", "D", "S", or "P".
