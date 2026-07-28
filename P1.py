import random

def run_flip_a_coin(n):
    head_count = 0

    for i in range(n):
        result = random.choice(["Head", "Tail"])

        if result == "Head":
            head_count += 1

    percentage_heads = (head_count / n) * 100

    print(f"After flipping the coin {n} times, the percentage of times head has come is: {percentage_heads:.2f}%")

coin_flip_times = int(input("Enter the number of times to flip the coin: "))
run_flip_a_coin(coin_flip_times)