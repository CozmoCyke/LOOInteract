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

## Temporary Results

## Stable BLE Mode Observed on Our LOOI

After pressing the **Touch button**, our LOOI exposes a stable BLE endpoint at:

`6D:46:AF:87:31:1D`

This is the BLE profile we have actually observed and tested on Windows.

### Known Characteristics (Stable Mode)

| UUID Prefix | Observed Function | Notes |
| --- | --- | --- |
| **fed4** | **Read buffer / raw state** | Always returns a large block of `00` bytes in current tests. |
| **fed5** | **Structured command write** | Valid write channel with response. |
| **fed6** | **Indicate / read** | Subscription works, but no useful payload has been observed yet. |
| **fed7** | **Structured command write (no response)** | Valid write channel, behavior very similar to `fed5`. |
| **fed8** | **Ack / status notify-read channel** | Main observable feedback channel in stable mode. |

## Important Difference from Other Reverse-Engineering Notes

Some external notes describe a LOOI command interface using:

- `fe00` as the main command write characteristic
- `fed0` for movement
- `fed1` for neck/head control
- `fed2` for headlight
- `fed9` for telemetry

**We do not observe those characteristics on our stable BLE endpoint.**

Instead, our tested stable mode uses:

- `fed5` and `fed7` for writes
- `fed8` for observable acknowledgements/status

So, while some **raw command frames may still be compatible**, the **BLE transport layer is different** in our setup.

## Known Valid Structured Frame

The following frame is accepted and recognized by our stable endpoint:

`00100000010032030a0001ff00010a3203ff0003`

This is the same raw frame that other reverse-engineering notes label as:

`fe00 SLOW RECENTER HEAD`

### What this means in our version

- The **raw frame itself matches**
- But the **write channel is different**
- In our setup, it is sent through:
  - `fed5` (write with response)
  - `fed7` (write without response)
- The main observed feedback comes from:
  - `fed8` (notify/read)

### Important caveat

Although this frame is clearly **recognized** by our device, we do **not yet have proof** that it produces the same physical neck movement as described elsewhere.

So the correct statement is:

> The frame is protocol-compatible, but the physical effect is not yet confirmed to be identical in our stable BLE mode.

## What We Have Learned About the Frame Structure

Using controlled mutation tests, we found the following:

### Byte 1 is critical

Base frame:

`00 10 00 00 01 00 32 03 0a 00 01 ff 00 01 0a 32 03 ff 00 03`

If **byte 1** (`10`) is changed, the frame stops triggering any `fed8` notification.

This strongly suggests that **byte 1 is a critical validity/type field**.

### Byte 0 is variable

If **byte 0** is changed, the frame is still accepted and `fed8` returns a structured response.

This suggests that **byte 0 is likely a command variant / opcode / command index field**.

## Observed ACK Behavior on `fed8`

For the base frame family, mutating byte 0 changes the `fed8` response:

| Sent Byte 0 | `fed8` Response Prefix |
| --- | --- |
| `01` | `01110010...` |
| `03` | `03110010...` |
| `0a` | `0a110010...` |
| `10` | `00110010...` |
| `32` | `02110010...` |
| `ff` | `0f110010...` |

This means `fed8` is **not just a static battery value**.  
It behaves more like:

- a structured ACK
- a transformed status code
- or a partial mirror of the command interpreted by the device

## Current Working Model

### Stable Mode Command Path

- **Write commands**
  - `fed5`
  - `fed7`

- **Read/notify acknowledgement**
  - `fed8`

- **Unused / not yet useful**
  - `fed4`
  - `fed6`

### Frame interpretation hypothesis

| Byte Index | Likely Role | Confidence |
| --- | --- | --- |
| **0** | Command variant / opcode / command selector | Medium |
| **1** | Critical type / validity / class field | High |
| **2..19** | Command parameters | Medium |
| **fed8 payload** | Structured ACK / interpreted status | High |

## Recommended Documentation Wording

Instead of writing:

> The primary write characteristic is `fe00`.

For our version, it is more accurate to write:

> On our stable LOOI BLE endpoint, the main observed write characteristics are `fed5` and `fed7`, while `fed8` acts as the primary acknowledgement/status channel.

And instead of using the generic characteristic table from other notes, we should document:

| UUID Prefix | Function | Notes |
| --- | --- | --- |
| **fed4** | **Read buffer / raw state** | Observed as all-zero data in current tests. |
| **fed5** | **Structured command write** | Valid command channel with response. |
| **fed6** | **Indicate / read** | Subscription works, but no useful payload observed yet. |
| **fed7** | **Structured command write (no response)** | Valid command channel, behavior close to `fed5`. |
| **fed8** | **ACK / status notify-read channel** | Main observable feedback channel in stable mode. |

## Summary

Our current reverse-engineering results strongly suggest that:

- the stable endpoint `6D:46:AF:87:31:1D` is a real LOOI BLE interface
- it appears after **Touch button activation**
- it accepts structured command frames on `fed5` and `fed7`
- it returns structured acknowledgements on `fed8`
- at least one known external command frame is recognized
- but direct physical control of motors/LEDs is **not yet proven** in this stable mode

So the safest conclusion is:

> Our LOOI stable BLE mode appears protocol-compatible with at least part of the known command frame family, but it uses a different visible GATT interface than the one described in some other reverse-engineering notes.
