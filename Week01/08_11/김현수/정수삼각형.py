def solution(triangle):
    answer = 0
    row_size = len(triangle)
    dp = [[0] * (row_size + 1) for _ in range(row_size)]
    dp[0][1] = triangle[0][0]

    for i in range(1, row_size):
        for j in range(1, len(triangle[i]) + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j - 1]
            
    return max(dp[row_size - 1])