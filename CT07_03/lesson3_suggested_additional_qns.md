
## 1) Firecracker Countdown (timing + while)

Simulate a firecracker countdown from a user-given number `n` to 0.

**Requirements**

* Use a `while` loop to count down.
* Print `T-<n>` every second.
* Use `time.sleep(1)`.
* When it reaches 0, print `"POP! 新年快乐!"`.

---

## 2) Ang Bao Luck Meter (random.random + thresholds)

Every second, generate a “luck value” between 0 and 1 using `random.random()`.

**Requirements**

* Run a `while` loop until luck value ≥ 0.95.
* Print the value to 3 decimal places each second.
* `sleep(1)` each loop.
* At the end, print how many tries it took.

---

## 3) Lion Dance Drum Combo (random.randint + while)

A lion dance needs a specific 3-beat combo: **8, 8, 6**.

**Requirements**

* Every 0.5 seconds, generate a beat `1–9` using `random.randint(1, 9)`.
* Keep printing beats.
* Stop only when the **last three beats** match `8, 8, 6`.
* Print total beats played.

*(This tests maintaining “last 3 values” in variables without lists.)*

---

## 4) ⭐ Algorithm: “Most Common Mandarin Orange” (mode, counting)

You are packing mandarin oranges. Each orange has a size rating from 1 to 5.

**Requirements**

* Generate 50 oranges using `random.randint(1, 5)`.
* Use a `while` loop to count how many of each size appeared.
* At the end, print the size with the **highest count** (mode).
* If tie, pick the **smaller size**.

*(Algorithm: frequency counting + max selection.)*

---

## 5) Lantern Festival “Even Only” Gate (loop control)

You want to light **10 lanterns**, but only even-numbered lantern IDs are allowed.

**Requirements**

* Randomly generate lantern ID from 1–20.
* If it’s even: count it as “lit” and print it.
* If it’s odd: print “skipped”.
* Stop when you have lit **10** even IDs.
* Add a tiny delay `sleep(0.2)` to see it run.

---

## 6) Reunion Dinner Queue Simulator (sleep + random.randint)

Customers arrive at a bak kwa stall.

**Rules**

* Start with `queue = 0`
* Every second:

  * `arrive = randint(0, 3)` people join
  * `serve = randint(0, 2)` people are served
* Queue cannot go below 0.

**Requirements**

* Use a `while` loop until queue reaches **20 or more**.
* Print queue size each second.

*(Tests clamping to 0 and state updates.)*

---

## 7) ⭐ Algorithm: “Lucky Number Search” (random search + stopping)

Your lucky number is given by the user (1–100).

**Requirements**

* Use a `while` loop to keep generating guesses with `randint(1,100)`.
* Stop when the guess matches the lucky number.
* Print each guess, and how many tries it took.
* Also print whether tries was “fast” (≤20) or “slow” (>20).

*(Algorithm: randomized search + counting + categorizing.)*

---

## 8) CNY Slot Machine: 财神 Jackpot (random.random + probability)

Simulate a 财神 slot pull each second.

**Rules**

* Generate `r = random.random()`
* If `r < 0.70`: “Small luck”
* Else if `r < 0.95`: “Good luck”
* Else: “JACKPOT!”

**Requirements**

* Keep pulling until JACKPOT happens.
* Print the category each second.
* Count how many of each category occurred.

---

## 9) ⭐ Algorithm: “Longest Streak of Red Packets” (streak tracking)

Each second, a person gives you an ang bao or not:

* `randint(0,1)` where 1 means received.

**Requirements**

* Run for exactly 60 seconds (60 iterations with `sleep(1)`).
* Track:

  * current streak of 1s
  * longest streak of 1s
* Print longest streak at the end.

*(Algorithm: classic longest-streak tracking.)*

---

## 10) Fireworks Safety Limit (while + “break” logic)

Fireworks have a safety meter starting at 0.

**Rules each loop**

* Add `randint(5, 20)` to meter
* Subtract `randint(0, 10)` (wind reduces danger)
* Meter cannot go below 0

**Requirements**

* Every 0.3 seconds, print meter.
* Stop when meter reaches **100 or more** (too dangerous) and print `"STOP SHOW!"`.
* Also print total loops taken.

---