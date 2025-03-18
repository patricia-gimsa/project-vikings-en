import random

# Soldier
class Soldier:  # Base class for all soldiers
    def __init__(self, health, strength):  # Initializes a Soldier with health and strength attributes
        self.health = health
        self.strength = strength

    def attack(self):  # Returns the strength of the Soldier
        return self.strength

    def receiveDamage(self, damage):  # Reduces the Soldier's health by the damage received
        self.health -= damage


# Viking
class Viking(Soldier):  # Viking class that extends Soldier
    def __init__(self, name, health, strength):  # Initializes a Viking, inheriting health and strength from Soldier, and adding a name attribute
        super().__init__(health, strength)  # Inherit health and strength from Soldier
        self.name = name  # Assigns the name to the Viking

    def battleCry(self):  # Returns the Viking's battle cry
        return "Odin Owns You All!"

    def receiveDamage(self, damage):  # Reduces the Viking's health by the amount of damage received
        self.health -= damage  # Reduce health

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon
class Saxon(Soldier):  # Saxon class that inherits from Soldier
    def __init__(self, health, strength):  # Initializes a Saxon, inheriting health and strength from Soldier
        super().__init__(health, strength)

    def receiveDamage(self, damage):  # Reduces the Saxon's health by the amount of damage received
        self.health -= damage  # Reduce health

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# ⚔️ War
class War():
    def __init__(self):  # Initializes a War with two empty armies: vikingArmy and saxonArmy
        self.vikingArmy = []  # List to store Vikings
        self.saxonArmy = []   # List to store Saxons
        self.vikingPoints = 0  # Points scored by Vikings
        self.saxonPoints = 0   # Points scored by Saxons

    def addViking(self, viking):  # Adds a Viking to the vikingArmy
        self.vikingArmy.append(viking)  

    def addSaxon(self, saxon):  # Adds a Saxon to the saxonArmy
        self.saxonArmy.append(saxon)  

    def vikingAttack(self):  # A Viking attacks a Saxon
        if not self.saxonArmy:  # Stop attack if no Saxons remain
            return "⚠️ No Saxons left to attack!"
        
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        attack_message = f"⚔️ {viking.name} strikes a Saxon for {viking.attack()} damage!"
        result = saxon.receiveDamage(viking.attack())

        if saxon.health <= 0:  # If the Saxon dies, remove from army and add points
            self.saxonArmy.remove(saxon)
            self.vikingPoints += 1
            attack_message += " 💀 A Saxon falls in battle!"

        return f"{attack_message}\n{result}"

    def saxonAttack(self):  # A Saxon attacks a Viking
        if not self.vikingArmy:  # Stop attack if no Vikings remain
            return "⚠️ No Vikings left to attack!"
        
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        attack_message = f"🛡️ A Saxon swings at {viking.name} for {saxon.attack()} damage!"
        result = viking.receiveDamage(saxon.attack())

        if viking.health <= 0:  # If the Viking dies, remove from army and add points
            self.vikingArmy.remove(viking)
            self.saxonPoints += 1
            attack_message += f" 💀 {viking.name} has fallen!"

        return f"{attack_message}\n{result}"  

    def showPoints(self):  # Returns the current score of the battle
        return f"🏆 Vikings: {self.vikingPoints} points | Saxons: {self.saxonPoints} points"  

    def showStatus(self):  # Returns the current status of the battle
        if not self.saxonArmy:
            return "⚔️ Vikings have won the battle!"
        elif not self.vikingArmy:
            return "⚔️ Saxons have fought bravely and survived!"
        else:
            return "⚔️ The battle rages on!"
