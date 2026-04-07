# 🚀🛸 DataMatrix — Module 09 👾

## 🎓👽 42 Python Module 09

> *Master the Art of Data Validation* 🌌

Welcome to **Cosmic Data Observatory** 🔭, a modular **Space Data Validation System** 🛰️ built entirely with Pydantic and advanced Python data modeling.

This module marks the transition from *writing basic classes* → to *enforcing data contracts*.

You are no longer just storing data.
You are **guaranteeing its integrity** ⭐.

---

# 🧠🌠 Overview

Imagine building the data backbone behind systems like:

* NASA mission control 🚀
* SETI signal monitoring 📡👽
* International Space Station telemetry 🛰️

Every piece of data must be valid, consistent, and trustworthy.

The challenge:
**How do we design a system that rejects bad data automatically, before it ever causes harm?** 👾

The answer:

## Pydantic Data Validation 🌌

This project builds a **layered validation architecture** using:

| Layer       | Purpose                                      |
| ----------- | -------------------------------------------- |
| Foundation  | Pydantic models with field constraints       |
| Logic       | Cross-field validation with model validators |
| Composition | Nested models and complex data structures    |
| Tooling     | Data generation and multi-format export      |

---

# 🎯🛸 Learning Goals

By completing this module you learn to:

* Use **Pydantic BaseModel** for data validation
* Define **field constraints** with `Field()`
* Use **Python Enums** for strict value sets
* Implement **`@model_validator`** for cross-field logic
* Compose **nested models**
* Handle and interpret **`ValidationError`**
* Generate and export realistic test datasets

This is production-grade data validation. 🌟

---

# 🧩👽 Core Concepts

## Pydantic BaseModel

Define **data contracts** that Python enforces automatically.

Example idea:

```
All space stations must have valid power and oxygen levels. 🛰️
All crew members must be within accepted age ranges. 👨‍🚀
```

## Field Constraints

Pydantic's `Field()` lets you set boundaries directly on the data:

```python
power_level: float = Field(..., ge=0.0, le=100.0)
crew_size: int     = Field(..., ge=1, le=20)
```

## Enums

Enums restrict values to a predefined set:

```python
class ContactType(str, Enum):
    radio      = "radio"
    visual     = "visual"
    physical   = "physical"
    telepathic = "telepathic"  # 👽🧠
```

## Model Validators

Cross-field logic that runs after all fields are validated:

```python
@model_validator(mode='after')
def validate_contact(self) -> 'AlienContact':
    if self.signal_strength > 7.0 and not self.message_received:
        raise ValueError("Strong signals should include a message")  # 📡👾
    return self
```

## Nested Models

One model can contain another:

```python
class SpaceMission(BaseModel):
    crew: List[CrewMember]  # 👨‍🚀🚀
```

---

# 🏗️🌌 Architecture

```
          ┌────────────────────────┐
          │   Data Export Layer    │ 📤
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │  Data Generator Layer  │ ⚙️
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │  Nested Model Layer    │ 🧩
          │     SpaceMission 🛸    │
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │  Cross-Field Logic     │ 🧠
          │     AlienContact 👽    │
          └───────────┬────────────┘
                      │
          ┌───────────▼────────────┐
          │   Foundation Layer     │ 🪐
          │     SpaceStation 🛰️   │
          └────────────────────────┘
```

Each exercise builds the next layer.

---

# 📦 Exercises Breakdown

---

# EX00 — Space Station 📡🛰️

## Goal

Create the **foundational Pydantic model** with field-level validation.

### Implement

* Class `SpaceStation`

### Model Fields

| Field              | Type             | Constraints              |
| ------------------ | ---------------- | ------------------------ |
| `station_id`       | `str`            | min 3, max 10 characters |
| `name`             | `str`            | min 1, max 50 characters |
| `crew_size`        | `int`            | 1 to 20                  |
| `power_level`      | `float`          | 0.0 to 100.0             |
| `oxygen_level`     | `float`          | 0.0 to 100.0             |
| `last_maintenance` | `datetime`       | required                 |
| `is_operational`   | `bool`           | default `True`           |
| `notes`            | `Optional[str]`  | max 200 characters       |

