# PLP-Python_wk_5

# 🏗️ Activity 1 & 🎭 Activity 2 – Object-Oriented Programming in Python

This repository contains Python programs that demonstrate **Object-Oriented Programming (OOP)** concepts such as:

- Classes & Objects
- Attributes & Methods
- Constructors (`__init__`)
- Inheritance
- Encapsulation
- Polymorphism

---

## 📌 Activity 1: Design Your Own Class

We designed a `Smartphone` class and extended it into a `GamingPhone` class to explore **inheritance** and **encapsulation**.

### Features

- Create a smartphone with brand, model, storage, and battery.
- Make calls and charge the phone.
- Extend to `GamingPhone` with additional features (GPU power + play games).

### Example

```python
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
print(phone1)              # Shows phone info
phone1.call("08065589988") # Makes a call
phone1.charge(15)          # Charges battery

gaming_phone = GamingPhone("Redmi MI", "Note 13", 256, 50, "Adreno 610")
gaming_phone.play_game("PUBG Mobile")
```
