def solution(s):
    answer = True
    stack = []
    # '(' 그냥 넣으면된다.
    # ')' top = '(' 이면 pop 아니면 False
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True