# storage.py - Member C: Inventory & Save/Load System
import json


def save_game(player, game_map, filename="save.json"):
  data = {"player": player, "map": game_map}
  try:
    with open(filename, "w", encoding="utf-8") as f:
      json.dump(data, f, indent=4)
    return True
  except Exception as e:
    print(f"Error saving game: {e}")
    return False


def load_game(filename="save.json"):
  try:
    with open(filename, "r", encoding="utf-8") as f:
      data = json.load(f)
    print("Save file loaded successfully!")
    return data["player"], data["map"]
  except FileNotFoundError:
    print("No save file found. Starting fresh...")
    return None, None
