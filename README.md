
# Slot‑Machine

This program provides a fully interactive **5×3 slot machine** built with Tkinter. It features:

- Real **reel strips** (100‑stop reels) with controlled symbol frequencies  
- Animated reel spins with staggered stopping  
- Adjustable bets and paylines  
- A full paytable window  
- Highlighted winning paylines  
- Credit tracking  
- Reset, Help, and Quit functionality  

## 1. Start the Slot Machine
Launching the program opens the Tkinter UI and initializes:

- Reel strips (5 reels, each with 100 positions)  
- Paytable multipliers for each symbol  
- Default credits, bets, and paylines  
- The slot grid (populated from reel strips)  
- A persistent mini‑paytable on the right  

### How to Run
```
python main.py
```

A welcome pop‑up explains gameplay, controls, and rules.

### Startup Defaults
- **200 credits**
- **Bet/Line = 2**
- **Active Lines = 5** (of 9 total)
- **Grid randomized from reel strip stops**
- **SPIN** button immediately available

## 2. Spin the Reels
Spinning now uses **true reel‑strip physics**, not weighted random choices.

### User Action
Click **SPIN**.

### What Happens
- Total Bet = **Bet/Line × Active Lines**
- Credits are deducted immediately  
- Each reel **advances through its strip** at different speeds  
- Reels stop sequentially (staggered stop ticks)  
- The final visible 3 symbols per reel come from the reel strip:
  ```
  strip[(stop_index + row) % strip_length]
  ```  
- After all reels stop, the game evaluates the selected paylines  
- Winning lines are highlighted in color

### Winning Example
```
WIN! +40  (2 line(s))
```

### Losing Example
```
No win — try again!
```

If credits reach zero:
```
Out of credits! Press Reset.
```

## 3. Adjust Bet/Line
Controls your per‑line wager.

### Controls
- **Bet -** : Minimum 1  
- **Bet +** : Maximum 20  

Higher bets produce proportionally higher payouts.

## 4. Select Number of Paylines
A spinbox lets the user activate anywhere from **1 to 9 paylines**.

More paylines:
- Increase hit frequency  
- Increase Total Bet  
- Do **not** change the symbol distribution or reel behavior  

### Example Display
```
Total Bet: 10
```

## 5. View Paytable
Shows a full payout reference, including:

- All symbols (🍒, 🍋, 🔔, ⭐, 7)  
- Multipliers for 3, 4, and 5 in a row  
- All 9 paylines in order  

### User Action
Click **Paytable**.

### Example (per line)
```
🍋 → 3 in a row: Bet × 4
      4 in a row: Bet × 10
      5 in a row: Bet × 25
```

## 6. Help Menu
Displays a detailed explanation of:

- Credits  
- Bets  
- Paylines  
- Total Bet  
- SPIN behavior  
- How wins are calculated  
- Reset/Quit rules  

### User Action
Click **Help**.

## 7. Reset the Game
Restores default values and clears highlights.

### User Action
Click **Reset** → Confirmation prompt appears:
```
Are you sure you want to reset?
This will restore:
• Credits to 200
• Bet/Line to 2
• Lines to 5
and clear current highlights.
```

Resetting:
- Resets credits  
- Resets bet and lines  
- Clears grid highlighting  
- Re‑randomizes reel stop positions  
- Renders a fresh 5×3 window from the strips  

## 8. Quit the Slot Machine
Closes the program (disabled while reels are still spinning).

### User Action
Click **Quit**.

Confirmation:
```
Are you sure you want to quit the slot machine?
```

## Reel Strips (Updated System)

The slot machine now uses **fixed, 100‑position reel strips** per reel.

Each reel contains:
| Symbol | Count |
|--------|-------|
| 🍒 | 45 |
| 🍋 | 29 |
| 🔔 | 13 |
| ⭐ | 10 |
| 7  | 3  |

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
    SlotMachine->>SlotMachine: Advance reel strips (animated)
    SlotMachine->>SlotMachine: Stagger reel stops
    SlotMachine->>SlotMachine: Evaluate paylines
    SlotMachine-->>User: Display win or loss message
    SlotMachine-->>User: Highlight winning lines (if any)
```

## Summary
This slot machine now uses **true reel strips** for realistic spinning, controlled probabilities, and accurate RTP modeling. It includes:

- 5×3 reels with animated strip‑based spins  
- Adjustable bets and paylines  
- Full paytable and help menu  
- Winning line highlighting  
- Reset and quit with confirmation  
- A polished, user‑friendly gameplay loop  
