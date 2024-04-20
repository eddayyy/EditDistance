# Edit Distance Calculator

This program calculates the edit distance between two input words and displays both the matrix of distance calculations and a visual alignment of the words to demonstrate the result.

The program was written by **Eduardo Nunez and Miguel Mancera**

## Running the Program

### Requirements

- Python 3.12 or higher

### Steps

1. **Open the Command Line**:

   - Navigate to the working directory where the file `main.py` is located.

2. **Execute the Program**:

   - Run the command:
     ```
     python main.py
     ```
   - This command executes the program in the terminal.

3. **Provide Input**:

   - The program will prompt you for input. Type your word and press `Enter`.
   - After entering the first word, wait for the next prompt and repeat the process for the second word.

4. **Processing**:
   - Once both words are entered, the program will begin the calculations automatically.

## Objective

The program is designed to calculate the edit distance between two words using a dynamic programming approach. It outputs both the distance calculation matrix and a visual alignment of the words.

## Features

- **Dynamic Matrix Display**: Shows how the edit distance is calculated step-by-step.
- **Word Alignment**: Visualizes how the words compare by showing optimal alignments with insertions, deletions, and substitutions highlighted.

## Submission Instructions

### Requirements

- **Input**: The program should ask for the input of two words.
- **Calculation**: Calculate the edit distance between the provided words.
- **Output**: Display the matrix of calculation and an alignment that verifies the edit distance.

### Additional Information

- **Language**: Any programming language compatible with Python 3.12 can be used.
- **Comments**: Include a paragraph of comments at the beginning of your submission describing how to compile and test your program, including the required tools/environment. Note: MATLAB is not acceptable, as it is not available on my computer.

## Example

Here is an example of how the output may look after you run the program:

```
Enter the first word: evaluation
Enter the second word: elution

Distance Matrix:

     0   1   2   3   4   5   6   7
   ------------------------
0  |  0 :  1 :  2 :  3 :  4 :  5 :  6 :  7 :
1  |  1 :  0 :  1 :  2 :  3 :  4 :  5 :  6 :
2  |  2 :  1 :  1 :  2 :  3 :  4 :  5 :  6 :
3  |  3 :  2 :  2 :  2 :  3 :  4 :  5 :  6 :
4  |  4 :  3 :  2 :  3 :  3 :  4 :  5 :  6 :
5  |  5 :  4 :  3 :  2 :  3 :  4 :  5 :  6 :
6  |  6 :  5 :  4 :  3 :  3 :  4 :  5 :  6 :
7  |  7 :  6 :  5 :  4 :  3 :  4 :  5 :  6 :
8  |  8 :  7 :  6 :  5 :  4 :  3 :  4 :  5 :
9  |  9 :  8 :  7 :  6 :  5 :  4 :  3 :  4 :
10 | 10 :  9 :  8 :  7 :  6 :  5 :  4 :  3 :

Edit distance: 3

Alignment:

Alignment 1: evaluation
Alignment 2: e--lu-tion
```
