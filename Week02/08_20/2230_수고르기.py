n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

left = 0
right = 0
ans = float('inf')

while left < n and right < n:
    diff = numbers[right] - numbers[left]
    if diff >= m:
        ans = min(ans, diff)
        left += 1
    else:
        right += 1
    if left > right:          # 항상 right가 left 이상이 되도록 유지
        right = left

print(ans)