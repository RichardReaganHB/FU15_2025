import random

rng1 = random.randint(1, 6)
rng2 = random.randint(1, 6)

total = rng1 + rng2
name = input("What is your name?\n")
print(f"Hello, {name}!")


print("Rolling dice...")
print(f"Die 1: {rng1}")
print(f"Die 2: {rng2}")
print(f"Total value: {total}")

if total > 7:
    print(f"{name} won.")
else: print(f"{name} lost.")