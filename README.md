# 🔁 Consistent Hashing CLI

A minimal Python project demonstrating consistent hashing with virtual nodes.  
It supports a simple interactive CLI for adding/removing nodes and checking which node a key maps to.

## 🚀 Features

- Consistent hashing with virtual nodes (replicas)
- Add and remove nodes dynamically
- Map keys to nodes
- Simple CLI interface

## 📦 Requirements

- Python 3.8+
- No external dependencies

## 🛠️ Installation

1. Clone the repository:
   git clone https://github.com/<your-username>/consistent-hashing.git
   cd consistent-hashing
   
(Optional but recommended) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
No dependencies to install — it uses the standard library only.

🧪 Usage
Run the CLI:
python cli.py
Example commands:
>>> add node1
>>> add node2
>>> get user123
>>> show
>>> remove node1
>>> exit

🧠 What is Consistent Hashing?
Consistent hashing is a strategy to distribute keys across a dynamic set of nodes, minimizing re-distribution when nodes are added or removed.
It's commonly used in distributed systems like:

Caching (e.g., memcached)

Load balancers

Distributed databases

Sharded storage systems

📂 Project Structure
consistent-hashing/
├── hashring.py     # Core logic for consistent hashing
├── cli.py          # Interactive command-line interface
└── README.md       # Project documentation
