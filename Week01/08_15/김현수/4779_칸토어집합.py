
def recur(n, ch, m):
    if (n < 1):
        print(ch * m, end='')
        return
    
    recur(n - 1, ch, m // 3)
    print(' ' * (m//3), end='')
    recur(n - 1, ch, m // 3)

try:
    while True:
        n = int(input())
        recur(n, '-', 3**n)
        print()

except EOFError:
    pass  