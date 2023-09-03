class SetItem :
    def get_name(self):
        pass
    def get_price(self):
        pass
    def get_category(self):
        pass


class Ingredients :
    def get_ingredients(self):
        pass
#i created two classes menuitem and menumanage for single responsibility for each one 

#initialize all interfaces
class MenuItem (SetItem,Ingredients):
    def __init__ (self,name,price,category,ingredients):
        self.name=name
        self.price=price
        self.category=category
        self.ingredients=ingredients
        
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_category(self):
        return self.category
    def get_ingredients(self):
        return self.ingredients    
# manage menuitem class to achieve open close Principle
class MenuManage :
    def __init__(self):
        self.menu_item=[]
    def add_item(self,item) :
        self.menu_item.append(item)
    def remove_item(self,item) :
        self.menu_item.remove(item)
    def get_item(self) :
        return self.menu_item

def main():
    menu_manager = MenuManage()

    item1 = MenuItem("ziger", 22, "sandwish", ["chicken strips", "hot souce", "ketchup"])
    item2 = MenuItem("chicken ranch", 40, "pizza", ["chicken pices", "ranch souce", "zaton"])
    item3 = MenuItem("pepperoni", 50, "pizza", ["pepperoni", "tomato souce", "zaton"])

    menu_manager.add_item(item1)
    menu_manager.add_item(item2)
    menu_manager.add_item(item3)
    menu_manager.remove_item(item3)

    for item in menu_manager.get_item():
        
        if isinstance(item, SetItem):
            print(f"Item: {item.get_name()}, Price: ${item.get_price()}, Category: {item.get_category()}")

        if isinstance(item, Ingredients):
            print(f"Ingredients: {item.get_ingredients()}")

if __name__ == "__main__":
    main()        
