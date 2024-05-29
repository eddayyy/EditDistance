<div align="center">
    <img width=35% src="./data/media/MatrixLogo.png">
    <h1>Edit Distance Calculator 🔠</h1>
    <img alt="Python Version" src="https://img.shields.io/badge/Python-v3.12%2B-blue">
    <a href="https://opensource.org/licenses/MIT">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg">
    </a>
</div>

## Table of Contents
1. [Overview](#-overview)
2. [Features and Demo](#features-and-demo)
3. [Example Output](#example-output)
4. [License](#-license)

## 🌟 Overview

**Edit Distance Calculator** is a Python application that calculates the edit distance between two input words using a dynamic programming approach. It provides a detailed matrix of distance calculations and a visual alignment of the words, demonstrating the result in a clear and interactive manner.

Developed by Eduardo Nunez and Miguel Mancera, this tool is designed for educational purposes, showcasing how edit distances are computed which can be particularly useful in fields such as computational linguistics and bioinformatics.

## **Features and Demo**

- **Dynamic Matrix Display**: Displays the step-by-step computation of the edit distance between two words.
- **Word Alignment Visualization**: Shows how the words compare by displaying the alignment visually with insertions, deletions, and substitutions highlighted.

## **Example Output**

Here is an example of how the output may look after you run the program:
```
Enter the first word: evaluation
Enter the second ...

Distance Matrix:

    0   1   2   3   4   5   6   7
0 | 0 : 1 : 2 : 3 : 4 : 5 : 6 : 7 :
1 | 1 : 0 : 1 : 2 : 3 : 4 : 5 : 6 :
2 | 2 : 1 : 1 : 2 : 3 : 4 : 5 : 6 :
3 | 3 : 2 : 2 : 2 : 3 : 4 : 5 : 6 :
4 | 4 : 3 : 2 : 3 : 3 : 4 : 5 : 6 :
5 | 5 : 4 : 3 : 2 : 3 : 4 : 5 : 6 :
6 | 6 : 5 : 4 : 3 : 3 : 4 : 5 : 6 :
7 | 7 : 6 : 5 : 4 : 3 : 4 : 5 : 6 :
8 | 8 : 7 : 6 : 5 : 4 : 3 : 4 : 5 :
9 | 9 : 8 : 7 : 6 : 5 : 4 : 3 : 4 :
10 | 10 : 9 : 8 : 7 : 6 : 5 : 4 : 3 :

Edit distance: 3

Alignment:

Alignment 1: evaluation
Alignment 2: e--lu-tion
```


## 📄 License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.
