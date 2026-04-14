# 🧙‍♂️⚡ FuncMage — Module 10 🔮

## 🎓🌌 42 Python Module 10

> *Master the Ancient Arts of Functional Programming* ✨

Welcome to **FuncMage Chronicles** 🏰, a modular **Functional Programming Mastery System** 🗡️ built entirely with Python's higher-order functions, closures, decorators, and the `functools` module.

This module marks the transition from *writing standard classes* → to *wielding the arcane arts of functional design*.

You are no longer just defining functions.
You are **composing elegant, reusable spells** ⭐.

---

# 🧠🌠 Overview

Imagine building the logic engine behind systems like:

* Spell-casting engines 🔮
* Enchantment validation pipelines ⚔️
* Mage guild management systems 🏰

Every function must be composable, pure, and trustworthy.

The challenge:
**How do we design a system where functions transform, wrap, and generate other functions automatically?** 👾

The answer:

## Functional Programming 🌌

This project builds a **layered functional architecture** using:

| Layer        | Purpose                                              |
| ------------ | ---------------------------------------------------- |
| Lambda       | Anonymous functions and data transformations         |
| Higher-Order | Functions that accept and return other functions     |
| Closures     | Lexical scoping and persistent state without globals |
| Functools    | `reduce`, `partial`, `lru_cache`, `singledispatch`   |
| Decorators   | Function wrappers with `@staticmethod` and `@wraps`  |

---

# 🎯🛸 Learning Goals

By completing this module you learn to:

* Use **lambda expressions** for concise anonymous transformations
* Apply **`map()`**, **`filter()`**, and **`sorted()`** with lambdas
* Build **higher-order functions** that accept and return callables
* Understand **lexical scoping** and create stateful **closures**
* Leverage **`functools`** (`reduce`, `partial`, `lru_cache`, `singledispatch`)
* Create **parameterized decorators** with `functools.wraps`
* Implement **`@staticmethod`** and understand its purpose in classes
* Handle errors **gracefully** inside functional pipelines

This is production-grade functional Python. 🌟

---

# 🧩👽 Core Concepts

## Lambda Expressions

Concise, inline anonymous functions for quick transformations:

```python
sorted(artifacts, key=lambda a: a["power"], reverse=True)
list(filter(lambda m: m["power"] >= min_power, mages))
list(map(lambda s: f"* {s} *", spells))
```

## Higher-Order Functions

Functions that take or return other functions:

```python
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified
```

## Closures & Lexical Scoping

Functions that capture and remember their creation environment:

```python
def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter
```

## Functools Arsenal

```python
functools.reduce(operator.add, spells)          # aggregate
functools.partial(enchant, power=50, element='fire')  # specialize
@functools.lru_cache(maxsize=None)              # memoize
@functools.singledispatch                       # type dispatch
```

## Decorators

Wrappers that enhance functions transparently:

```python
def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func()
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        return result
    return wrapper
```

---

# 🏗️🌌 Architecture

```
          ┌────────────────────────┐
          │   Decorator Layer      │ 🎭
          │   decorator_mastery.py │
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │   Functools Layer      │ ⚙️
          │  functools_artifacts.py│
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │   Closure Layer        │ 🔒
          │   scope_mysteries.py   │
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │  Higher-Order Layer    │ 🧠
          │    higher_magic.py     │
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │   Lambda Layer         │ λ
          │   lambda_spells.py     │
          └────────────────────────┘
```

Each exercise builds on the previous layer.

---

# 📦 Exercises Breakdown

---

# EX00 — Lambda Sanctum λ✨

## Goal

Master **anonymous functions** using lambda expressions with `map`, `filter`, and `sorted`.

### Implement

* Functions in `lambda_spells.py`

### Functions

| Function            | Description                                      |
| ------------------- | ------------------------------------------------ |
| `artifact_sorter`   | Sort artifacts by `power` descending via lambda  |
| `power_filter`      | Filter mages with `power >= min_power` via lambda|
| `spell_transformer` | Add `"* "` prefix and `" *"` suffix via `map`   |
| `mage_stats`        | Compute max, min, avg power with lambdas         |

### Concepts

* `lambda` expressions
* `sorted()`, `filter()`, `map()` with anonymous functions
* `max()`, `min()`, `sum()` with lambdas
* Returning plain collections from functional pipelines

### Example Output

