#Task:
# 38) (1sd) Comparison between A* and Uniform Cost search for the labyrinth problem on the same labyrinth of size 20 by 20, then 30 by 30. 
# Generate random labyrinths with 5, 10, 20, 25, 30 percents of the space as "walls". You should count the number cells visited.
# There will be a number of labyrinths which have no solution. The output should be written in a text file as CSV values. 
# e.g. "AStar; 20; 20; 253.35; 17"  meaning: for A* on 20 by 20 averaged number of moves measured on 50 labyrinths is 253.35 ans 17 unsolvable problems
import labGen
import output
    
def main():
    print("test ■")
    output.printLabyrinth(labGen.generateLabyrinth(20, 40))
main()