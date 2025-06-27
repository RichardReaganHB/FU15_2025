import random

rng1 = random.randint(1, 6)
rng2 = random.randint(1, 6)

total = rng1 + rng2

print("Rolling dice...")
print(f"Die 1: {rng1}")
print(f"Die 2: {rng2}")
print(f"Total value: {total}")