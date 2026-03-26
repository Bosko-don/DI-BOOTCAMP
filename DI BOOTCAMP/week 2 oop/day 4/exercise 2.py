import json
import requests


# ============================================
# EXERCISE 1: RESTAURANT MENU MANAGER
# ============================================

class MenuManager:
    def __init__(self):
        with open('restaurant_menu.json', 'r') as file:
            self.menu = json.load(file)
    
    def add_item(self, name, price):
        new_item = {"name": name, "price": price}
        self.menu["items"].append(new_item)
    
    def remove_item(self, name):
        for i, item in enumerate(self.menu["items"]):
            if item["name"] == name:
                del self.menu["items"][i]
                return True
        return False
    
    def save_to_file(self):
        with open('restaurant_menu.json', 'w') as file:
            json.dump(self.menu, file, indent=4)


def load_manager():
    return MenuManager()


def show_user_menu():
    print("\n=== RESTAURANT MENU MANAGER ===")
    print("1. View Menu")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")


def add_item_to_menu(manager):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    manager.add_item(name, price)
    print(f"{name} was added successfully!")


def remove_item_from_menu(manager):
    name = input("Enter item name to remove: ")
    if manager.remove_item(name):
        print(f"{name} was deleted successfully!")
    else:
        print("Error: Item not found in menu.")


def show_restaurant_menu(manager):
    print("\n--- CURRENT MENU ---")
    for item in manager.menu["items"]:
        print(f"{item['name']}: ${item['price']}")


def run_menu_manager():
    manager = load_manager()
    
    while True:
        show_user_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            show_restaurant_menu(manager)
        elif choice == '2':
            add_item_to_menu(manager)
        elif choice == '3':
            remove_item_from_menu(manager)
        elif choice == '4':
            manager.save_to_file()
            print("Menu saved successfully! Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


# ============================================
# EXERCISE 2 & 3: GIPHY API
# ============================================

API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"


def get_gifs(search_term, limit=10):
    """Fetch gifs from Giphy API"""
    url = f"https://api.giphy.com/v1/gifs/search?q={search_term}&rating=g&api_key={API_KEY}&limit={limit}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        gifs = data['data']
        
        # Filter gifs with height > 100
        filtered_gifs = [gif for gif in gifs if gif['images']['original']['height'] > '100']
        
        print(f"\nFound {len(filtered_gifs)} gifs for '{search_term}'")
        
        # Display first 10 gifs
        for i, gif in enumerate(filtered_gifs[:10], 1):
            print(f"{i}. {gif['title']} - {gif['url']}")
        
        return filtered_gifs
    else:
        return None


def get_trending_gifs(limit=10):
    """Fetch trending gifs as fallback"""
    url = f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit={limit}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        gifs = data['data']
        
        print(f"\n--- TRENDING GIFS ---")
        for i, gif in enumerate(gifs[:10], 1):
            print(f"{i}. {gif['title']} - {gif['url']}")
        
        return gifs
    return []


def run_giphy_search():
    print("\n=== GIPHY SEARCH ===")
    search_term = input("Enter a search term (or press Enter to skip): ").strip()
    
    if search_term:
        result = get_gifs(search_term)
        if result is None or len(result) == 0:
            print(f"\nCouldn't find '{search_term}'. Showing trending gifs instead.")
            get_trending_gifs()
    else:
        get_trending_gifs()


# ============================================
# MAIN PROGRAM - RUN BOTH EXERCISES
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("PYTHON EXERCISES: MENU MANAGER & GIPHY API")
    print("=" * 50)
    
    # Run Exercise 1: Menu Manager
    print("\n[EXERCISE 1: RESTAURANT MENU MANAGER]")
    try:
        run_menu_manager()
    except FileNotFoundError:
        # Create sample menu file if not exists
        sample_menu = {
            "items": [
                {"name": "Vegetable soup", "price": 30},
                {"name": "Hamburger", "price": 44.9},
                {"name": "Milkshake", "price": 22.5},
                {"name": "Artichoke", "price": 18},
                {"name": "Beef stew", "price": 52.5}
            ]
        }
        with open('restaurant_menu.json', 'w') as f:
            json.dump(sample_menu, f, indent=4)
        print("Created restaurant_menu.json. Running menu manager...")
        run_menu_manager()
    
    # Run Exercise 2 & 3: Giphy API
    print("\n" + "=" * 50)
    print("[EXERCISE 2 & 3: GIPHY API]")
    run_giphy_search()
    
    print("\n" + "=" * 50)
    print("ALL EXERCISES COMPLETED!")
    print("=" * 50)