```
Testing artifact sorter...
Storm Crown (111 power) comes before Lightning Rod (109 power)

Testing spell transformer...
* blizzard * * meteor * * lightning * * earthquake *

Testing mage stats...
Max: 91, Min: 51, Avg: 63.6
```

You sort, filter, and transform **data the functional way** 🌌.

---

# EX01 — Higher Realm 🔮⚔️

## Goal

Create **higher-order functions** — functions that accept and return other callables.

### Implement

* Functions in `higher_magic.py`

### Functions

| Function             | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `spell_combiner`     | Returns a function calling both spells, result as tuple  |
| `power_amplifier`    | Returns a function multiplying the spell's result        |
| `conditional_caster` | Returns a function that casts only if condition is true  |
| `spell_sequence`     | Returns a function casting all spells in order           |

### Concepts

* Functions as first-class citizens
* Returning inner functions (closures)
* Function composition and combination
* Using `*args` and `**kwargs` for flexible wrappers

### Example Output

```
Testing spell combiner...
Combined spell result: Fireball hits Dragon for 10 damage, Heals Dragon for 10 health

Testing power amplifier...
Original: 10, Amplified: 30
Fireball hits Dragon for 10 damage
Fireball hits Dragon for 30 damage

Testing conditional caster...
Fireball hits Dragon for 25 damage
Spell fizzled
```

You build **functions that forge other functions** 🧠.

---

# EX02 — Memory Depths 🌊🔒

## Goal

Understand **lexical scoping** and implement **closures** that preserve state without global variables.

### Implement

* Functions in `scope_mysteries.py`

### Functions

| Function               | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `mage_counter`         | Returns a closure that counts how many times it's called |
| `spell_accumulator`    | Returns a closure accumulating power from a base value |
| `enchantment_factory`  | Returns a closure applying a specific enchantment type |
| `memory_vault`         | Returns a dict with `store`/`recall` closures          |

### Concepts

* `nonlocal` keyword for mutable closure state
* Factory functions creating specialized closures
* Private state encapsulated in closures
* Multiple closures sharing the same enclosing scope

### Example Output

```
Testing mage counter...
counter_a call 1: 1
counter_a call 2: 2
counter_b call 1: 1

Testing enchantment factory...
Flaming Sword
Frozen Shield

Testing memory vault...
Store 'secret' = 42
Recall 'secret': 42
Recall 'unknown': Memory not found
```

You capture **the environment itself inside a function** 🔒.

---

# EX03 — Ancient Library 📚⚗️

## Goal

Wield the **`functools` module** — reduce, partial application, memoization, and single dispatch.

### Implement

* Functions in `functools_artifacts.py`

### Functions

| Function              | Description                                              |
| --------------------- | -------------------------------------------------------- |
| `spell_reducer`       | Uses `functools.reduce` + `operator` for aggregation     |
| `partial_enchanter`   | Uses `functools.partial` to create specialized callables |
| `memoized_fibonacci`  | Uses `@functools.lru_cache` for cached recursion         |
| `spell_dispatcher`    | Uses `@functools.singledispatch` for type-based routing  |

### Supported Operations for `spell_reducer`

```
"add" | "multiply" | "max" | "min"
```

### Concepts

* `functools.reduce` for data aggregation
* `functools.partial` for pre-filling function arguments
* `functools.lru_cache` for transparent memoization
* `functools.singledispatch` for type-based polymorphism
* `operator` module (`operator.add`, `operator.mul`)

### Example Output

```
Testing spell reducer...
Sum: 100
Product: 240000
Max: 40

Testing partial enchanter...
Fire enchantment (50 power) on Dragon Sword
Ice enchantment (50 power) on Dragon Sword
Lightning enchantment (50 power) on Dragon Sword

Testing memoized fibonacci...
Fib(0): 0
Fib(1): 1
Fib(10): 55
Fib(15): 610

Testing spell dispatcher...
Damage spell: 42 damage
Enchantment: fireball
Multi-cast: 3 spells
Unknown spell type
```

You leverage **the full power of the functools arsenal** ⚗️.

---

# EX04 — Master's Tower 🏰🎭

## Goal

Create **decorators** — parameterized and plain — and demonstrate `@staticmethod` in a class.

### Implement

* Decorators and class in `decorator_mastery.py`

### Decorators & Class

