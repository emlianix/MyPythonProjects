rgb = map(int, input().split())
opp_color = map(lambda x: abs(x - 255), rgb)
print(*opp_color)