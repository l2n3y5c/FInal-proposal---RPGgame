# main.py - System Integration & Game Loop (Lead Integrator)
import combat
import map_engine
import storage


def main():
  print("=== Welcome to Terminal Dungeon RPG ===")
  choice = input("1. New Game\n2. Load Game\nChoice: ")

  if choice == "2":
    player, game_map = storage.load_game()
  else:
    player = {
        "name": "Hero",
        "hp": 100,
        "max_hp": 100,
        "atk": 15,
        "gold": 0,
        "x": 1,
        "y": 1,
        "inventory": [],
    }
    game_map = map_engine.init_map()

  game_running = True
  while game_running:
    map_engine.render_map(game_map, (player["x"], player["y"]))
    cmd = input("Move (W/A/S/D) or Save (P) or Quit (Q): ").strip().upper()

    if cmd == "P":
      storage.save_game(player, game_map)
      print("Game progress saved!")
      continue
    elif cmd == "Q":
      print("Exiting game...")
      break

    new_pos, event = map_engine.move_player(
        game_map, (player["x"], player["y"]), cmd
    )
    player["x"], player["y"] = new_pos

    if event == "MONSTER":
      result = combat.start_battle(player, "Goblin")
      if result == "LOSE":
        print("Game Over!")
        game_running = False
    elif event == "BOSS":
      result = combat.start_battle(player, "Dragon Boss")
      if result == "WIN":
        print("Victory! You beat the dungeon!")
        game_running = False


if __name__ == "__main__":
  main()
