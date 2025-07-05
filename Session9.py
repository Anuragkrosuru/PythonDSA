class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) >= 20:
            print("Invalid Catchphrase")
            return
        
       
        for word in new_catchphrase.split():
            if not word.isalpha():
                print("Invalid Catchphrase")
                return
                
        self.catchphrase = new_catchphrase
        print("Catchphrase Updated!")
            
    def add_item(self, item_name):
        list1 = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]

        if item_name in list1:
            self.furniture.append(item_name)
    
    def print_inventory(self):
        # Implement the method here
        freq = {}

        if not self.furniture:
            print("inventory empty")
            return

        for item in self.furniture:
            
                
            if item not in freq:
                
                freq[item] = 1
            elif item in freq:
                freq[item] += 1
        
        print(freq)

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yip")


print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 
print(bones.greet_player("Bob"))

bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("codepath course portal")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)



alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)


alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
