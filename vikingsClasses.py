import random

# Soldier


class Soldier: #base class for all soldiers
    def __init__(self, health, strength): #initializes a Soldier with health and strength attributes
        self.health = health
        self.strength = strength
    
    def attack(self): #returns the strength of the Soldier
        return self.strength

    def receiveDamage(self, damage): #reduce the health of the Soldier by the damage received
        self.health -= damage
    

# Viking

class Viking(Soldier): #viking class that extends Soldier
    def __init__(self, name, health, strength):  #Initializes a Viking, inheriting health and strength from Soldier, and adding a name attribute.
        super().__init__(health, strength)  # # Inherit health and strength from Soldier
        self.name = name  # Assigns the name to the Viking

    def battleCry(self): #Returns the Viking's battle cry
        return "Odin Owns You All!"

    def receiveDamage(self, damage): #Reduces the Viking's health by the amount of damage received. Returns a custom message based on whether the Viking survives or dies.
        self.health -= damage  # Reduce health

        # If the Viking is still alive, return a custom message
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:  # If the Viking dies, return a different message
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier): #Saxon class that inherits from Soldier
    def __init__(self, health, strength): #Initializes a Saxon, inheriting health and strength from Soldier.
        super().__init__(health, strength)  # Inherit health and strength from Soldier

    def receiveDamage(self, damage):  #Reduces the Saxon's health by the amount of damage received.
        self.health -= damage # Reduce health

        # If the Saxon is still alive, return a custom message
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:  # If the Saxon dies, return a different message
            return f"A Saxon has died in combat"

# WAAAAAAAAAGH

class War():
    def __init__(self):  #Initializes a War with two empty armies: vikingArmy and saxonArmy
        self.vikingArmy = []  # List to store Vikings
        self.saxonArmy = []   # List to store Saxons

    def addViking(self, viking):
        self.vikingArmy.append(viking)  # Add a Viking object to the vikingArmy
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)  # Add a Saxon object to the saxonArmy
    
    def vikingAttack(self):  #A Viking attacks a Saxon
        if not self.saxonArmy:
            return "No Saxons left!"

        viking = random.choice(self.vikingArmy) # A random Viking attacks a random Saxon.
        saxon = random.choice(self.saxonArmy)
        result = saxon.receiveDamage(viking.attack()) #The Saxon receives damage equal to the Viking's strength. The result of calling the receiveDamage() method is stored in a variable.

        if saxon.health <= 0: #If the Saxon dies, it is removed from the army.
            self.saxonArmy.remove(saxon)  # Remove dead Saxon

        return result #Returns the result of the attack.
    
    def saxonAttack(self): #A Saxon attacks a Viking
        if not self.vikingArmy:
            return "No Vikings left!"
        
        saxon = random.choice(self.saxonArmy) # A random Saxon attacks a random Viking.
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.attack()) #the Viking receives damage equal to the Saxon's strength. The result of calling the receiveDamage() method is stored in a variable.

        if viking.health <= 0: #If the Viking dies, it is removed from the army.
            self.vikingArmy.remove(viking)  # Remove dead Viking

        return result #Returns the result of the attack.


    def showStatus(self): #Returns the current status of the war
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


