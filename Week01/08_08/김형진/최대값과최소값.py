def solution(s):
    answer = []
    s_int = list(map(int, s.split()))
    
    return f"{min(s_int)} {max(s_int)}"