# Connect 4

Classic game of connect 4 (Tic Tac Toe but 4 in a row and gravity enabled placement of pieces)
Game is by default a 6x7 matrix game but `ROW_COUNT` and `COLUMN_COUNT` can be changed inside `connect4.py`.

## Files

- `connect4_logic.py` is the logic used for connect 4 and it runs the connect 4 in terminal
- `connect4.py` is the main file that runs the code as a pygame window
- assets folder contains all the assets used for the pygame window
- currently the game only uses few `.wav` files for sound. Images/webp are uploaded to replace the logic of drawing each time using pygame but is yet to be implemented

## Requirements
- Numpy (`pip install numpy`)
- Pygame (`pip install pygame`)

## Example

- Player 1 wins
  <br>
  ![Image](https://github.com/Rishabh4Jakhar/connect4/blob/main/assets/imgs/player1.jpeg?raw=True =400x400)
- Player 2 wins
  <br>
  ![Image](https://github.com/Rishabh4Jakhar/connect4/blob/main/assets/imgs/player2.jpeg?raw=True)
- Draw
  <br>
  ![Image](https://github.com/Rishabh4Jakhar/connect4/blob/main/assets/imgs/draw.jpeg?raw=True)
