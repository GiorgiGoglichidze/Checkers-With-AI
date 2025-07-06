# Checkers-With-AI

This is a Python implementation of the classic Checkers (Draughts) game with an integrated AI opponent using the Minimax algorithm with alpha-beta pruning. The project is built using `pygame` for visualization.

## 🕹️ Features

- Fully playable Checkers game (single or AI opponent)
- Chain captures and king promotion logic implemented
- AI opponent using Minimax algorithm with alpha-beta pruning
- Piece movement highlighting
- Win/draw detection
- Clean and intuitive board UI with Pygame

## 🤖 AI Logic

The AI uses the Minimax algorithm to evaluate possible moves up to a given depth, applying alpha-beta pruning for optimization. Evaluation is based on a heuristic scoring function that considers piece count and king advantage.

## 💡 How to Play

- Click on a piece to select it
- Highlighted circles show possible moves
- Captures are prioritized according to official Checkers rules
- Kings can move both forward and backward after promotion

## 🛠️ Requirements

- Python 3.8+
- `pygame`

Install dependencies:

```bash
pip install pygame
