lost_fight_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet_broken = lost_fight_count // 2
total_sword_broken = lost_fight_count // 3
total_shield_broken = lost_fight_count // (2 * 3)
total_armor_broken = total_shield_broken // 2

expenses = total_helmet_broken * helmet_price \
           + total_sword_broken * sword_price \
           + total_shield_broken * shield_price \
           + total_armor_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")