
# Slot-Machine
This program provides a fully interactive 5×3 slot machine built with Tkinter. It allows users to: Spin weighted reels, Adjust bets and paylines, View payouts through a paytable, Track credits, Highlight winning paylines, and Reset or quit the game cleanly.

## 1. Start the Slot Machine
Launches the Tkinter UI and initializes the reels, paytable, credits, and controls.

### How to Run
```
python main.py
```

When the program starts, a welcome pop‑up explains gameplay rules, controls, and benefits.

### What Happens on Startup
- 200 starting credits
- Bet/Line defaults to 2
- 5 active paylines (out of 9 total)
- Grid is randomized
- Mini‑paytable visible on the right side
- SPIN button ready for use

## 2. Spin the Reels
Performs a simulated slot machine spin with animated reels and weighted symbols.

### User Action
Click **SPIN** in the UI.

### Process
- Total Bet = Bet/Line × Active Lines
- Credits are deducted immediately
- Each reel stops at staggered times
- The game checks all active paylines for wins
- Any winning lines are highlighted

### Winning Example Response in UI
```
WIN! +40  (2 line(s))
```

### Losing Example Response
```
No win — try again!
```

If credits reach 0:
```
Out of credits! Press Reset.
```

## 3. Adjust Bet/Line
Controls the per‑line wager.

### Buttons
- **Bet -** decreases Bet/Line (min 1)
- **Bet +** increases Bet/Line (max 20)

### Effect on Gameplay
Higher Bet/Line = higher potential payouts.

## 4. Select Number of Paylines
Uses a spinbox to choose how many paylines are active.

### Control
```
Lines: [1–9]
```

### Effect
- More lines → more chances to win
- Also increases Total Bet before each spin

### Total Bet Display Example
```
Total Bet: 10
```

## 5. View Paytable
Opens a separate window containing:
- All 5 symbols (🍒, 🍋, 🔔, ⭐, 7)
- Payout multipliers for 3, 4, and 5 in a row
- All 9 paylines in left‑to‑right order

### User Action
Click **Paytable**.

### Paytable Example (per line)
```
🍋 → 3 in a row: Bet × 4
      4 in a row: Bet × 10
      5 in a row: Bet × 25
```

## 6. Help Menu
Provides a readable explanation of all controls, including:
- Credits
- Bet/Line
- Paylines
- Total Bet
- SPIN instructions
- How wins are calculated
- Reset / Quit behavior

### User Action
Click **Help** to open the pop‑up.

## 7. Reset the Game
Restores all default values and clears the grid.

### User Action
Click **Reset**.

### Confirmation Prompt
```
Are you sure you want to reset?
This will restore:
• Credits to 200
• Bet/Line to 2
• Lines to 5
and clear current highlights.
```

If confirmed, the program:
- Resets credits
- Resets bet values
- Resets paylines
- Clears highlights
- Randomizes the grid

## 8. Quit the Slot Machine
Closes the application.

### User Action
Click **Quit**.

### Confirmation Prompt
```
Are you sure you want to quit the slot machine?
```

(Spin animation must not be in progress.)

## Symbol Weights
| Symbol | Weight |
|--------|--------|
| 🍒 | 35 |
| 🍋 | 30 |
| 🔔 | 18 |
| ⭐ | 12 |
| 7 | 5 |

Higher weight → more common.

## Paylines (1–9)
```
1: [1,1,1,1,1]
2: [0,0,0,0,0]
3: [2,2,2,2,2]
4: [0,1,2,1,0]
5: [2,1,0,1,2]
6: [0,0,1,0,0]
7: [2,2,1,2,2]
8: [1,0,0,0,1]
9: [1,2,2,2,1]
```

## UML Sequence Diagram
```
sequenceDiagram
    participant User
    participant SlotMachine

    User->>SlotMachine: Click SPIN
    SlotMachine->>SlotMachine: Deduct credits (Total Bet)
    SlotMachine->>SlotMachine: Animate reels (staggered stopping)
    SlotMachine->>SlotMachine: Evaluate paylines
    SlotMachine-->>User: Display win or loss message
    SlotMachine-->>User: Highlight winning lines (if any)
```

## Summary
This Tkinter slot machine provides a full casino‑style experience with weighted symbols, animated reels, adjustable bets, paylines, and payout evaluation. The UI includes help menus, a full paytable, reset controls, and a polished workflow designed for ease of play and clarity.
