#Task:
# 38) (1sd) Comparison between A* and Uniform Cost search for the labyrinth problem on the same labyrinth of size 20 by 20, then 30 by 30. 
# Generate random labyrinths with 5, 10, 20, 25, 30 percents of the space as "walls". You should count the number cells visited.
# There will be a number of labyrinths which have no solution. The output should be written in a text file as CSV values. 
# e.g. "AStar; 20; 20; 253.35; 17"  meaning: for A* on 20 by 20 averaged number of moves measured on 50 labyrinths is 253.35 ans 17 unsolvable problems

import labGen
import searchAlg
import output
import numpy as np

def run_experiment(size, percentages, num_trials=50):
    results = []
    for percentage in percentages:
        a_star_counts = []
        ucs_counts = []
        unsolvable = 0
        
        for _ in range(num_trials):
            labyrinth = labGen.generateLabyrinth(size, percentage)
            
            _, a_star_visited = searchAlg.aStar(labyrinth.copy())
            _, ucs_visited = searchAlg.uniformCost(labyrinth.copy())
            
            if _ is None:
                unsolvable += 1
                continue
                
            a_star_counts.append(a_star_visited)
            ucs_counts.append(ucs_visited)
        
        if a_star_counts:
            avg_a_star = np.mean(a_star_counts)
            avg_ucs = np.mean(ucs_counts)
            results.append(f"AStar; {size}; {percentage}; {avg_a_star:.2f}; {unsolvable}")
            results.append(f"UCS; {size}; {percentage}; {avg_ucs:.2f}; {unsolvable}")
    
    return results

def main():
    sizes = [20, 30]
    percentages = [5, 10, 20, 25, 30]
    output.clearOutput()
    
    for size in sizes:
        results = run_experiment(size, percentages)
        for result in results:
            output.addOutput(result)
    
    output.writeOutput("\n".join(output.readOutput()))

if __name__ == "__main__":
    main()