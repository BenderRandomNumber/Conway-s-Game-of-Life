# Conway's-Game-of-Life
Conway's Game of Life is a celuar cellular automaton devised by the mathemitician John Horton Conway in 1970.

The Game is a Non-player game, with a set of rules dictating how the game plays out based on the inicial board. To start the game one must create an intial board then after that the board will evolve based of the rules.

The inicial starting board is a 2d grid of squares. Each square is either dead or alive, the normal way to defrencrate a square(cell) is to color alive cells black and dead cells white.

The board evolves by going through each cell determining if it will be dead or alive the next generation based of three rules.

"Well what are these sacret rules you speak of" I hear you beg, well, first you need to understand one concept. When I refer to neighbor cells I mean all the cells bordering even if they are touching by corners. An example of this is bellow(# - neihboring cells of the 0 cell).

###
#0#
###

Rule Uno:
If a cell is alive and has less than two alive neighbors, the cell will die of under population.

Rule Dos:
If a cell has more than three alive neighbors, again the cell will die of overpopulation.

Rule Tres:
If cell is dead and has three alive neighbors, The cell will come alive!

Thus, these rules create the wonderfull patterns I behold to you in my code and bellow in the link.

https://www.youtube.com/watch?v=OEbCsKJKXaE
