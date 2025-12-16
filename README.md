# Solver for the Coundown numbers game
This repo implements a solver for the numbers part of the coundown game using DFS and memoisation. 

## What is Countdown
The Countdown numbers game is a game where you are given 6 numbers (positive integers less than 100) and have to use the standard operators (+, -, *, /) to create the goal number (a positive integer less than 1,000). My code allows for the use of nested brackets e.g. (5 * 2) + (14 /7). You can play countdown at https://happysoft.org.uk/countdown/numgame.php (This is not my website). Thank you to El_Tel for creating the countdown game website and to Channel 4 for creating the game.

## Example
Run main.py

Starting numbers (Use ' ' as a delimiter): 9 2 8 100 6 10  
Goal: 923  
(8 + (9 * (100 + (10 / 6))))  
((10 / 2) - (9 * ((6 - 100) - 8)))  
((100 * (10 - (6 / 8))) - 2)  

Normaly takes ~10s to search through all solutions.