### Concepts

* `BaseModel` and `Field()`
* `Optional` fields with defaults
* `datetime` type parsing
* `ValidationError` handling

### Example Output

```
Space Station Data Validation 🛰️
========================================
Valid station created: ✅
ID: ISS001
Name: International Space Station
Crew: 6 people 👨‍🚀
Power: 85.5% ⚡
Oxygen: 92.3% 🌬️
Status: Operational 🟢
========================================
Expected validation error: ❌
Input should be less than or equal to 20
```

You define **the rules of the station** 🌌.

---

# EX01 — Alien Contact 👽🛸

## Goal

Implement **cross-field validation** using model validators and Enums.

### Implement

* Enum `ContactType`
* Class `AlienContact`

### Enum Values

```python
radio | visual | physical | telepathic 👾
```

### Model Fields

| Field              | Type             | Constraints          |
| ------------------ | ---------------- | -------------------- |
| `contact_id`       | `str`            | min 5, max 15 chars  |
| `timestamp`        | `datetime`       | required             |
| `location`         | `str`            | min 3, max 100 chars |
| `contact_type`     | `ContactType`    | valid enum value     |
| `signal_strength`  | `float`          | 0.0 to 10.0          |
| `duration_minutes` | `int`            | 1 to 1440            |
| `witness_count`    | `int`            | 1 to 100             |
| `message_received` | `Optional[str]`  | max 500 chars        |
| `is_verified`      | `bool`           | default `False`      |

### Cross-Field Rules

| Condition                    | Requirement                           |
| ---------------------------- | ------------------------------------- |
| `contact_id` format          | Must start with `"AC"` 🆔            |
| `contact_type == physical`   | `is_verified` must be `True` ✅      |
| `contact_type == telepathic` | `witness_count` must be ≥ 3 🧠👁️   |
| `signal_strength > 7.0`      | `message_received` must not be empty 📡|

### Example Output

```
Alien Contact Log Validation 👽📡
======================================
Valid contact report: ✅
ID: AC_2024_001
Type: radio 📻
Location: Area 51, Nevada 🌵
Signal: 8.5/10 📶
Duration: 45 minutes ⏱️
Witnesses: 5 👀
Message: 'Greetings from Zeta Reticuli' 🌌👾
======================================
Expected validation error: ❌
Telepathic contact requires at least 3 witnesses 🧠
```

You validate **the signal from beyond** 🌠👽.

---

# EX02 — Space Mission 🛸🚀

## Goal

Compose **nested models** and enforce complex multi-object validation.

### Implement

* Enum `Rank`
* Class `CrewMember`
* Class `SpaceMission`

### Rank Values

```python
cadet | officer | lieutenant | captain | commander 👨‍🚀
```

### CrewMember Fields

| Field              | Type     | Constraints          |
| ------------------ | -------- | -------------------- |
| `member_id`        | `str`    | min 3, max 10 chars  |
| `name`             | `str`    | min 2, max 50 chars  |
| `rank`             | `Rank`   | valid enum value     |
| `age`              | `int`    | 18 to 80             |
| `specialization`   | `str`    | min 3, max 30 chars  |
| `years_experience` | `int`    | 0 to 50              |
| `is_active`        | `bool`   | default `True`       |

### SpaceMission Fields

| Field             | Type               | Constraints         |
| ----------------- | ------------------ | ------------------- |
| `mission_id`      | `str`              | min 5, max 15 chars |
| `mission_name`    | `str`              | min 3, max 100 chars|
| `destination`     | `str`              | min 3, max 50 chars |
| `launch_date`     | `datetime`         | required            |
| `duration_days`   | `int`              | 1 to 3650           |
| `crew`            | `List[CrewMember]` | 1 to 12 members     |
| `mission_status`  | `str`              | default `"planned"` |
| `budget_millions` | `float`            | 1.0 to 10000.0      |

### Cross-Field Rules

