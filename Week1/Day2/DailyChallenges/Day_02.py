# Challenge 1: Letter index dictionary
# Challenge 1: build a dictionary that stores the positions of each letter
# in a word entered by the user.

print("=" * 70)
print("CHALLENGE 1: Letter index dictionary")
print("=" * 70)

word = input("Enter a word: ")
letter_index = {}

for i, ch in enumerate(word):
    if ch in letter_index:
        letter_index[ch].append(i)
    else:
        letter_index[ch] = [i]

print(f"Result: {letter_index}")
print()


# Challenge 2: Affordable items selection
# Challenge 2: given item prices and a wallet amount, pick items in order
# while you can afford them; return sorted list or "Nothing".

print("=" * 70)
print("CHALLENGE 2: Affordable items selection")
print("=" * 70)

def affordable_items(items_purchase, wallet):
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))
    basket = []
    for item, price_str in items_purchase.items():
        price = int(price_str.replace("$", "").replace(",", ""))
        if price <= wallet_amount:
            basket.append(item)
            wallet_amount -= price
    return "Nothing" if not basket else sorted(basket)

examples = [
    ({"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}, "$300"),
    ({"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}, "$100"),
    ({"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}, "$1"),
]

for idx, (items, wallet) in enumerate(examples, 1):
    result = affordable_items(items, wallet)
    print(f"Example {idx} -> {result}")
