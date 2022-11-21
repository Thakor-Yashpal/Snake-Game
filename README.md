# Snake-Game
<iframe src="https://giphy.com/embed/jdFm2bcWlj4EUVCpc0" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/tokyo-revengers-tokyorev-rev-jdFm2bcWlj4EUVCpc0"></p>

# codepen preview : https://codepen.io/YASH-ITACHI/pen/rNKYxMN
A snake game is a simple game where a snake moves around a box trying to eat an apple. Once it successfully eats the apple, the length of the snake increases and the movement becomes faster.  Then the game is over when the snake runs into itself or any of the four walls of the box.
We have a div of class scoreDisplay that will display our scores.
There's a div of class grid that will house the game (this is going to be a 10 by 10 grid)
The class button basically contains a button for users playing the game on a phone (we will automate it with the keyboard for desktop user).
And the popup class will hold our replay button.
Now let's add some styling with CSS.


In the CSS, the grid which is the gameboard has a set dimension and a display of flex. This allows the contents (div) of this grid to line up in a horizontal manner as if they were inline elements instead of the normal block display which they possess.

The flex wrap property simply moves the divs to the next line, preventing them from going past the set dimension of their parent element (grid).

We will be dynamically creating the game board contents from JS but we can give a width and height here (with the .grid div). I included the comments here to help you actually see the divs, so as time goes on we will uncomment the code.

The snake and Apple classes are to show us where the snake and bonus is on the game, while the popup class is a fixed div that houses the replay div.

At this point, you should have something like this:


<center>
  
![snake game](https://user-images.githubusercontent.com/75574310/202585997-f708356b-ab30-490c-917e-76cf98844933.png)

  

  <center>

<center><h1>Display the snake</h1></center>
In this section, we will first establish a variable called tileCount which will divide our screen into 20 small squares. Then define the horizontal position of our snake as headX, and initialize it with value 10.

We will also define the vertical position of our snake as headY, and initialize it with value 10 which will center our snake.

Next is to define the initial size of our snake, by creating a variable called tileSize and assigning it a value of 18.

To display our snake, we create a function named drawSnake, and then call it on our primary function drawGame as shown in the code snippet below.**

# Use arrow keys to change the snake’s direction
# We will set two variables named xvelocity and yvelocity, and initialize them with values zero.

Conclusion
Fun projects are best to learn any programming language. In this project, we learned how to create a game using JavaScript.

We creates a snake game using the HTML’s canvas element and JavaScript methods to play the game depending on the set rules.

#Happy coding!

