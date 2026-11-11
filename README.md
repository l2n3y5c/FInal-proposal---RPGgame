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
    "name": "Hero",  # Player name / 玩家名稱 (str)
    "hp": 100,  # Current Health / 當前生命值 (int)
    "max_hp": 100,  # Max Health / 生命值上限 (int)
    "atk": 15,  # Base Attack / 基礎攻擊力 (int)
    "gold": 50,  # Gold coins / 身上金幣 (int)
    "x": 1,  # Grid X coordinate / 地圖 X 座標 (int)
    "y": 1,  # Grid Y coordinate / 地圖 Y 座標 (int)
    "inventory": [  # Item list / 背包物品清單 (list of str)
        "Health Potion",
        "Dungeon Key",
    ],
}
```

---

## 3. Project Overview & Features (專案簡介與核心特色)

### English
**Terminal Dungeon RPG** is a retro, lightweight, turn-based dungeon crawler game designed to run directly within the command-line interface (CLI)[cite: 4]. Players navigate through an uncharted 2D maze using directional controls, explore rooms shrouded in fog, encounter randomized monsters, manage inventory items, and defeat the guardian boss to escape[cite: 4].

* **2D Grid-based Exploration**: Procedural or file-loaded maze layouts featuring obstacle collision and movement validation[cite: 4].
* **Turn-Based Combat Loop**: Strategic combat mechanics including basic attacks, skill usage, health potions, and tactical escape options[cite: 4].
* **Persistent Game State**: Instant saving and loading via local JSON storage, preserving player progression and map status across sessions[cite: 4].
* **Modular Software Architecture**: High-cohesion and low-coupling components ensuring clean separation of concerns among team members[cite: 4, 8, 12].

### 中文說明
**Terminal Dungeon RPG** 是一款在終端機（CLI）運行的輕量化復古文字地牢冒險遊戲[cite: 4]。玩家透過方向鍵控制角色在未知迷宮中探索，穿越視野迷霧、收集關鍵道具與藥水、遭遇隨機怪物進行回合制戰鬥，並以擊敗地牢守門 Boss 為最終通關目標[cite: 4]。

* **二維網格探索**：支援陣列地圖載入、牆壁障礙碰撞判定與即時座標更新[cite: 4]。
* **回合制戰鬥迴圈**：提供普通攻擊、技能施放、道具飲用與逃跑判定等多樣化戰術指令[cite: 4]。
* **資料持久化保存**：利用本地 JSON 格式隨時存檔與讀檔，完整保留角色血量、金幣、背包與關卡進度[cite: 4]。
* **模組化軟體架構**：採用關注點分離原則，各子模組高內聚低耦合，利於團隊獨立開發與整合測試[cite: 4, 8, 12]。

---

## 4. System Architecture & State Machine (系統架構與狀態流程)

The game execution is driven by a central Finite State Machine (FSM)[cite: 4]:  
遊戲主控流程由有限狀態機驅動，狀態切換流程如下[cite: 4]：

```text
                  +-----------------------+
                  |   Main Menu (主選單)   |
                  +-----------------------+
                         /         \
          [Load Game / 讀取]     [New Game / 新增]
                       \             /
                        v           v
            +-----------------------------------+
            |  Exploration Mode (地圖探索模式)   | <----+ (Flee/Win / 戰鬥結束)
            +-----------------------------------+      |
                |               |             |        |
        (Encounter / 遭遇)  (Chest / 寶箱) (Save / 存檔) |
                v               v             v        |
     +--------------------+ [Add Items]  [JSON File]   |
     | Combat (戰鬥模式)  |                            |
     +--------------------+ ---------------------------+
        |            |
     (Defeat)     (Boss Clear)
        v            v
  [Game Over]   [Victory Screen]
```

---

## 5. Project Directory Structure (專案檔案結構)

```text
FInal-proposal---RPGgame/
│
├── main.py              # Central entry point & state controller (主程式進入點與狀態整合)
├── map_engine.py        # 2D matrix rendering & collision detection (地圖引擎與探索移動)
├── combat.py            # Battle loops & numerical combat balance (戰鬥機制與數值演算法)
├── storage.py           # Inventory tracking & JSON persistence (背包管理與檔案存檔/讀檔)
├── README.md            # Project specification & documentation (專案規格與說明文件)
├── .gitignore           # Ignored temporary files & cache (Git 忽略清單)
└── save.json            # Local save state file (Auto-generated) (本機存檔檔，自動生成)
```

---

## 6. Getting Started & Execution (執行方式)

### Prerequisites (環境需求)
* Python 3.8+ installed on your operating system.

### How to Run (如何執行)
Clone the repository and launch the game directly via the terminal:  
將專案複製到本地並在終端機啟動：

```bash
# 1. Clone this repository (複製儲存庫)
git clone [https://github.com/l2n3y5c/FInal-proposal---RPGgame.git](https://github.com/l2n3y5c/FInal-proposal---RPGgame.git)

# 2. Navigate to project root (進入專案資料夾)
cd FInal-proposal---RPGgame

# 3. Launch game (啟動遊戲)
python main.py
```

---

## 7. Project Milestones & Timeline (開發進度與里程碑)

| Milestone (階段) | Target Date (目標日期) | Key Deliverables & Goals (核心成果與目標) |
| :--- | :--- | :--- |
| **Proposal Submission** | **2026/11/24 (Tue) 23:59** | • Finalize and submit Proposal slides (PDF format, font size 12, APA style)[cite: 8].<br>• Submit 5-minute video presentation (MP4) to eCourse2[cite: 8]. |
| **Module Prototyping** | **2026/12/05 (Sat)** | • Complete individual sub-module prototypes (`map_engine.py`, `combat.py`, `storage.py`).<br>• Ensure all modules follow the unified `player` data dictionary and API contracts. |
| **System Integration** | **2026/12/12 (Sat)** | • Integrate all sub-modules into `main.py` via the central Finite State Machine (FSM).<br>• Conduct end-to-end bug tests, resolve merge conflicts, and polish CLI UI formatting. |
| **Final Class Demo** | **2026/12/15 (Tue)** | • Live in-class presentation and 8-minute projector functional demonstration[cite: 4, 7]. |
| **Written Report Due** | **2026/12/23 (Wed) 23:59** | • Submit comprehensive final written report (PDF, at least 9 content pages, font size 12, APA 6th edition)[cite: 14]. |
