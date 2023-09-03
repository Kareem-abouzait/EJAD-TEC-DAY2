class SetItem:
    pass

class Ingredients:
    pass

class MenuItem(SetItem, Ingredients):
    def __init__(self, name, price, category, ingredients):
        self.name = name
        self.price = price
        self.category = category
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_category(self):
        return self.category

    def get_ingredients(self):
        return self.ingredients

# Using Singleton pattern for MenuManager
class MenuManagerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MenuManagerSingleton, cls).__new__(cls)
            cls._instance.menu_item = []
        return cls._instance

    def add_item(self, item):
        self.menu_item.append(item)

    def remove_item(self, item):
        self.menu_item.remove(item)

    def get_item(self):
        return self.menu_item

# Creating MenuItem objects using Proxy pattern
class MenuItemProxy:
    def __init__(self, item):
        self._item = item

    def get_name(self):
        return self._item.get_name()

    def get_price(self):
        return self._item.get_price()

    def get_category(self):
        return self._item.get_category()

    def get_ingredients(self):
        return self._item.get_ingredients()

class Observer:
    def update(self, menu_item):
        pass
# Adding an Observer for MenuManagerObservable
class MenuManagerObservable:
    def __init__(self):
        self.menu_item = []
        self.observers = []

    def add_item(self, item):
        self.menu_item.append(item)
        self.notify_observers(item)

    def remove_item(self, item):
        self.menu_item.remove(item)
        self.notify_observers(item)

    def get_item(self):
        return self.menu_item

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, item):
        for observer in self.observers:
            observer.update(item)

class MenuItemObserver(Observer):
    def update(self, menu_item):
        if isinstance(menu_item, SetItem):
            print(f"Item: {menu_item.get_name()}, Price: ${menu_item.get_price()}, Category: {menu_item.get_category()}")
        if isinstance(menu_item, Ingredients):
            print(f"Ingredients: {menu_item.get_ingredients()}")

def main():
    
    menu_manager = MenuManagerSingleton()

    
    item1 = MenuItemProxy(MenuItem("ziger", 22, "sandwich", ["chicken strips", "hot sauce", "ketchup"]))
    item2 = MenuItemProxy(MenuItem("chicken ranch", 40, "pizza", ["chicken pieces", "ranch sauce", "zaton"]))
    item3 = MenuItemProxy(MenuItem("pepperoni", 50, "pizza", ["pepperoni", "tomato sauce", "zaton"]))

    
    observer = MenuItemObserver()
    menu_manager.add_observer(observer)

    menu_manager.add_item(item1)
    menu_manager.add_item(item2)
    menu_manager.remove_item(item2)

if __name__ == "__main__":
    main()
