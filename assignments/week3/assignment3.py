import random

while True:
    try:
        num_fireworks = int(input("How many fireworks? (1-10):"))
        if 1 <= num_fireworks <= 10:
            break
        else:
            print("Please enter a number between 1 and 10")
    except ValueError:
        print ("That's not a valid number.")

while True:
    try:
        height = int(input("How tall should each firework be? (3-10): "))
        if 3 <= height <= 10:
            break
        else:
            print("Please enter a number between 3 and 10")
    except ValueError:
        print("That's not a valid number.")


while True:
    symbol = input("Choose a symbol for the explosion (like *, @, #): ")
    if len(symbol) == 1:
        break
    else:
        print("Please enter just one character")



explosions = [
    [
        f"  {symbol}  ",
        f" {symbol*3} ",
        f"{symbol*5}",
        f" {symbol*3} ",
        f"  {symbol}  "
    ],
    [
        f"   {symbol}   ",
        f"  {symbol} {symbol}  ",
        f" {symbol}   {symbol} ",
        f"  {symbol} {symbol}  ",
        f"   {symbol}   "
    ],
    [
        f"   {symbol*3}   ",
        f"  {symbol} {symbol} {symbol}  ",
        f" {symbol}  {symbol}  {symbol} ",
        f"  {symbol} {symbol} {symbol}  ",
        f"   {symbol*3}   "
    ]
]


for i in range(num_fireworks):
    print(f"\nFirework #{i+1}:")

    shift = random.randint(0, 20)

    for j in range(height):
        print(" " *shift + " | ")

    if i % 2 == 0:
        explosion = random.choice(explosions)
    else:
        explosion = random.choice(explosions)[::-1]

    for line in explosion:
        print(" " * shift + line)