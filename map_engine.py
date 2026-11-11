# map_engine.py - Member A: Map & Movement Engine


def init_map():
  # 10x10 地圖: # 牆壁, . 空地, E 敵人, B 首領, D 終點門
  return [
      ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
      ["#", ".", ".", ".", "#", ".", ".", "E", ".", "#"],
      ["#", ".", "#", ".", "#", ".", "#", "#", ".", "#"],
      ["#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
      ["#", ".", "#", "#", "#", "#", ".", "#", ".", "#"],
      ["#", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
      ["#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
      ["#", ".", ".", "E", ".", ".", ".", ".", ".", "#"],
      ["#", ".", "#", "#", "#", "#", "#", "#", "B", "#"],
      ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
  ]


def render_map(grid, player_pos):
  px, py = player_pos
  print("\n--- Current Dungeon ---")
  for y in range(len(grid)):
    row_str = ""
    for x in range(len(grid[0])):
      if (x, y) == (px, py):
        row_str += "P "  # 玩家位置
      else:
        row_str += grid[y][x] + " "
    print(row_str)


def move_player(grid, player_pos, direction):
  px, py = player_pos
  dx, dy = 0, 0
  if direction == "W":
    dy = -1
  elif direction == "S":
    dy = 1
  elif direction == "A":
    dx = -1
  elif direction == "D":
    dx = 1

  nx, ny = px + dx, py + dy
  # 邊界與牆壁碰撞檢查
  if grid[ny][nx] == "#":
    print("Blocked by a wall!")
    return player_pos, "EMPTY"

  event = "EMPTY"
  if grid[ny][nx] == "E":
    event = "MONSTER"
    grid[ny][nx] = "."  # 戰勝後清除該格怪物標記
  elif grid[ny][nx] == "B":
    event = "BOSS"

  return (nx, ny), event
