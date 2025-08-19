# 🎮 Pacman AI Projects

A Python implementation of artificial intelligence search algorithms to solve problems within the Berkeley Pac-Man environment. The Pac-Man Projects, developed at UC Berkeley, apply Artificial Intelligence concepts to the famous arcade game.

![Pacman](https://img.shields.io/badge/Pacman-AI%20Projects-yellow) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 📋 About

> Under The Supervision of [Prof. Mahdi Javanmardi](https://scholar.google.co.jp/citations?user=6Za8HuYAAAAJ&hl=en)  
> Fall 2021 | Amirkabir University of Technology

This repository contains implementations of various AI algorithms applied to the classic Pacman game. Each project builds upon the previous one, introducing more complex AI concepts and challenges.

## 🚀 Projects

### 1. 🔍 Search Algorithms
Implemented classic search algorithms for pathfinding in Pacman mazes:

- **Depth-First Search (DFS)** - `depthFirstSearch`
- **Breadth-First Search (BFS)** - `breadthFirstSearch`
- **Uniform Cost Search** - `uniformCostSearch`
- **A * Search** - `aStarSearch`

**Key Features:**
- 🧭 Pathfinding in various maze configurations
- 📏 Heuristic functions (Manhattan distance, custom heuristics)
- 🎯 Corner finding problem solution
- 🍎 Food collection search

### 2. 👥 Multi-Agent Search
Implemented adversarial search algorithms for Pacman vs Ghosts scenarios:

- **Minimax** - `MinimaxAgent`
- **Alpha-Beta Pruning** - `AlphaBetaAgent`
- **Expectimax** - `ExpectimaxAgent`
- **Evaluation Functions** - `Custom heuristic evaluation`

**Key Features:**
- 🎲 Probabilistic reasoning for ghost movements
- ✂️ Efficient pruning of search trees
- 🧠 Sophisticated evaluation functions
- 🏆 Performance optimization for various game scenarios

### 3. 🤖 Reinforcement Learning
Implemented model-based and model-free reinforcement learning algorithms:

- **Value Iteration** - `ValueIterationAgent`
- **Q-Learning** - `QLearningAgent`
- **Approximate Q-Learning** - `ApproximateQAgent`
- **Epsilon-Greedy Action Selection**
- **Bridge Crossing Analysis**

**Key Features:**
- 📊 Policy evaluation and improvement
- 🎯 Reward maximization strategies
- 🔧 Parameter tuning for optimal performance
- 🧮 Function approximation for large state spaces

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Amirbehnam1009/Pacman.git
   cd Pacman
   ```
2. **Ensure you have Python 3.x installed**
3. **Run the projects:**
    ```bash
    # Project 1: Search
    python pacman.py
    
    # Project 2: Multi-Agent Search
    python pacman.py -p MinimaxAgent
    
    # Project 3: Reinforcement Learning
    python gridworld.py -a q -k 100
    ```
## 📁 Project Structure
``` bash
Pacman/
│
├── search.py              # Search algorithms implementation
├── searchAgents.py        # Search agents and problems
├── multiAgents.py         # Multi-agent algorithms
├── valueIterationAgents.py # Value iteration agents
├── qlearningAgents.py     # Q-learning agents
├── analysis.py            # Analysis and answers
├── game.py               # Game engine
├── pacman.py             # Main Pacman executable
├── gridworld.py          # Gridworld environment
├── util.py               # Utility functions
└── test_cases/           # Test cases for autograder  
```
## 🧪 Testing
Use the autograder to test your implementations:

``` bash
# Test all questions
python autograder.py

# Test specific question
python autograder.py -q q2

# Test with no graphics
python autograder.py -q q2 --no-graphics
```

## 🎮 How to Play
Run the game with different agents:

``` bash
# Run with specific layout and agent
python pacman.py -l mediumClassic -p MinimaxAgent -a depth=3

# Run with faster animation
python pacman.py --frameTime 0 -p ExpectimaxAgent -k 2

# Run Q-learning agent
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
```
## 📊 Performance Metrics
Each project includes evaluation criteria:

* 🎯 Solution optimality (path length, score)

* ⚡ Algorithm efficiency (nodes expanded, time)

* 🧠 Heuristic quality (admissibility, consistency)

* 🏆 Win rates against ghosts

* 📚 Learning Concepts
This repository demonstrates:

* State space representation

* Search algorithm properties (completeness, optimality)

* Adversarial search techniques

* Reinforcement learning principles

* Heuristic function design

* Performance optimization

## 📄 License
This project is based on the UC Berkeley Pacman Projects, adapted for educational purposes at Amirkabir University of Technology.

## 🙏 Acknowledgments
* UC Berkeley CS188 for the original Pacman projects

* Amirkabir University of Technology for the course structure

* Professor Mahdi Javanmardi for guidance and supervision
