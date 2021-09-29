# Tetris (pygame)

My first go at making Tetris

* Random fun project I decided to pick up to dabble myself in some pygame

## Function

* Key Bindings
  * Arrow keys to move
    * Up arrow to rotate
  * Press C to hold piece
  * Tap Space to drop instantly
* Points
  * You gain points by clearing an entire row See how high you can go!(Doesn't save score)
  * My highest: 10400 (before I got bored outta my mind)

## Plans

* Revamping the code of how the tetrominos are made so some of the code is easier to read
* Extra Feature: Making it increasingly harder by dropping the pieces faster as your score reaches certain thresholds
  * Difficulty levels where you can just immediately start at a certain difficulty (speed)
* Extra Feature: Showing the outline at the bottom of where the tetromino will land
* Extra Feature: Menu and a gameover scene
* Extra Feature: Showing the upcoming (3) pieces
* Fixing bug: Clipping into other pieces when rotating if there's no space
* Fixing bug: The tetrominos not being centered in hold slot
* Fixing bug: Score noclippin when the number gets too high

## Problems

* I made some huge mistakes near the beginning, I used coordinates to form my tetrominos.
  * Thus, when rotating, I had to meticulously change the coordinates to make them rotate correctly.

    ```python
      if amount == 1:
              self.coords[0][0] -= 1
              self.coords[0][1] += 1
              self.coords[2][0] += 1
              self.coords[2][1] -= 1
              self.coords[3][0] += 2
              self.coords[3][1] -= 2
    ```

  * Flipped the x and y coordinates for the tetrominos (0 and 1's in the second bracket should be flipped) because of pygames formatting for the grid but I instead should've flipped the grid.
* Using pre-formatted tetrominos would've have saved a lot of pain
  
  ```python
    ['-----',
    '--00-',
    '-00--',
    '-----']
  ```
