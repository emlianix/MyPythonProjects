n = int(input())
correct = set()
total_correct = 0  # все верные попытки, в том числе повторные

for _ in range(n):
    nick, result = input().split(": ")
    if result.strip() == "Correct":
        correct.add(nick)
        total_correct += 1

if not correct:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    percent = int(total_correct / n * 100 + 0.5)
    print(f"Верно решили {len(correct)} учащихся")
    print(f"Из всех попыток {percent}% верных")