import random
from vikingsClasses_Improvements import Viking, Saxon, War

# Create the ⚔️ Battle instance
soldier_names = ["Albert", "Andres", "Archie", "Dani", "David", "Gerard", "German", "Graham", "Imanol", "Laura"]
great_war = War()

# Create 5 Vikings
for _ in range(5):
    great_war.addViking(Viking(random.choice(soldier_names), 100, random.randint(50, 100)))

# Create 5 Saxons
for _ in range(5):
    great_war.addSaxon(Saxon(100, random.randint(50, 100)))

# Start battle simulation
round_num = 1
while great_war.showStatus() == "⚔️ The battle rages on!":
    print(f"\n🔥 Round {round_num} 🔥")
    
    if great_war.vikingArmy:  # ✅ Ensure there are Vikings before attacking!
        print(great_war.vikingAttack())  # Display Viking attack message
    
    if great_war.saxonArmy:  # ✅ Ensure there are Saxons before attacking!
        print(great_war.saxonAttack())  # Display Saxon attack message

    print(f"📜 Round {round_num}: Viking army - {len(great_war.vikingArmy)} warriors | Saxon army - {len(great_war.saxonArmy)} warriors")
    print(great_war.showStatus())
    print(great_war.showPoints())  # Show battle points

    round_num += 1

# Final result
print("\n⚔️ The battle has ended! ⚔️")
print(great_war.showStatus())
print(great_war.showPoints())