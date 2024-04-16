def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[i if j == 0 else j if i ==
           0 else 0 for j in range(n+1)] for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp


def print_matrix(matrix):
    # Print top header row
    top_header = " " * 4 + \
        "  ".join(f"{i:2}" for i in range(len(matrix[0]))) + "  "
    print(top_header)
    print("   " + "---" * len(matrix[0]))

    # Print matrix rows with row header
    for i, row in enumerate(matrix):
        # Prepare the row header
        row_header = f"{i:<2} |"
        # Prepare the matrix row, ensuring each cell is 3 characters wide
        row_str = " : ".join(f"{cell:2}" for cell in row) + " :"
        print(f"{row_header} {row_str}")


def print_alignment(s1, s2, dp):
    alignment1, alignment2 = "", ""
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            alignment1 = s1[i-1] + alignment1
            alignment2 = s2[j-1] + alignment2
            i, j = i-1, j-1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            alignment1 = s1[i-1] + alignment1
            alignment2 = s2[j-1] + alignment2
            i, j = i-1, j-1
        elif dp[i][j] == dp[i-1][j] + 1:
            alignment1 = s1[i-1] + alignment1
            alignment2 = "-" + alignment2
            i -= 1
        else:
            alignment1 = "-" + alignment1
            alignment2 = s2[j-1] + alignment2
            j -= 1
    while i > 0:
        alignment1 = s1[i-1] + alignment1
        alignment2 = "-" + alignment2
        i -= 1
    while j > 0:
        alignment1 = "-" + alignment1
        alignment2 = s2[j-1] + alignment2
        j -= 1
    print(f"Alignment 1: {alignment1}")
    print(f"Alignment 2: {alignment2}")


if __name__ == "__main__":
    s1 = input("Enter the first word: ")
    s2 = input("Enter the second word: ")

    dp = edit_distance(s1, s2)
    print("\nDistance Matrix:")
    print_matrix(dp)
    print(f"\nEdit distance: {dp[-1][-1]}\n")
    print("\nAlignment:\n")
    print_alignment(s1, s2, dp)
