# Collatz Conjecture — Python Implementation

A clean Python implementation of the **Collatz Conjecture** (also known as the 3n+1 problem), one of the most famous unsolved problems in mathematics.

## 📖 What is the Collatz Conjecture?

Take any positive integer. Apply these two rules repeatedly:

- If the number is **even** → divide it by 2
- If the number is **odd** → multiply by 3 and add 1

The conjecture claims: **no matter what number you start with, you will always eventually reach 1.**

### Example — starting with 6:
```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1  (8 steps)
```

### Example — starting with 27:
```
27 → 82 → 41 → 124 → ... → 9232 → ... → 1  (111 steps, peak: 9232!)
```

Despite being easy to explain, **this has never been mathematically proven for all positive integers.**

---

## 🚀 How to Run

No external libraries needed — just Python 3.

```bash
python collatz.py
```

You'll be prompted to enter a number:
```
Enter a positive integer to start: 27
Starting value: 27
Step 1: 27 is odd. Formula: (3 * 27) + 1 = 82
Step 2: 82 is even. Formula: 82 / 2 = 41
...
Process finished. Total steps taken: 111
```

---

## 📁 Project Structure

```
collatz-conjecture/
│
├── collatz.py          # Main implementation
├── NOTES.md            # My personal research notes and impressions  ← ADD YOUR WRITING HERE
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

---

## 🧠 My Notes

See [`NOTES.md`](./NOTES.md) for my personal research, observations, and impressions while working on this project.

---

## 🔬 Interesting Facts

- The conjecture has been verified for all numbers up to **2⁶⁸** (about 295 quintillion)
- The number **27** is famous — it takes 111 steps and shoots up to **9,232** before coming back down
- Powers of 2 are the simplest case: they drop straight to 1 with no odd steps
- It was proposed by **Lothar Collatz** in 1937 and remains unsolved today

---

## 📚 Resources

- [Collatz Conjecture — Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [Veritasium video: "The Simplest Math Problem No One Can Solve"](https://www.youtube.com/watch?v=094y1Z2wpJg)
- [OEIS A006577](https://oeis.org/A006577) — number of steps to reach 1

---

## 👤 Author

**Alisher** — Cybersecurity student and Junior pentester

> This project is part of my ongoing journey documenting math and security concepts through code.
