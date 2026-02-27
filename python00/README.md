# 🌱 Growing Code — Module 00

> **Python Fundamentals Through Garden Data**  
> *42 Network — Python Cursus*

---

## 📖 About

**Growing Code** is the introductory module of the 42 Python cursus. It teaches Python's core building blocks — expressions, variables, functions, and control flow — through a real-world community garden data context.

Each exercise is self-contained, progressively introducing new concepts while keeping the theme consistent and engaging.

---

## 🗂️ Project Structure

```
module00/
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_plot_area.py
├── ex2/
│   └── ft_harvest_total.py
├── ex3/
│   └── ft_plant_age.py
├── ex4/
│   └── ft_water_reminder.py
├── ex5/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
├── ex6/
│   └── ft_garden_summary.py
└── ex7/
    └── ft_seed_inventory.py
```

---

## 📋 Exercises Overview

| Exercise | File(s) | Concept |
|----------|---------|---------|
| **Ex00** — Hello Garden | `ft_hello_garden.py` | First function, `print()` |
| **Ex01** — Garden Plot Area | `ft_plot_area.py` | Variables, arithmetic, `input()` |
| **Ex02** — Harvest Total | `ft_harvest_total.py` | Multiple inputs, addition |
| **Ex03** — Plant Age Check | `ft_plant_age.py` | Conditionals (`if/else`) |
| **Ex04** — Water Reminder | `ft_water_reminder.py` | Conditionals with comparison |
| **Ex05** — Count to Harvest | `ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py` | Loops & recursion |
| **Ex06** — Garden Summary | `ft_garden_summary.py` | String formatting, multiple data types |
| **Ex07** — Seed Inventory | `ft_seed_inventory.py` | Type annotations, match/conditional logic |

---

## 🔧 Technical Requirements

- **Language:** Python 3.10+
- **Linting:** All code must pass `flake8` standards
- **Structure:** Each exercise lives in its own file, containing **only** the requested function — no `if __name__ == "__main__":` blocks, no direct calls

---

## 📝 Exercise Details

### Ex00 — Hello Garden
```python
ft_hello_garden()
# Output: Hello, Garden Community!
```
Authorized: `print()`

---

### Ex01 — Garden Plot Area
```python
ft_plot_area()
# Enter length: 5
# Enter width: 3
# Output: Plot area: 15
```
Authorized: `input()`, `int()`, `print()`

---

### Ex02 — Harvest Total
```python
ft_harvest_total()
# Day 1 harvest: 5
# Day 2 harvest: 8
# Day 3 harvest: 3
# Output: Total harvest: 16
```
Authorized: `input()`, `int()`, `print()`

---

### Ex03 — Plant Age Check
```python
ft_plant_age()
# Enter plant age in days: 75
# Output: Plant is ready to harvest!   (if age > 60)

ft_plant_age()
# Enter plant age in days: 45
# Output: Plant needs more time to grow.
```
Authorized: `input()`, `int()`, `print()`

---

### Ex04 — Water Reminder
```python
ft_water_reminder()
# Days since last watering: 4
# Output: Water the plants!   (if days > 2)

ft_water_reminder()
# Days since last watering: 1
# Output: Plants are fine
```
Authorized: `input()`, `int()`, `print()`

---

### Ex05 — Count to Harvest (Iterative & Recursive)
```python
ft_count_harvest_iterative()
# Days until harvest: 5
# Day 1 ... Day 5
# Output: Harvest time!
```
Two separate implementations required — one using a loop, one using recursion.  
Authorized: `input()`, `int()`, `print()`, `range()`

---

### Ex06 — Garden Summary
```python
ft_garden_summary()
# Enter garden name: Community Garden
# Enter number of plants: 25
# Garden: Community Garden
# Plants: 25
# Status: Growing well!
```
Authorized: `input()`, `print()`  
> Note: `"Status: Growing well!"` is a **fixed** string — always print exactly that.

---

### Ex07 — Seed Inventory with Type Annotations
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```
```python
ft_seed_inventory("tomato", 15, "packets")
# Output: Tomato seeds: 15 packets available

ft_seed_inventory("carrot", 8, "grams")
# Output: Carrot seeds: 8 grams total

ft_seed_inventory("lettuce", 12, "area")
# Output: Lettuce seeds: covers 12 square meters
```
Supported units: `"packets"`, `"grams"`, `"area"`. Any other unit prints `Unknown unit type`.  
Authorized: `print()`

---

## 🚀 Usage & Testing

A `main.py` helper is provided to import and test all functions:

```bash
# Place main.py in the same directory as your exercise folders, then:
python3 main.py
```

To manually test a single function:

```bash
cd ex0/
python3 -c "from ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

To check linting:

```bash
flake8 ft_hello_garden.py
```

---

## ⚠️ Important Rules

- Write **only** the function — no main program, no direct calls at module level
- Function names must match **exactly** as specified
- You do **not** need to handle invalid or negative inputs (behavior is undefined)
- Type hints are optional for ex00–ex06, **required** for ex07

---

## 🤖 AI Usage Policy

AI tools are **permitted** with the following rules:

- ✅ Use AI to explore concepts and reduce tedious tasks
- ✅ Only submit code you **fully understand** and can explain
- ❌ Do not copy-paste AI output blindly
- ❌ During peer evaluation, you will be asked to explain every line

> Peer review is essential — AI lacks your specific context. Use your peers as a quality checkpoint.

---

## 📦 Submission

Submit all files via your **Git repository**. Only files tracked in the repo will be evaluated.

Files to submit:
- `ex0/ft_hello_garden.py`
- `ex1/ft_plot_area.py`
- `ex2/ft_harvest_total.py`
- `ex3/ft_plant_age.py`
- `ex4/ft_water_reminder.py`
- `ex5/ft_count_harvest_iterative.py`
- `ex5/ft_count_harvest_recursive.py`
- `ex6/ft_garden_summary.py`
- `ex7/ft_seed_inventory.py`

---

*"Programming, like gardening, is about nurturing growth — both in code and in the communities we serve."*
