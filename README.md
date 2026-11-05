# Object-Oriented Address Book

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Object--Oriented%20Programming-lightgrey?style=flat-square)
![UserDict](https://img.shields.io/badge/collections-UserDict-yellow?style=flat-square)

## Overview

This repository contains an object-oriented Python implementation of a simple address book.

The project introduces custom classes for contacts and phone numbers and uses inheritance to organize and validate stored data.

## Tech Stack

- Python
- Object-Oriented Programming
- `collections.UserDict`

## Implemented Classes

### Field

Base class for stored contact values.

### Name

Represents a contact name.

### Phone

Represents a phone number and validates that it:

- contains only digits;
- has exactly 10 characters.

### Record

Represents a single contact and supports:

- adding phone numbers;
- searching for a phone number;
- removing phone numbers;
- editing existing phone numbers.

### AddressBook

Extends `UserDict` and supports:

- adding records;
- searching records by name;
- deleting records;
- displaying all saved contacts.

## Demonstration

[tech_task.py](./tech_task.py) creates example contacts, adds them to the address book, edits phone numbers, searches for a phone, and removes a record.

## Learning Outcomes

This homework helped me practice:

- classes and inheritance;
- encapsulating validation logic;
- custom object representations;
- collections based on `UserDict`;
- composing objects through `Record` and `AddressBook`;
- building the foundation for a larger CLI contact-management application.
