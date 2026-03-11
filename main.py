import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random
import json
import urllib.request
import urllib.error
import urllib.parse

LOGIN_URL = "http://127.0.0.1:8081/auth/login"
RNG_URL = "http://127.0.0.1:8088/reels/spin"
class SlotMachineApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Slot Machine (5x3)")
        self.resizable(False, False)

        # -------------------------
        # Configuration
        # -------------------------
        self.reels = 5
        self.rows = 3

        self.symbols = ["🍒", "🍋", "🔔", "⭐", "7"]
        self.scatter_symbol = "🎁"
        self.scatter_threshold = 3
        self.scatter_highlight = "#C7F0BD"

        self.reel_strips = [
            # Reel 1 (len=100)
            [
            '🔔','🍋','🍋','🍋','🍋','🍋','🍋','⭐','🍋','🍋','🎁','🍒','🍋','🍒','🍒','🍒','🍒','🍒','🍋','🍒',
            '🍋','🍒','🍒','🍋','🔔','🍒','🍋','⭐','🍒','🔔','🎁','🔔','🍒','🍒','🔔','🍒','🍒','🍋','⭐','🍋',
            '🍋','🍒','🍒','7','⭐','🍋','🍒','🍒','🎁','🍒','🍋','🔔','🍒','🍒','🍒','🍋','🍋','⭐','🍒','🍒',
            '🍒','🔔','🍒','🍒','🍒','🍋','🍒','7','🎁','🍒','⭐','🍒','🍒','🍒','🍋','🍒','🍒','🔔','🍋','🔔',
            '🍒','🍋','🍒','🍒','🍒','⭐','🍒','⭐','🔔','🔔','🍋','⭐','🍒','🍒','🔔','🍋','7','🍋','🍋','🎁'
            ]
            # Reel 2 (len=100)
            [
            '🍒','🍒','⭐','🍒','⭐','🍒','🍋','🍒','🍒','🍒','🎁','⭐','⭐','🔔','🍒','🍋','🍋','7','🔔','🍋',
            '🍒','🔔','🍋','🍒','🍋','🍋','🍋','🍒','🍋','🎁','🍋','🔔','🍋','🍒','🍒','🍋','🍋','🍒','🍒','🍋',
            '🍒','🍋','🍋','🍒','🍋','🍒','🍒','⭐','🎁','7','🍒','🍒','⭐','🔔','🍋','🍋','7','🍒','🍒','🍋',
            '🔔','🍋','⭐','🔔','🍋','🍋','🔔','🍒','🍒','🍒','🍋','🍒','🎁','🍒','🍋','🍒','🍒','🔔','🍒','🍋',
            '🔔','🍋','🍋','🍒','🔔','🍒','🍒','🍒','🍒','🍒','🍒','🔔','🍒','⭐','🍒','🍋','🔔','🍒','🍒','🎁'
            ]

            # Reel 3 (len=100)
            [
            '🔔','🍋','🍋','🍋','🍋','🍋','🍒','🍒','🔔','🍒','🎁','🍒','⭐','🍒','🔔','🍒','🍋','⭐','🍒','⭐',
            '🍋','🍋','🍒','🍒','🍒','7','🍒','🍋','🔔','🎁','⭐','🍒','🍒','7','🍋','🔔','🍒','7','🍒','🍒',
            '🍋','🔔','⭐','🍒','🍋','🍒','🍒','🍒','🍒','🍋','🎁','🍒','🍒','🍒','🍒','🍒','🍋','🍒','🍒','🍋',
            '🍋','🍒','🔔','⭐','🍋','🍒','🍒','🔔','🍋','🍒','🍒','🍒','🍒','⭐','🍋','🍒','🍋','🍋','🍒','🍋',
            '🎁','🍒','🔔','🍒','🍋','⭐','⭐','🍒','🍋','🔔','⭐','🍒','🍋','🍋','🔔','🍋','🍒','🍒','🔔','🎁'
            ]
            # Reel 4 (len=100)
            [
            '🍋','🍒','🔔','🍋','🍒','🍋','🍋','🍒','🍒','🍒','🎁','7','🔔','🍒','🍒','🍋','🍋','🍋','🍒','🍋',
            '🍒','🍒','⭐','🍒','🍋','🍒','⭐','🍒','🍒','🎁','🍋','🍒','🍋','🍒','7','🍋','🔔','🍋','🍋','🍒',
            '🍋','🍒','🍒','🔔','🔔','🔔','🍒','🔔','🔔','🎁','⭐','🍋','🍒','🍋','🍒','7','🍋','🍋','🍋','🍒',
            '🍒','🍒','⭐','🍒','⭐','🍒','🍒','🍒','🔔','🍒','🔔','⭐','🔔','🍒','🍒','🍒','🍋','🎁','🍋','🔔',
            '⭐','🔔','🍒','🍋','🍒','🍒','🍒','🍋','⭐','⭐','🍒','🍒','🍒','🍋','🍒','🍒','⭐','🍋','🍋','🎁'
            ]
            # Reel 5 (len=100)
            [
            '🔔','🍋','⭐','🍋','🍒','🍒','🍒','🍋','🔔','🍒','🎁','🍒','🍒','🍋','🍒','🍒','🍒','🍒','🍒','🔔',
            '🍋','🍒','🍒','🍋','🍒','🔔','🔔','🍒','⭐','🍋','🎁','7','🔔','🍒','🍋','🍒','🍒','🍋','🍋','🍒',
            '🍒','🔔','🍒','🍋','🍋','🍋','🍒','🍒','🍒','⭐','🎁','🍒','🍋','⭐','🍋','🍋','🍒','🍋','🍒','7',
            '⭐','🍒','🍒','⭐','🔔','🍒','🔔','⭐','⭐','🔔','🍋','🍒','🍒','🍋','🍋','🍒','🍋','🍒','🔔','🎁',
            '🍒','🍒','🍋','🍋','🍒','🍋','🍋','🔔','🍋','🍋','🍋','🔔','🍋','7','⭐','🍒','🍒','🍒','⭐','🎁'
            ]     
        ]


        # Payout multipliers PER LINE for 3/4/5-of-a-kind (left-to-right)
        # winnings = bet_per_line * multiplier
        self.paytable = {
            "🍒": {3: 3, 4: 8, 5: 20},
            "🍋": {3: 4, 4: 10, 5: 25},
            "🔔": {3: 6, 4: 15, 5: 40},
            "⭐": {3: 10, 4: 25, 5: 80},
            "7": {3: 25, 4: 80, 5: 250},
        }

        # Define paylines as a list of row indices for each reel (length = 5)
        # Row indices: 0=top, 1=middle, 2=bottom
        self.all_paylines = [
            [1, 1, 1, 1, 1],  # 1) middle
            [0, 0, 0, 0, 0],  # 2) top
            [2, 2, 2, 2, 2],  # 3) bottom
            [0, 1, 2, 1, 0],  # 4) V shape
            [2, 1, 0, 1, 2],  # 5) inverted V
            [0, 0, 1, 0, 0],  # 6) top dip
            [2, 2, 1, 2, 2],  # 7) bottom bump
            [1, 0, 0, 0, 1],  # 8) top run with ends middle
            [1, 2, 2, 2, 1],  # 9) bottom run with ends middle
        ]

        # -------------------------
        # State
        # -------------------------
        self.credits = tk.IntVar(value=200)
        self.bet_per_line = tk.IntVar(value=2)
        self.active_lines = tk.IntVar(value=5)  # user can choose 1..len(all_paylines)
        self.message = tk.StringVar(value="Press SPIN to play!")
        self.spinning = False
        self.paytable_win = None
        self.biggest_record = tk.StringVar(value="-")

        # Reel stop indices (top visible row index per reel)
        self.current_stops = [0] * self.reels

        # Grid values (StringVars) and label widgets for highlight
        self.grid_vars = [[tk.StringVar(value="") for _ in range(self.reels)] for _ in range(self.rows)]
        self.cell_labels = [[None for _ in range(self.reels)] for _ in range(self.rows)]

        self._build_ui()
        self._randomize_full_grid_from_strips()

        self.auth_token = None
        self.prompt_login()

        self.after(150, self.show_welcome)

        rec = self._leaderboard_biggest("tk5x3:v1")
        if rec and "amount" in rec:
            self.biggest_record.set(str(rec["amount"]))

    def show_welcome(self):
        """Show a startup pop-up explaining the program and its benefits."""
        text = (
            "Welcome to Zach's Slot Machine!\n\n"
            "What this program does:\n"
            "• Simulates a 5‑reel, 3‑row slot machine with multiple paylines.\n"
            "• Now uses REEL STRIPS for realistic spinning and slot math control.\n"
            "• Lets you choose how many paylines to play and your bet per line.\n"
            "• Calculates wins based on 3/4/5‑of‑a‑kind from left to right.\n\n"
            "How it benefits you:\n"
            "• Practice decision‑making with risk/reward.\n"
            "• Visualize probability/odds and bankroll management.\n"
            "• Realistic reel behavior suitable for bonus triggers and audits.\n\n"
            "How to play:\n"
            "1) Set Lines and Bet/Line\n"
            "2) Press SPIN\n"
            "3) Use Paytable to see all payouts\n\n"
            "Good luck!"
        )
        messagebox.showinfo("Welcome!", text)

    def show_help(self):
        help_text = (
            "HELP — Controls & What They Do\n\n"
            "Credits:\n"
            "• Shows how many credits you currently have.\n\n"
            "Bet/Line:\n"
            "• The amount you wager on each active payline.\n"
            "• Bet - : Decrease your bet per line (min 1).\n"
            "• Bet + : Increase your bet per line (max 20).\n\n"
            "Lines (Spinbox):\n"
            "• Selects how many paylines are active for the next spin.\n"
            "• More lines = higher total bet, but more chances to win.\n\n"
            "Total Bet:\n"
            "• Displays Bet/Line × Active Lines.\n"
            "• This amount is deducted when you press SPIN.\n\n"
            "SPIN:\n"
            "• Starts a spin if you have enough credits.\n"
            "• Deducts the Total Bet upfront.\n"
            "• Reels spin by advancing their strip indices and then stop.\n\n"
            "Paytable:\n"
            "• Opens the full paytable window.\n"
            "• Shows the payout multipliers for 3/4/5-of-a-kind per line.\n"
            "• Also lists all paylines.\n\n"
            "Reset:\n"
            "• Restores credits to 200, bet/line to 2, and active lines to 5.\n"
            "• Clears highlights and randomizes the grid.\n\n"
            "Quit:\n"
            "• Closes the application.\n\n"
            "How wins work (quick overview):\n"
            "• Only left-to-right matches starting from reel 1 count.\n"
            "• 3+ matching symbols in a row on a payline pay out.\n"
            "Scatter Bonus:\n"
            "• 🎁 appears anywhere on the reels.\n"
            "• 3+ triggers a Free Spin bonus.\n\n"

        )
        messagebox.showinfo("Help", help_text)

    # -------------------------
    # UI
    # -------------------------
    def _build_ui(self):
        root = ttk.Frame(self, padding=12)
        root.grid(row=0, column=0)

        # Layout: left game area + right mini paytable
        left = ttk.Frame(root)
        left.grid(row=0, column=0, padx=(0, 12), sticky="n")
        right = ttk.Frame(root)
        right.grid(row=0, column=1, sticky="n")

        # Top bar: credits / bet / lines
        top = ttk.Frame(left)
        top.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        ttk.Label(top, text="Credits:").grid(row=0, column=0, padx=(0, 6))
        ttk.Label(top, textvariable=self.credits, width=8).grid(row=0, column=1, sticky="w")

        ttk.Label(top, text="Bet/Line:").grid(row=0, column=2, padx=(18, 6))
        ttk.Label(top, textvariable=self.bet_per_line, width=6).grid(row=0, column=3, sticky="w")
        ttk.Button(top, text="Bet -", command=self.bet_down).grid(row=0, column=4, padx=(18, 4))
        ttk.Button(top, text="Bet +", command=self.bet_up).grid(row=0, column=5, padx=(0, 10))

        ttk.Label(top, text="Lines:").grid(row=0, column=6, padx=(6, 6))
        self.lines_spin = ttk.Spinbox(
            top,
            from_=1,
            to=len(self.all_paylines),
            textvariable=self.active_lines,
            width=4,
            command=self._update_total_bet_label,
            wrap=True
        )
        self.lines_spin.grid(row=0, column=7, sticky="w")

        self.total_bet_label = ttk.Label(top, text="")
        self.total_bet_label.grid(row=0, column=8, padx=(18, 0), sticky="w")
        self._update_total_bet_label()
        ttk.Label(top, text="Record:").grid(row=0, column=9, padx=(18, 6))
        ttk.Label(top, textvariable=self.biggest_record, width=8).grid(row=0, column=10, sticky="w")    

        # Slot grid frame (use tk.Label for easy background highlighting)
        grid_frame = ttk.Frame(left)
        grid_frame.grid(row=1, column=0, pady=(0, 10))

        # Choose font; fallback if emoji font not available
        self.symbol_font = ("Segoe UI Emoji", 28)

        # Create 3x5 grid
        for r in range(self.rows):
            for c in range(self.reels):
                cell = tk.Label(
                    grid_frame,
                    textvariable=self.grid_vars[r][c],
                    font=self.symbol_font,
                    width=3,
                    relief="ridge",
                    borderwidth=2,
                    bg="white"
                )
                cell.grid(row=r, column=c, padx=4, pady=4)
                self.cell_labels[r][c] = cell

        # Message
        ttk.Label(left, textvariable=self.message, font=("Segoe UI", 12)).grid(row=2, column=0, pady=(0, 10))

        # Controls
        controls = ttk.Frame(left)
        controls.grid(row=3, column=0)
        self.spin_btn = ttk.Button(controls, text="SPIN", command=self.start_spin)
        self.spin_btn.grid(row=0, column=0, padx=6)
        ttk.Button(controls, text="Paytable", command=self.show_paytable).grid(row=0, column=1, padx=6)
        ttk.Button(controls, text="Help", command=self.show_help).grid(row=0, column=2, padx=6)
        ttk.Button(controls, text="Reset", command=self.confirm_reset).grid(row=0, column=3, padx=6)
        ttk.Button(controls, text="Quit", command=self.confirm_quit).grid(row=0, column=4, padx=6)

        # -------------------------
        # Hybrid mini paytable (always visible)
        # -------------------------
        mini = ttk.LabelFrame(right, text="Mini Paytable (per line)", padding=10)
        mini.grid(row=0, column=0, sticky="n")

        # Show top 3 "5 of a kind" payouts as a quick reference
        top_wins = sorted(
            ((sym, self.paytable[sym][5]) for sym in self.symbols),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        ttk.Label(mini, text="Top Wins:", font=("Segoe UI", 11, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 8))
        for i, (sym, mult) in enumerate(top_wins, start=1):
            ttk.Label(mini, text=f"{sym*5}", font=("Segoe UI Emoji", 14)).grid(row=i, column=0, sticky="w")
            ttk.Label(mini, text=f"Bet × {mult}").grid(row=i, column=1, sticky="w", padx=(12, 0))

        ttk.Separator(mini).grid(row=5, column=0, columnspan=2, sticky="ew", pady=10)
        ttk.Label(mini, text="Tip: Use Paytable button\nfor full 3/4/5 payouts.").grid(row=6, column=0, columnspan=2, sticky="w")

    # -------------------------
    # Helpers
    # -------------------------
    def _update_total_bet_label(self):
        total = self.total_bet()
        self.total_bet_label.config(text=f"Total Bet: {total}")

    def total_bet(self):
        lines = max(1, min(self.active_lines.get(), len(self.all_paylines)))
        return self.bet_per_line.get() * lines

    # ----- Reel-strip rendering helpers -----
    def _render_from_strips(self, stops):
        """
        Render the visible 3x5 window from reel strips using provided stop indices.
        For each reel c: rows 0..2 are strip[(stop + r) % len(strip)].
        """
        for c in range(self.reels):
            strip = self.reel_strips[c]
            L = len(strip)
            stop = stops[c] % L
            for r in range(self.rows):
                sym = strip[(stop + r) % L]
                self.grid_vars[r][c].set(sym)

    def _randomize_full_grid_from_strips(self):
        """Pick random stops per reel and render."""
        self.current_stops = self.get_rng_stops(seed=None)
        self._render_from_strips(self.current_stops)

    def _reset_highlights(self):
        for r in range(self.rows):
            for c in range(self.reels):
                self.cell_labels[r][c].config(bg="white")

    def _highlight_line(self, payline, color="light goldenrod"):
        for c, r in enumerate(payline):
            self.cell_labels[r][c].config(bg=color)

    def _highlight_cells(self, coords, color):
        """Highlight arbitrary (row, col) cells."""
        for (r, c) in coords:
            if 0 <= r < self.rows and 0 <= c < self.reels:
                self.cell_labels[r][c].config(bg=color)

    def get_active_paylines(self):
        n = max(1, min(self.active_lines.get(), len(self.all_paylines)))
        return self.all_paylines[:n]
    
    def _check_bonus_via_service_urllib(self, prob=1.0, seed=None):
        url = "http://127.0.0.1:8095/bonus/evaluate"
        payload = {
            "grid": self._current_grid(),
            "config": {
                "type": "scatter_count",
                "symbol": getattr(self, "scatter_symbol", "🎁"),
                "count": getattr(self, "scatter_threshold", 3),
                "prob": prob
            }
        }
        if seed is not None:
            payload["seed"] = int(seed)

        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=0.9) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError):
            return {"bonusTriggered": False, "highlights": []}
        
    def _leaderboard_record(self, amount: int, game_id: str = None):
        url = "http://127.0.0.1:8090/leaderboard/record"
        body = {"amount": int(amount)}
        if game_id and game_id.strip():
            body["gameId"] = game_id

        try:
            data = json.dumps(body).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=0.9) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError):
            return None

    def _leaderboard_biggest(self, game_id: str = None):
        base = "http://127.0.0.1:8090/leaderboard/biggest-win"
        qs = ""
        if game_id and game_id.strip():
            qs = "?gameId=" + urllib.parse.quote(game_id)
        url = base + qs

        try:
            with urllib.request.urlopen(url, timeout=0.9) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError):
            return None
        
    def _post_json(self, url, payload, token=None, timeout=1.0):
        data = json.dumps(payload).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def prompt_login(self):
        try:
            user = simpledialog.askstring("Login", "Username:")
            if user is None:
                self.message.set("Proceeding as guest.")
                return
            pw = simpledialog.askstring("Login", "Password:", show="*")
            if pw is None:
                self.message.set("Proceeding as guest.")
                return
            token = self._login_request(user, pw)
            if token:
                self.auth_token = token
                self.message.set(f"Logged in as {user}.")
            else:
                self.message.set("Login failed — proceeding as guest.")
        except Exception:
            self.message.set("Login service unavailable — proceeding as guest.")

    def _login_request(self, username, password):
        try:
            resp = self._post_json(LOGIN_URL, {"username": username, "password": password}, timeout=1.5)
            return resp.get("access_token") or resp.get("token")
        except Exception:
            return None

    def get_rng_stops(self, seed=None):
        strip_lengths = [len(s) for s in self.reel_strips]
        payload = {"strip_lengths": strip_lengths}
        if seed is not None:
            payload["seed"] = int(seed)
        try:
            resp = self._post_json(RNG_URL, payload, token=self.auth_token, timeout=0.9)
            stops = resp.get("stops", None)
            if not stops or len(stops) != len(strip_lengths):
                raise ValueError("Bad RNG response shape.")
            # Ensure indices are in range
            for i, L in enumerate(strip_lengths):
                stops[i] = int(stops[i]) % L
            return stops
        except Exception:
            # Fallback: local random 
            return [random.randrange(L) for L in strip_lengths]

    # -------------------------
    # Bet controls
    # -------------------------
    def bet_up(self):
        if self.spinning:
            return
        self.bet_per_line.set(min(20, self.bet_per_line.get() + 1))
        self._update_total_bet_label()

    def bet_down(self):
        if self.spinning:
            return
        self.bet_per_line.set(max(1, self.bet_per_line.get() - 1))
        self._update_total_bet_label()

    # -------------------------
    # Game flow
    # -------------------------
    def start_spin(self):
        if self.spinning:
            return
        self._reset_highlights()
        self._update_total_bet_label()

        cost = self.total_bet()
        if self.credits.get() < cost:
            self.message.set("Not enough credits for that bet!")
            return

        # Deduct cost and start spinning
        self.credits.set(self.credits.get() - cost)
        self.message.set("Spinning...")
        self.spinning = True
        self.spin_btn.state(["disabled"])

        # Create staggered stop ticks for each reel (longer reels can spin longer)
        base_ticks = 22
        gap = 3
        stop_ticks = [base_ticks + i * gap for i in range(self.reels)]

        # Optional: give each reel an initial angular velocity in "steps per tick"
        self._spin_speeds = [3, 4, 5, 4, 3]  # steps per tick per reel (tune feel)
        self._tick = 0

        # Choose random final stops now, and we'll decelerate into them
        self.spin_index = getattr(self, "spin_index", 0) + 1
        self._final_stops = self.get_rng_stops(seed=self.spin_index)

        self._animate_spin(stop_ticks)

    def _animate_spin(self, stop_ticks):
        """
        Advance each reel's stop index while tick < stop_ticks[c].
        On the last tick for a reel, snap its index to the final stop to ensure determinism.
        """
        any_spinning = False
        for c in range(self.reels):
            if self._tick < stop_ticks[c]:
                # advance the reel by its speed
                speed = self._spin_speeds[c]
                self.current_stops[c] = (self.current_stops[c] + speed) % len(self.reel_strips[c])
                any_spinning = True
            elif self._tick == stop_ticks[c]:
                # final snap to preselected stop for clean stop
                self.current_stops[c] = self._final_stops[c] % len(self.reel_strips[c])

        # Render current window
        self._render_from_strips(self.current_stops)

        if any_spinning:
            self._tick += 1
            self.after(45, lambda: self._animate_spin(stop_ticks))
        else:
            # Done
            self.finish_spin()

    def finish_spin(self):
        wins, total_win = self.evaluate_wins()

        if total_win > 0:
            self.credits.set(self.credits.get() + total_win)
            colors = ["light goldenrod", "light cyan", "light pink", "pale green"]
            for i, w in enumerate(wins):
                self._highlight_line(w["payline"], color=colors[i % len(colors)])
            record = self._leaderboard_record(total_win, game_id="tk5x3:v1")
            if record:
                rec = self._leaderboard_biggest("tk5x3:v1")
                if rec and "amount" in rec:
                    self.biggest_record.set(str(rec["amount"]))
            if record and record.get("updated"):
                self.message.set(f"WIN! +{total_win}  — NEW RECORD 🎉")
            else:
                self.message.set(f"WIN! +{total_win} ({len(wins)} line(s))")
        else:
            self.message.set("No win — try again!")

        if not hasattr(self, "scatter_symbol"):
            self.scatter_symbol = "🎁"
        if not hasattr(self, "scatter_threshold"):
            self.scatter_threshold = 3
        scatter_color = getattr(self, "scatter_highlight", "#C7F0BD")

        self.spin_index = getattr(self, "spin_index", 0) + 1
        bonus = self._check_bonus_via_service_urllib(prob=1.0, seed=self.spin_index)  

        msg = self.message.get()
        if bonus.get("bonusTriggered"):
            coords = [(h["r"], h["c"]) for h in bonus.get("highlights", [])]
            self._highlight_cells(coords, scatter_color)
            bonus_msg = f"BONUS TRIGGERED ({len(coords)} {self.scatter_symbol})!"
            if msg:
                self.message.set(f"{msg}  |  {bonus_msg}")
            else:
                self.message.set(bonus_msg)

        self.spinning = False
        self.spin_btn.state(["!disabled"])

        if self.credits.get() <= 0:
            self.message.set("Out of credits! Press Reset.")

    def evaluate_wins(self):
        bet = self.bet_per_line.get()
        paylines = self.get_active_paylines()
        wins = []
        total_win = 0

        for idx, payline in enumerate(paylines, start=1):
            line_symbols = [self.grid_vars[payline[c]][c].get() for c in range(self.reels)]
            first = line_symbols[0]

            if first == '🎁':
                continue
            run = 1
            for c in range(1, self.reels):
                if line_symbols[c] == first:
                    run += 1
                else:
                    break

            if run >= 3:
                mult = self.paytable.get(first, {}).get(run, 0)
                win_amt = bet * mult
                if win_amt > 0:
                    wins.append({
                        "line_index": idx,
                        "payline": payline,
                        "symbol": first,
                        "run": run,
                        "mult": mult,
                        "amount": win_amt,
                        "symbols": line_symbols
                    })
                    total_win += win_amt

        return wins, total_win

    def show_paytable(self):
        if self.paytable_win and self.paytable_win.winfo_exists():
            self.paytable_win.deiconify()
            self.paytable_win.lift()
            self.paytable_win.focus_force()
            return

        win = tk.Toplevel(self)
        self.paytable_win = win
        win.title("Paytable (Full)")
        win.resizable(False, False)
        win.transient(self)

        wrapper = ttk.Frame(win, padding=12)
        wrapper.grid(row=0, column=0, sticky="nsew")

        ttk.Label(wrapper, text="FULL PAYTABLE (per line)", font=("Segoe UI", 14, "bold")).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 10))
        ttk.Label(wrapper, text="Symbol").grid(row=1, column=0, sticky="w", padx=(0, 18))
        ttk.Label(wrapper, text="3 in a row").grid(row=1, column=1, sticky="w", padx=(0, 18))
        ttk.Label(wrapper, text="4 in a row").grid(row=1, column=2, sticky="w", padx=(0, 18))
        ttk.Label(wrapper, text="5 in a row").grid(row=1, column=3, sticky="w")

        ttk.Separator(wrapper).grid(row=2, column=0, columnspan=4, sticky="ew", pady=8)

        for r, sym in enumerate(self.symbols, start=3):
            ttk.Label(wrapper, text=sym, font=("Segoe UI Emoji", 14)).grid(row=r, column=0, sticky="w")
            ttk.Label(wrapper, text=f"Bet × {self.paytable[sym][3]}").grid(row=r, column=1, sticky="w")
            ttk.Label(wrapper, text=f"Bet × {self.paytable[sym][4]}").grid(row=r, column=2, sticky="w")
            ttk.Label(wrapper, text=f"Bet × {self.paytable[sym][5]}").grid(row=r, column=3, sticky="w")

        ttk.Separator(wrapper).grid(row=r+1, column=0, columnspan=4, sticky="ew", pady=10)
        ttk.Label(wrapper, text="Active Paylines:", font=("Segoe UI", 11, "bold")).grid(row=r+2, column=0, columnspan=4, sticky="w", pady=(0, 6))
        for i, pl in enumerate(self.all_paylines, start=1):
            ttk.Label(wrapper, text=f"Line {i}: {pl}").grid(row=r+2+i, column=0, columnspan=4, sticky="w")

        ttk.Button(wrapper, text="Close", command=win.destroy).grid(row=r+2+len(self.all_paylines)+1, column=3, sticky="e", pady=(12, 0))

    def reset(self):
        if self.spinning:
            return
        self.credits.set(200)
        self.bet_per_line.set(2)
        self.active_lines.set(5)
        self._update_total_bet_label()
        self._reset_highlights()
        self._randomize_full_grid_from_strips()
        self.message.set("Press SPIN to play!")

    def confirm_reset(self):
        """Ask the user to confirm resetting the game."""
        if self.spinning:
            messagebox.showinfo("Please wait", "You can't reset while the reels are spinning.")
            return
        if messagebox.askyesno(
            "Confirm Reset",
            "Are you sure you want to reset?\n\n"
            "This will restore:\n"
            "• Credits to 200\n"
            "• Bet/Line to 2\n"
            "• Lines to 5\n"
            "and clear current highlights."
        ):
            self.reset()

    def confirm_quit(self):
        """Ask the user to confirm quitting the application."""
        if self.spinning:
            messagebox.showinfo("Please wait", "You can't quit while the reels are spinning.")
            return
        if messagebox.askyesno("Confirm Quit", "Are you sure you want to quit the slot machine?"):
            self.destroy()


if __name__ == "__main__":
    app = SlotMachineApp()
    app.mainloop()
