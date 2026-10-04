---
title: "OSC++.019: Pure Virtual Functions and Abstract Classes"
status: published
wordpress_post_id: 20424
published: "2026-10-04T00:34:46"
live_url: "https://bitcoinversus.tech/2026/10/04/oscpp-019-pure-virtual-functions-abstract-classes/"
series: "Open-Source C++"
pathway: cpp
lesson_number: "019"
featured_media_id: 20423
featured_image_url: "https://bitcoinversus.wordpress.com/wp-content/uploads/2026/10/osc.019-abstract-classes-and-pure-virtual-functions-cover.png"
youtube_1: "https://www.youtube.com/watch?v=XNHSSduMBbY"
youtube_2: "https://www.youtube.com/watch?v=rECcII1Mdfc"
youtube_3: "https://www.youtube.com/watch?v=mvTo_zpr9oA"
---

# OSC++.019: Pure Virtual Functions and Abstract Classes

A pure virtual function says that every concrete derived class must provide the required behavior. A class that still has an unimplemented pure virtual function is abstract and cannot be instantiated.

This lesson continues from [OSC++.018: Virtual Functions and Polymorphism Basics](https://bitcoinversus.tech/2026/10/03/oscpp-018-virtual-functions-polymorphism-basics/).

## The syntax to recognize

```cpp
virtual void run() = 0;
```

The `= 0` is the pure specifier. It turns the virtual member into a **pure virtual function**.

According to [cppreference](https://en.cppreference.com/w/cpp/language/abstract_class), an abstract class cannot be instantiated but can be used as a base class. [Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/abstract-classes-cpp?view=msvc-170) likewise documents that pointers and references to abstract types are allowed even though objects of the abstract type itself are not.

## Smallest useful example

```cpp
#include <iostream>

class Machine {
public:
    virtual void start() = 0;
};

class Miner : public Machine {
public:
    void start() override {
        std::cout << "Miner starting\n";
    }
};

int main() {
    Miner s21;
    s21.start();
}
```

Output:

```text
Miner starting
```

`Machine` defines the contract. `Miner` supplies the concrete behavior.

## Video 1 — Pure virtual functions and abstract classes

https://www.youtube.com/watch?v=XNHSSduMBbY

ProgrammingKnowledge introduces pure virtual functions and abstract classes in C++.

## Abstract classes cannot be instantiated

```cpp
Machine machine;  // compile-time error
```

But an abstract base reference can refer to a concrete derived object:

```cpp
Miner s21;
Machine& machine = s21;
machine.start();
```

The call still reaches `Miner::start()` through runtime polymorphism.

## Abstract does not mean empty

An abstract base class can still contain data, constructors, ordinary member functions, and regular virtual functions:

```cpp
class Machine {
protected:
    int id;

public:
    Machine(int machineId) : id(machineId) {}

    void showId() const {
        std::cout << id << '\n';
    }

    virtual void start() = 0;
};
```

## Video 2 — Abstract base classes

https://www.youtube.com/watch?v=rECcII1Mdfc

Professor Hank Stalica demonstrates abstract base classes, pure virtual functions, and required derived-class overrides.

## Data-center example

```cpp
#include <iostream>

class Sensor {
public:
    virtual double read() const = 0;
    virtual ~Sensor() = default;
};

class TemperatureSensor : public Sensor {
public:
    double read() const override {
        return 72.5;
    }
};

class PowerSensor : public Sensor {
public:
    double read() const override {
        return 428.0;
    }
};

void printReading(const Sensor& sensor) {
    std::cout << sensor.read() << '\n';
}
```

The caller depends on the `Sensor` contract instead of the concrete sensor type.

## Why a virtual destructor matters

```cpp
virtual ~Sensor() = default;
```

A polymorphic base class should normally have a virtual destructor so destruction through a base pointer correctly runs the derived destructor chain.

## Interface-style design

Native C++ does not require a special `interface` keyword. A class made mostly or entirely from public pure virtual functions is commonly used as an interface-style contract:

```cpp
class Controllable {
public:
    virtual void start() = 0;
    virtual void stop() = 0;
    virtual bool healthy() const = 0;
    virtual ~Controllable() = default;
};
```

Different devices can implement the same contract while keeping their own internal logic.

## Video 3 — Beginner reinforcement

https://www.youtube.com/watch?v=mvTo_zpr9oA

ScoreShala reinforces the relationship between pure virtual functions and abstract classes.

## Pure virtual vs. ordinary virtual

| Declaration | Meaning |
|---|---|
| `virtual void run();` | Virtual behavior; base normally supplies a definition. |
| `virtual void run() = 0;` | Pure virtual behavior; concrete derived classes must provide a final override. |
| `void run() override;` | Derived class explicitly states that it overrides a virtual base function. |

## Common mistakes

- Trying to instantiate an abstract base class.
- Forgetting the `= 0` pure specifier.
- Writing an override with the wrong parameter list.
- Leaving off `override` and losing a useful compiler check.
- Deleting derived objects through a base pointer without a virtual base destructor.
- Assuming abstract classes cannot contain ordinary implemented functions or state.

## Practice

1. Create an abstract class named `Device`.
2. Add `virtual void status() const = 0;`.
3. Add a virtual default destructor.
4. Derive `Router` and `ASICMiner`.
5. Override `status()` in both.
6. Write a function that accepts `const Device&` and calls `status()`.
7. Pass both concrete objects to that function.

Review [OSC++.017: Inheritance Basics](https://bitcoinversus.tech/2026/10/02/oscpp-017-inheritance-basics/) and [OSC++.006: References and Pass by Reference](https://bitcoinversus.tech/2026/09/25/cpp-lesson-6-references-pass-by-reference/) if you want to reinforce the class hierarchy and reference mechanics.

## Key takeaway

A pure virtual function uses `= 0` to define required polymorphic behavior. A class with an unimplemented pure virtual function is abstract and cannot be instantiated, but it can still provide shared code and serve as a common base-class interface for concrete derived classes.
