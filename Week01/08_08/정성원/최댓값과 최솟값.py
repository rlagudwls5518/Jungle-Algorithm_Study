def solution(s):
    lst = list(map(int, s.split()))
    rst = []
    rst.append(max(lst))
    rst.append(min(lst))
    answer = f"{rst[1]} {rst[0]}"
    return answer