# 🥊 Pixel Punishment (Pygame)

A 2D local multiplayer fighter game built using **Pygame**. Two players face off using keyboard controls, with simple animations, health bars, and win screens. Designed to be lightweight, fast, and fun.

## 🎮 Gameplay Overview

- **Player 1** and **Player 2** take turns moving and punching.
- Each player starts with 10 health bars.
- The first player to reduce their opponent’s health to 0 wins.
- Includes basic animations, sounds, and end-game screens.

---

## 🕹️ Controls

### Player 1 (Left):
- **A** – Move Left
- **D** – Move Right
- **W** – Punch

### Player 2 (Right):
- **J** – Move Left
- **L** – Move Right
- **I** – Punch

---

## 📦 Features

- Character animation using sprite sequences.
- Sound effects on punches.
- Health bar display with visual segments.
- Start screen and win screens for both players.
- Restart option after game ends.

---

## 📁 Assets Required

Make sure to have the following image and sound files in the same directory:

| Filename       | Purpose                     |
|----------------|-----------------------------|
| `Start_pic.png` | Start screen background     |
| `Background.png`| Game background             |
| `p1win.png`     | Player 1 win screen         |
| `p2won.png`     | Player 2 win screen         |
| `RightChar1.png` to `RightChar6.png` | Player 1 animation frames |
| `leftChar1.png` to `leftChar3.png`  | Player 2 animation frames |
| `punch.mp3`     | Punch sound effect          |

> ⚠️ The game will **crash** if any of these files are missing.

---

## 🚀 Getting Started

### 1. Install Requirements

Make sure you have Python 3 and Pygame installed:

```bash
pip install pygame
