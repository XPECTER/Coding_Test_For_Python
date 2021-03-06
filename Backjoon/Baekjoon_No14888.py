import sys

input = sys.stdin.readline
n = int(input())
lst = list(input().rstrip().split())
operators = list(map(int, input().split()))

mx, mn = -1e9, 1e9

def dfs(expression, cnt, operators):
    global mx, mn

    expression += lst[cnt]
    val = int(eval(expression))

    if cnt == len(lst) - 1:
        mx = max(mx, val)
        mn = min(mn, val)
        print(f'expression : {expression}, value = {val}')
        return

    for idx in range(len(operators)):
        if operators[idx] > 0:
            operators[idx] -= 1

            if idx == 0:
                dfs(str(val) + '+', cnt+1, operators)
            elif idx == 1:
                dfs(str(val) + '-', cnt+1, operators)
            elif idx == 2:
                dfs(str(val) + '*', cnt+1, operators)
            else:
                dfs(str(val) + '/', cnt+1, operators)

            operators[idx] += 1
    return

dfs('', 0, operators)

print(f'{mx}\n{mn}')


def f(s, idx, plus, minus, mul, div):
    global minV, maxV
    if idx >= N:
        minV = s if s < minV else minV
        maxV = s if s > maxV else maxV
    else:
        if plus: f(s+M[idx], idx+1, plus-1, minus, mul, div)
        if minus: f(s-M[idx], idx+1, plus, minus-1, mul, div)
        if mul: f(s*M[idx], idx+1, plus, minus, mul-1, div)
        if div: f(int(s/M[idx]), idx+1, plus, minus, mul, div-1)

N = int(input())
M = list(map(int, input().split()))
C = list(map(int, input().split()))
minV = 987654321
maxV = -987654321

f(M[0], 1, C[0], C[1], C[2], C[3])

print(maxV)
print(minV)
