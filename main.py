def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    # Create a matrix to store distances
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Initialize the matrix
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
        
    # Fill dp
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
    return dp

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
        
def print_alignment(s1, s2, dp):
    alignment1 = ""
    alignment2 = ""
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
    print("Alignment 1: " + alignment1)
    print("Alignment 2: " + alignment2)

if __name__ == "__main__":
    s1 = input("Enter the first word: ")
    s2 = input("Enter the second word: ")
    
    dp = edit_distance(s1, s2)
    print("Edit distance: ", dp[-1][-1])
    print("Distance Matrix:")
    print_matrix(dp)
    print("Alignment:")
    print_alignment(s1, s2, dp)
