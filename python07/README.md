# 🃏 DataDeck — Module 07

## 🎓 42 Python Module 07

> *Master the Art of Abstract Programming Patterns*

Welcome to **DataDeck**, a modular **Trading Card Game Engine** built entirely with advanced Object-Oriented Programming in Python.

This module marks the transition from *writing classes* → to *designing architectures*.

You are no longer just coding.
You are designing **extensible systems**.

---

# 📚 Table of Contents

* Overview
* Learning Goals
* Core Concepts
* Project Architecture
* Exercises Breakdown
* Repository Structure
* How to Run
* Example Outputs
* Evaluation Tips

---

# 🧠 Overview

Imagine building the engine behind games like:

* Magic The Gathering
* Hearthstone
* Pokémon TCG

Thousands of card types must interact consistently.

The challenge:
**How do we design a system flexible enough to support infinite card types without rewriting the engine?**

The answer:

## Abstract Programming Patterns

This project builds a **layered architecture** using:

| Layer          | Purpose                           |
| -------------- | --------------------------------- |
| Foundation     | Abstract base classes             |
| Implementation | Concrete card types               |
| Ability Layer  | Interfaces & multiple inheritance |
| Engine         | Strategy + Abstract Factory       |
| Platform       | Tournament system                 |

---

# 🎯 Learning Goals

By completing this module you learn to:

* Use **Abstract Base Classes (ABC)**
* Implement **Polymorphism**
* Design **Interfaces**
* Use **Multiple Inheritance**
* Implement **Design Patterns**

  * Abstract Factory
  * Strategy Pattern
* Build **Extensible Architectures**

This is enterprise-level OOP.

---

# 🧩 Core Concepts

## Abstract Base Classes

Define **contracts** that all subclasses must follow.

Example idea:

```
All cards must be playable.
All cards must provide info.
```

## Interfaces

Interfaces add **optional abilities** to classes.

Examples:

* Combatable → can attack
* Magical → can cast spells
* Rankable → can be ranked

## Polymorphism

Different card types share the same interface:

```
deck.draw_card().play()
```

The deck doesn’t care what type of card it draws.

## Design Patterns Used

| Pattern               | Where                    |
| --------------------- | ------------------------ |
| Abstract Factory      | Card creation            |
| Strategy              | Game behavior            |
| Interface Composition | Elite & Tournament cards |

---

# 🏗️ Architecture

```
          ┌────────────────────┐
          │   Tournament Layer │
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │     Game Engine     │
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │   Ability System    │
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │ Implementation Layer│
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │   Foundation Layer  │
          └────────────────────┘
```

Each exercise builds the next layer.

---

# 📦 Exercises Breakdown

---

# EX00 — Card Foundation 🃏

## Goal

Create the **universal blueprint** for all cards.

### Implement

* Abstract class `Card`
* Concrete class `CreatureCard`

### Concepts

* ABC module
* Abstract methods
* Validation
* Basic polymorphism

### Key Methods

```
play()
get_card_info()
is_playable()
attack_target()
```

You create the **first playable card**.

---

# EX01 — Deck Builder 🗂️

## Goal

Create multiple card types & a deck manager.

### New Card Types

* SpellCard → instant effects
* ArtifactCard → permanent effects

### Deck System

```
add_card()
remove_card()
shuffle()
draw_card()
get_deck_stats()
```

### Concepts

* Polymorphism in action
* Managing heterogeneous collections

Your deck now supports **any card type**.

---

# EX02 — Ability System ⚔️✨

## Goal

Implement **interfaces + multiple inheritance**

### Interfaces

| Interface  | Ability            |
| ---------- | ------------------ |
| Combatable | Attack / Defend    |
| Magical    | Cast spells / Mana |

### New Class

```
EliteCard = Card + Combatable + Magical
```

This is where the architecture becomes powerful.

---

# EX03 — Game Engine 🧠

## Goal

Implement **Design Patterns**

### Strategy Pattern

Controls how a turn is played.

Example:

```
AggressiveStrategy → attack first
```

### Abstract Factory

Creates themed cards dynamically.

Example:

```
FantasyCardFactory → dragons, goblins, spells
```

### GameEngine

Orchestrates everything.

This is the **brain** of DataDeck.

---

# EX04 — Tournament Platform 🏆

## Goal

Combine everything into a ranking system.

### New Interface

```
Rankable
```

### New Classes

* TournamentCard
* TournamentPlatform

Features:

* Register cards
* Create matches
* Leaderboards
* Tournament reports

You built a **complete ecosystem**.

---

# 📁 Repository Structure

```
python07/
│
├── __init__.py
│
├── ex0/
├── ex1/
├── ex2/
├── ex3/
└── ex4/
```

⚠️ Absolute imports required:

```
from ex0.Card import Card
```

Run from repo root:

```
python3 -m exN.main
```

---

# ▶️ How to Run

```
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
```

---

# 🧪 Example Features Demonstrated

* Creating cards dynamically
* Playing cards with mana cost
* Deck polymorphism
* Multi-ability cards
* Strategy-driven turns
* Tournament ranking system

---

# 🧑‍🏫 Evaluation Tips

You WILL be asked about:

### Abstract Classes

* Why use them?
* What happens if abstract methods aren't implemented?

### Interfaces

* Why separate combat & magic?

### Multiple Inheritance

* Benefits vs composition

### Strategy Pattern

* Why not hardcode behavior?

### Abstract Factory

* Why create objects through factories?

If you understand the architecture → you pass easily.

---

# 💡 Final Thoughts

This module teaches **real software architecture**.

You didn’t just write classes.
You designed a **scalable engine**.

You are now thinking like a **software architect**.