| Component          | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `spell_timer`      | Measures and prints execution time, preserves metadata        |
| `power_validator`  | Parameterized decorator that blocks calls below min power     |
| `retry_spell`      | Retries a failing function up to `max_attempts` times         |
| `MageGuild`        | Class with `@staticmethod` `validate_mage_name` + `cast_spell`|

### Cross-Cutting Rules

| Decorator         | Requirement                                          |
| ----------------- | ---------------------------------------------------- |
| `spell_timer`     | Must use `functools.wraps` 🔧                        |
| `power_validator` | Checks first `int` arg or `power` kwarg 🔋           |
| `retry_spell`     | Prints retry messages, returns failure string ⚠️     |
| `cast_spell`      | Decorated with `@power_validator(min_power=10)` ✅   |

### Concepts

* Decorator factories (decorators with arguments)
* `functools.wraps` for preserving `__name__`, `__doc__`
* `@staticmethod` — class-level utility without `self`
* Exception handling inside retry wrappers
* Separation of concerns via decoration

### Example Output

```
Testing spell timer...
Casting fireball...
Spell completed in 0.101 seconds
Result: Fireball cast!

Testing retrying spell...
Spell failed, retrying... (attempt 1/3)
Spell failed, retrying... (attempt 2/3)
Spell casting failed after 3 attempts

Testing MageGuild...
True
False
Successfully cast Lightning with 15 power
Insufficient power for this spell
```

You become the **architect of function behavior itself** 🏰.

---

# 📁 Repository Structure

```
p10/ 🧙‍♂️
│
├── ex0/ λ
│   └── lambda_spells.py
│
├── ex1/ 🔮
│   └── higher_magic.py
│
├── ex2/ 🌊
│   └── scope_mysteries.py
│
├── ex3/ 📚
│   └── functools_artifacts.py
│
└── ex4/ 🏰
    └── decorator_mastery.py
```

---

# ▶️ How to Run

```bash
# No external dependencies needed — stdlib only ✅

# EX00 λ
python3 ex0/lambda_spells.py

# EX01 🔮
python3 ex1/higher_magic.py

# EX02 🌊
python3 ex2/scope_mysteries.py

# EX03 📚
python3 ex3/functools_artifacts.py

# EX04 🏰
python3 ex4/decorator_mastery.py
```

---

# 🧪🌌 Example Features Demonstrated

* Anonymous transformations with **lambda** in `sorted`, `filter`, `map` ✅
* Building **higher-order functions** that compose behavior 🔮
* Stateful **closures** using `nonlocal` without global variables 🔒
* Data aggregation with **`functools.reduce`** + `operator` module ⚙️
* Argument pre-filling with **`functools.partial`** 🎯
* Transparent caching with **`functools.lru_cache`** ⚡
* Type-based routing with **`functools.singledispatch`** 🗂️
* Plain and **parameterized decorators** with `functools.wraps` 🎭
* Class utility methods via **`@staticmethod`** 🏰
* Graceful **exception handling** inside retry and validation wrappers ⚠️

---

# 🧑‍🏫 Evaluation Tips

You WILL be asked about:

### Lambda & Builtins 🔩

* When should you use `lambda` vs a named `def`?
* What is the difference between `map`, `filter`, and a list comprehension?
* Why does `sorted()` accept a `key` argument instead of comparing directly?

### Higher-Order Functions 🔮

* What does it mean for a function to be a "first-class citizen" in Python?
* How does returning an inner function differ from calling it directly?
* What is function composition, and why is it useful?

### Closures & Scoping 🌊

* What is lexical scoping, and how does Python implement it?
* When and why do you need the `nonlocal` keyword?
* How does a closure differ from a class when managing state?

### Functools ⚙️

* What does `functools.reduce` do, and when is it better than a loop?
* How does `functools.partial` differ from calling a function with defaults?
* What are the performance benefits of `lru_cache`?
* How does `singledispatch` enable type-based polymorphism without `if/isinstance`?

### Decorators 🎭

* Explain the three-layer structure of a parameterized decorator.
* Why is `functools.wraps` important when writing decorators?
* What is the difference between `@staticmethod` and a regular instance method?
* How do decorators enable separation of concerns?

If you understand function transformation → you control the magic 🔮🌌.

---

# 💡🌟 Final Thoughts

This module teaches **real-world functional design** 🛡️.

You didn't just write functions.
You designed a **system where functions build, wrap, and enhance other functions** 🌌👾.

You are now thinking like a **software architect** 👨‍💻🧙‍♂️.
