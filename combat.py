# combat.py - Member B: Combat & Stats Engine
import random


def start_battle(player, monster_type):
  monster_hp = 30 if monster_type == "Goblin" else 100
  monster_atk = 8 if monster_type == "Goblin" else 20
  print(f"\n[Battle Start] A wild {monster_type} appears!")

  while monster_hp > 0 and player["hp"] > 0:
    print(f"\nHero HP: {player['hp']}/{player['max_hp']} | Enemy HP: {monster_hp}")
    act = input("Action: (1) Attack (2) Run: ").strip()

    if act == "1":
      # 玩家攻擊 (計算命中與隨機浮動傷害)
      dmg = player["atk"] + random.randint(-2, 3)
      monster_hp -= dmg
      print(f"You hit {monster_type} for {dmg} damage!")
      if monster_hp <= 0:
        print(f"You defeated the {monster_type}!")
        player["gold"] += 10
        return "WIN"

      # 怪物反擊
      e_dmg = monster_atk + random.randint(-1, 2)
      player["hp"] -= e_dmg
      print(f"{monster_type} dealt {e_dmg} damage to you!")
      if player["hp"] <= 0:
        return "LOSE"
    elif act == "2":
      print("You escaped successfully!")
      return "ESCAPE"

  return "WIN"
