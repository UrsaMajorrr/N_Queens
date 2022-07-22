# N_Queens
I undertook this project last week because I wanted to practice my programming skills after reading the book [Composing Programs](https://composingprograms.com). I didn't want to lose my understanding of what I learned in that book, mostly the recursive topics. The N Queens problem uses a backtracking algorithm to find a solution. This backtracking algorithm contains recursive elements, that will allow me to solidfy my understanding of recursion.

Overall, this project took me about 10 hours if you factor in the time I needed to learn about backtracking and how it works. To me, 10 hours is not that long to put a project like this on your github and even show it off on a resume. 

In this README, I will be talking about what I learned about backtracking itself and problems I ran into when writing this program as well as improvements I could make to the code that I found after looking over it again.

# Learning Backtracking
To learn backtracking I turned to the [Geeks for Geeks](https://www.geeksforgeeks.org/backtracking-introduction/?ref=lbp) series on backtracking where they give a brief introduction and a list of common backtracking problems. I started by reading the introduction, of course. I will explain in my own words the backtracking algorithm below.

**Backtracking** is an algorithm that solves combinatorial problems. It does this by taking a possible value and checks it against constraints (if they exist) to determine its validity. It will do this recursively by *backtracking* to update solutions as necessary to fit within the given constraints.

I hope I explained that well enough. In order, to learn backtracking, I first decided to run through the Sudoku Solver problem on Geeks for Geeks. This helped me understand the basic concepts and how the algorithm can be implemented into code. 

I noticed some basic concepts that showed up when implementing this algorithm into code. First, you should determine your base case. For N Queens, the base case is if you have run through all of the columns on the board. If that's true then great, you're done, if it's not then keep going. You might have more than one base case. If I remember correctly, sudoku had 2. Second, you have to figure out what value you want to store recursively. Once you do that you will be storing it in a for loop. For N Queens you wanted to store the row position of the previous queen you just placed. I like to think of this value as the value that is going to change that is also relevant to the solution. Basically, the value that you are going to check for validity. In sudoku, that's the numbers 1-9. In N Queens its the position of the Queens.

From there it really is not that difficult to implement backtracking into your code. One of the more difficult parts is checking for validity. This is where I will discuss problems I had writing this code.

#Problems I Fixed
