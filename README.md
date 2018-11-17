## Overview  
The bfs_maze_solution application uses a Breadth First Search (BFS) algorithm  
to find a path from a given starting point to an end point in a maze.  

## Problem solution approach  
File is provided containing a start point, an end point and  
a maze. The maze is converted into a graph stored as a dict. Each point,  
represented as a tuple of (x, y) and of value a list of all child nodes.  
A BFS algorithm will expand nodes in layers in an attempt to reach the end  
point. This means that once a new node is discovered it will be checked  
if it is the desired node and if not all child nodes will be added in a que  
to be checked in latter iterations. Although this means that in the worst  
case the algorithm will check all nodes, the path to the end point will alwats  
be the shortest one.  

## Requirements
- Python 3.6 or latter installed

## Assumptions  
* File must be of type *.txt. 
* File must not contain any blank lines.  
* Maze is contained within a peripheral wall.
* Start and end points can be anywhere within this peripheral wall.

#### File Template  

```buildoutcfg
Maze file format
================

The input is a maze description file in plain text.  
 1 - denotes walls
 0 - traversable passage way

INPUT:
<START_X> <START_Y><CR>		(x,y) location of the start. (0,0) is upper left and (width-1,height-1) is lower right
<END_X> <END_Y><CR>		(x,y) location of the end
<HEIGHT> rows where each row has <WIDTH> {0,1} integers space delimited

Example file:  
1 1
8 8
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 1 0 1 1 1 1 1 1
1 0 1 0 0 0 0 0 0 1
1 0 1 1 0 1 0 1 1 1
1 0 1 0 0 1 0 1 0 1
1 0 1 0 0 0 0 0 0 1
1 0 1 1 1 0 1 1 1 1
1 0 1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
``` 

## Running the application  
Please make sure you run the application with a Python 3.6 or later interpreter.  
Run from terminal:  
```buildoutcfg
python run.py
```  
You will be prompt to type in file path.  
```buildoutcfg
Please enter file path or type exit to exit:
```
In case file is not accessible or not valid user will be asked to retype file path.  
```buildoutcfg
There seems to be a problem with file "{path}"!
```
if you want to close the app type "exit".  

## Output
####Solvable maze  
The output of a solved maze will be printed on console as such  
```buildoutcfg
OUTPUT:
 the maze with a path from start to end
 walls marked by '#', passages marked by ' ', path marked by 'X', start/end marked by 'S'/'E'

OUTPUT:
##########
#SXX     #
# #X######
# #XX    #
# ##X# ###
# # X# # #
# # XX   #
# ###X####
# #  XXXE#
##########
```

####Unsolvable maze  
If no path is found from start point to end a message will be displayed on the console.  
```buildoutcfg
Could not reach end point!
```

## Tests 
Test files can be found in test_files directory.  
Unit tests are provided in the tests directory.  