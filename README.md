# LOOInteract

![Status](https://img.shields.io/badge/status-experimental-orange)
![Python](https://img.shields.io/badge/python-planned-blue)
![BLE](https://img.shields.io/badge/protocol-BLE-informational)
![Platform](https://img.shields.io/badge/platform-LOOI-lightgrey)

**LOOInteract** is a reverse-engineering, experimentation, and open API development project for the **LOOI robot**.

Its purpose is to turn LOOI into a **programmable robotic platform** by documenting its BLE protocol, reproducing the required handshake, and building a clean Python API before any Android MVP.

---

## Overview

LOOI is not treated here as a simple gadget, but as a **robotic body driven by a smartphone**.

This project focuses on understanding and exposing the robot’s low-level capabilities in a structured way, so they can later be used by:

- a Python SDK,
- a scripting layer,
- and eventually a custom Android application.

---

## Goals

The main goals of this project are to:

- connect to the LOOI robot over BLE;
- understand and reproduce the required handshake;
- send movement and hardware commands;
- control the neck, lamp, and other exposed features;
- read sensor and robot state data;
- build a clean, reusable Python API;
- prepare a future scripting system;
- keep the project independent from the official application.

---

## Current Status

This project is in its **early experimental phase**.

So far, the following building blocks have been identified:

- main command characteristic: `fe00`
- other known characteristics:
  - `fed0`
  - `fed1`
  - `fed2`
  - `fed9`
  - `ff02`

Some command mappings and protocol hypotheses come from public reverse-engineering work, but they still need direct experimental validation.

---

## Project Principles

LOOInteract follows a few strict design principles:

- **Understand before coding**
- **Isolate the handshake**
- **Build Python first**
- **Avoid dependency on the official app**
- **Document discoveries precisely**
- **Separate transport, protocol, commands, and behavior**

The idea is to avoid mixing reverse engineering, UI, scripting, and app logic too early.

---

## Technical Roadmap

The intended roadmap is:

1. Map the known BLE characteristics
2. Understand and reproduce the handshake
3. Validate simple commands:
   - lamp
   - neck
   - slow movement
   - sensor reading
4. Build a stable Python client
5. Add a scripting layer
6. Only then consider an Android MVP

---

## Planned Architecture

The repository is expected to evolve toward something like this:

```text
LOOInteract/
├─ docs/                # protocol notes, reverse-engineering docs
├─ captures/            # BLE captures and raw observations
├─ looi/                # Python package
├─ examples/            # quick tests and demos
├─ tools/               # helper scripts
├─ tests/               # unit and protocol tests
└─ README.md
