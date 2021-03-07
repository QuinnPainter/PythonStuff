# PythonStuff
Random python projects
## AsciiSweeper
A version of Minesweeper, to be played in the command line.
### Usage
First arg is size, second is difficulty (number of mines)  
Third argument is to present with colour and numbers, True or False  
Example - `python asciisweeper.py 5 5 True`  

Once in game, the controls are:  
Type 'help' for help.  
Type coordinates, in format 'x, y', to dig a tile.  
example: 5, 7  
Type 'flag' before coordinates to flag those coordinates.  
example: flag 5, 6  
