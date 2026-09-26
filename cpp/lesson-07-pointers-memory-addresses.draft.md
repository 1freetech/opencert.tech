---
title: "C++ Lesson 7: Pointers and Memory Addresses"
status: prepared-draft
wordpress_post_id: 18634
wordpress_status: draft
series: "C++ Lessons"
lesson_number: 7
---

# C++ Lesson 7: Pointers and Memory Addresses

C++ Lesson 7 continues directly from references and pass-by-reference by introducing pointers. A pointer stores the memory address of another object.

## Create and Dereference a Pointer

```cpp
int value = 42;
int* ptr = &value;
std::cout << *ptr << '\n';
```

`&value` obtains the address of `value`. The pointer stores that address. `*ptr` dereferences it and accesses the object.

## Modify Through a Pointer

```cpp
int value = 42;
int* ptr = &value;
*ptr = 100;
```

After the assignment, `value` is 100.

## Use nullptr

```cpp
int* ptr = nullptr;
if (ptr != nullptr) {
    std::cout << *ptr;
}
```

A pointer should not be dereferenced unless it refers to a valid object.

## Pointers and Functions

```cpp
void set_value(int* number) {
    if (number != nullptr) {
        *number = 75;
    }
}

int value = 10;
set_value(&value);
```

Lesson 6 introduced references. Understanding references and pointers prepares students for arrays, dynamic memory, data structures, APIs, and systems programming.

## Video Reference

freeCodeCamp.org — Pointers in C/C++ [Full Course]

https://www.youtube.com/watch?v=zuegQmMdy8M

## Practice

Create an integer, point to it, modify it through the pointer, and print the changed value. Then initialize another pointer to `nullptr` and guard its dereference.

## Reference

cppreference C++ language documentation and the freeCodeCamp.org pointer course developed from MyCodeSchool material.
