# Terminal Dungeon RPG (文字地牢冒險遊戲)

A modular, CLI-based turn-based dungeon crawler role-playing game developed in Python.  
基於 Python 開發的終端機文字版地牢探索與回合制角色扮演遊戲（模組化架構）。

---

## 1. Team Division of Labor (團隊分工)

| Member (組員) | Module & File (負責模組與檔案) | Key Responsibilities (核心職責) |
| :--- | :--- | :--- |
| **Kashish & Fariha**<br>(415410901 & 415410906) | **`map_engine.py`**<br>(Map & Navigation Engine / 地圖與移動引擎)<br><br>**`combat.py`**<br>(Combat & Stats Engine / 戰鬥與數值系統) | • **Map Engine**: 2D grid matrix generation, WASD player movement, wall/obstacle collision detection, and tile-based trigger events (Monsters, Boss, Exit).<br>• **Combat Engine**: Enemy data models (HP, ATK), interactive turn-based combat loop (Attack, Defend, Run), randomized damage, hit rates, and critical strikes.<br>*(Collaborated or divided between Kashish & Fariha / 由兩人合作或自選拆分)* |
| **Kai-Hsiang Yang (楊凱翔)** | **`storage.py`**<br>(Inventory & Persistence / 道具背包與存檔系統) | • Item definitions (potions, keys), inventory capacity/usage logic.<br>• Local JSON persistence: implementing `save_game()` and `load_game()` to save/restore player attributes, inventory, and dungeon progression. |
| **Yu-Ching Lin (林昱晴)**<br>(414515031) - *Lead Integrator* | **`main.py`**<br>(Architecture & Controller / 主控整合與狀態機) | • Global Finite State Machine (FSM: Menu $\rightarrow$ Map $\rightarrow$ Combat $\rightarrow$ Save/Over).<br>• Interface specification contract enforcement, Git branch merging, conflict resolution, CLI UI layout, and proposal coordination. |

---

## 2. Unified Data Structure Contract (共用資料規格契約)

To ensure seamless integration across all independent modules, all functions must strictly adhere to the following `player` dictionary structure:  
為了確保各模組獨立開發後能無縫串接，所有模組調用與更新玩家資料時，必須嚴格遵守以下 `player` 字典規格：

```python
player = {
    "name": "Hero",       # Player name / 玩家名稱 (str)
    "hp": 100,            # Current Health / 當前生命值 (int)
    "max_hp": 100,        # Max Health / 生命值上限 (int)
    "atk": 15,            # Base Attack / 基礎攻擊力 (int)
    "gold": 50,           # Gold coins / 身上金幣 (int)
    "x": 1,               # Grid X coordinate / 地圖 X 座標 (int)
    "y": 1,               # Grid Y coordinate / 地圖 Y 座標 (int)
    "inventory": [        # Item list / 背包物品清單 (list of str)
        "Health Potion",
        "Dungeon Key"
    ]
}
