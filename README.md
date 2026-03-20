# LOOInteract

**LOOInteract** is a reverse-engineering, experimentation, and open API development project for the **LOOI robot**.

## Objective

The goal of this project is to understand, document, and properly use the LOOI BLE protocol in order to:

- connect to the robot;
- reproduce the required handshake;
- send movement commands;
- control the neck, lamp, and other hardware features;
- read sensors and robot state;
- build a clean and reusable Python API;
- later prepare a scriptable Android application.

## Vision

LOOI is not seen here as a simple gadget, but as a **robotic body driven by a smartphone**.  
The goal is to turn this robot into a **programmable, educational, and extensible platform**.

## Project Principles

- Understand before coding.
- Isolate the handshake.
- Build a minimal but clean Python API first.
- Do not depend on the official app.
- Document every discovery precisely.
- Separate BLE transport, protocol, commands, and application logic.

## Roadmap

1. Map the known BLE characteristics.
2. Understand and reproduce the handshake.
3. Test simple commands:
   - lamp
   - neck
   - slow movement
   - sensor reading
4. Build a stable Python client.
5. Add a scripting layer.
6. Consider an Android port afterwards.

## Current Status

The project is in its initial phase.

The first identified building blocks are:

- main command characteristic: `fe00`
- other known characteristics:
  - `fed0`
  - `fed1`
  - `fed2`
  - `fed9`
  - `ff02`

Some commands and hypotheses come from public reverse-engineering work, but they still need experimental validation.

## Planned Architecture

The repository is expected to evolve toward a structure including:

- protocol documentation
- reverse-engineering notes and captures
- Python API
- CLI testing tools
- experimentation scripts
- later, a scripting engine and an Android interface

## Technical Philosophy

This project follows this order:

1. Functional Python API
2. Clean command abstraction
3. Scripting engine
4. Only then an Android MVP

This makes it possible to validate the protocol without mixing BLE, UI, and advanced logic too early.

## Warning

This project is experimental.  
The LOOI protocol is not yet fully documented.  
Some hypotheses may change.  
Tests must be performed carefully to avoid unexpected robot movements.

## Project Name

**LOOInteract** = **LOOI + Interaction + Programmable Interface**

## Author

Project initiated by **CozmoCyke**.

## License

To be defined.

## Notes

This `README.md` is an initial foundation.  
It will be expanded as the protocol becomes clearer and the Python API matures.
