from sys import stdin

N, P = map(int, stdin.readline().split())
stack = [[0] for _ in range(7)] #1번 ~6번 줄 만큼 스택 만들기
cnt = 0

for _ in range(N):
    l, p = map(int, stdin.readline().split())
    # 프렛번호보다 큰 값을 다 pop
    while stack[l][-1] > p:
        stack[l].pop()
        cnt += 1

    if stack[l][-1] < p:
        stack[l].append(p)
        cnt += 1
print(cnt)