| Condition                | Requirement                                        |
| ------------------------ | -------------------------------------------------- |
| `mission_id` format      | Must start with `"M"` 🆔                          |
| Crew composition         | At least one `captain` or `commander` required 🎖️ |
| `duration_days > 365`    | ≥ 50% of crew must have `years_experience >= 5` ⭐ |
| All crew members         | `is_active` must be `True` ✅                     |

### Example Output

```
Space Mission Crew Validation 🛸👨‍🚀
=========================================
Valid mission created: ✅
Mission: Mars Colony Establishment 🪐
ID: M2024_MARS
Destination: Mars 🔴
Duration: 900 days ⏳
Budget: $2500.0M 💰
Crew size: 3 👨‍🚀
Crew members:
- Sarah Connor (commander) 🎖️ - Mission Command
- John Smith (lieutenant) ⭐ - Navigation
- Alice Johnson (officer) 🔧 - Engineering
=========================================
Expected validation error: ❌
Mission must have at least one Commander or Captain 🎖️
```

You assemble **the crew that will reach the stars** 🌟🚀.

---

# 🛠️⚙️ Utility Files

Two helper files are provided at the root level:

### `data_generator.py` 🤖

Generates realistic test data for all three model types:

| Generator               | Produces              |
| ----------------------- | --------------------- |
| `SpaceStationGenerator` | Space station records 🛰️ |
| `AlienContactGenerator` | Contact log entries 👽 |
| `CrewMissionGenerator`  | Full mission payloads 🚀 |

Run standalone:

```bash
python data_generator.py
```

### `data_exporter.py` 📤

Exports generated data in multiple formats:

| Format  | Use case                 |
| ------- | ------------------------ |
| `.json` | API testing & sharing    |
| `.csv`  | Spreadsheet analysis     |
| `.py`   | Direct Python import     |

Run standalone:

```bash
python data_exporter.py
```

---

# 📁 Repository Structure

```
python09/ 🛸
│
├── data_generator.py 🤖
├── data_exporter.py 📤
│
├── ex0/ 🛰️
│   └── space_station.py
│
├── ex1/ 👽
│   └── alien_contact.py
│
└── ex2/ 🚀
    └── space_crew.py
```

---

# ▶️ How to Run

```bash
# Install dependency
pip install pydantic

# EX00 🛰️
python ex0/space_station.py

# EX01 👽
python ex1/alien_contact.py

# EX02 🚀
python ex2/space_crew.py

# Utilities ⚙️
python data_generator.py
python data_exporter.py
```

---

# 🧪🌌 Example Features Demonstrated

* Creating valid and invalid Pydantic models ✅❌
* Field-level constraint enforcement 🔒
* Enum-restricted fields 🗂️
* Cross-field business logic with `@model_validator` 🧠
* Nested model composition (`SpaceMission` contains a `List[CrewMember]`) 🛸👨‍🚀
* Graceful `ValidationError` parsing and display ⚠️
* Generating randomized but rule-compliant test datasets 🤖
* Exporting data to JSON, CSV, and importable Python files 📤

---

# 🧑‍🏫 Evaluation Tips

You WILL be asked about:

### Pydantic Basics 🔩

* What is a `BaseModel` and why use it over a plain class?
* What does `Field(...)` mean — what does `...` (Ellipsis) signify?
* What is the difference between a required and an optional field?

### Validation ✅

* What is a `ValidationError` and when is it raised?
* How do you access individual errors from a `ValidationError`?
* What is the difference between field-level and model-level validation?

### Model Validators 🧠

* When does `@model_validator(mode='after')` run?
* Why can't a field constraint handle cross-field rules?

### Enums 🗂️

* Why use a `str, Enum` instead of a plain string field?
* What happens if an invalid enum value is provided?

### Nested Models 🧩

* How does Pydantic validate a `List[CrewMember]` field?
* What happens if one crew member in a list is invalid?

If you understand the data contracts → you control the mission 🚀🌌.

---

# 💡🌟 Final Thoughts

This module teaches **real-world data integrity** 🛡️.

You didn't just write models.
You designed a **validation system** that rejects bad data at the boundary 🌌👾.

You are now thinking like a **backend engineer** 👨‍💻🚀.