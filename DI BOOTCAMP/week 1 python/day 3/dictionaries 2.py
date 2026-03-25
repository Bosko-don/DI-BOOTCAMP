# ============================================================
# PYTHON CHALLENGES
# Topics: Dictionaries, Loops, Conditionals, String Manipulation
# ============================================================

print("=" * 60)
print("🎯 CHALLENGE 1: Letter Index Dictionary")
print("=" * 60)

# Get user input
word = input("Enter a word: ")

# Create dictionary with letter indices
letter_indices = {}

for index, char in enumerate(word):
    if char in letter_indices:
        letter_indices[char].append(index)
    else:
        letter_indices[char] = [index]

print(f"\nWord: '{word}'")
print(f"Letter indices: {letter_indices}")


print("\n" + "=" * 60)
print("🎯 CHALLENGE 2: Affordable Items")
print("=" * 60)

def clean_price(price_str):
    """Remove $ and commas from price string, return as int"""
    return int(price_str.replace("$", "").replace(",", ""))

def affordable_items(items_purchase, wallet):
    """Determine which items can be purchased with given wallet amount"""
    # Clean wallet amount
    available_money = clean_price(wallet)
    
    basket = []
    
    # Iterate through items (maintaining dictionary order for priority)
    for item, price_str in items_purchase.items():
        price = clean_price(price_str)
        
        # Check if we can afford this item
        if price <= available_money:
            basket.append(item)
            available_money -= price  # Update wallet
    
    # Return result
    if len(basket) == 0:
        return "Nothing"
    else:
        return sorted(basket)  # Return in alphabetical order

# Example 1
print("\n--- Example 1 ---")
items_purchase1 = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet1 = "$300"
result1 = affordable_items(items_purchase1, wallet1)
print(f"Items: {items_purchase1}")
print(f"Wallet: {wallet1}")
print(f"Can buy: {result1}")

# Example 2
print("\n--- Example 2 ---")
items_purchase2 = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet2 = "$100"
result2 = affordable_items(items_purchase2, wallet2)
print(f"Items: {items_purchase2}")
print(f"Wallet: {wallet2}")
print(f"Can buy: {result2}")

# Example 3
print("\n--- Example 3 ---")
items_purchase3 = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet3 = "$1"
result3 = affordable_items(items_purchase3, wallet3)
print(f"Items: {items_purchase3}")
print(f"Wallet: {wallet3}")
print(f"Can buy: {result3}")

# Interactive version
print("\n--- Interactive Version ---")
try:
    user_wallet = input("Enter your wallet amount (e.g., $100): ")
    
    # Create items dictionary from user input or use default
    user_items = {}
    print("Enter items (type 'done' when finished):")
    while True:
        item_name = input("Item name (or 'done'): ").strip()
        if item_name.lower() == 'done':
            break
        item_price = input(f"Price for {item_name} (e.g., $10): ").strip()
        user_items[item_name] = item_price
    
    if user_items:
        user_result = affordable_items(user_items, user_wallet)
        print(f"\nYou can buy: {user_result}")
    else:
        print("No items entered.")
        
except Exception as e:
    print(f"Error: {e}")


print("\n" + "=" * 60)
print("ALL CHALLENGES COMPLETED! 🎉")
print("=" * 60)