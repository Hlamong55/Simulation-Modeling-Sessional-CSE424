## Simulation & Modeling Sessional - CSE 454

This repository contains Python implementations of different experiments performed in the **Simulation & Modeling Sessional Course**.

The experiments cover queue simulation, inventory simulation, and random number generation using mathematical methods.

---

## Experiments

### 1. Single-Server Queue Simulation

**Description:**

This experiment simulates a single-server queuing system using predefined random numbers. It determines customer arrival times, service times, waiting times, and server idle times.

**Key Features:**

- Generates Inter-Arrival Time (IAT) from random numbers.
- Generates Service Time (ST) from random numbers.
- Calculates customer Arrival Time.
- Calculates Time Service Begins (TSB).
- Calculates Waiting Time (WT).
- Calculates Time Service Ends (TSE).
- Calculates Time Spent in System (TSS).
- Calculates Idle Time of Server (ITS).
- Generates a customer-wise simulation table.
- Provides a statistical summary.

**Statistical Measures:**

- Average Waiting Time
- Average Inter-Arrival Time
- Average Service Time
- Average Time in System
- Total Server Idle Time
- Average Waiting Time of Customers Who Waited

---

### 2. Newspaper Inventory Simulation

**Description:**

This experiment implements a newspaper inventory simulation using random numbers and probability distributions.

The simulation determines the type of newsday (Good, Fair, or Poor), calculates daily newspaper demand, and evaluates the daily profit based on sales revenue, scrap revenue, and purchase cost.

**Key Features:**

- Determines newsday type using random numbers.
- Uses probability distributions to generate daily demand.
- Calculates the number of newspapers sold.
- Calculates unsold newspapers.
- Calculates sales revenue.
- Calculates scrap revenue.
- Calculates daily profit.
- Calculates total profit over multiple days.
- Generates a complete simulation table.

**Business Parameters:**

| Parameter | Value |
|---|---:|
| Newspapers Purchased per Day | 80 |
| Purchase Price | $0.50 |
| Selling Price | $0.75 |
| Scrap Value | $0.15 |
| Simulation Period | 5 Days |

**Profit Calculation:**

```text
Profit = Sales Revenue + Scrap Revenue - Purchase Cost
```

---

### 3. Linear Congruential Generator (LCG)

**Description:**

This experiment implements a **Linear Congruential Generator (LCG)** in Python to generate pseudo-random numbers using a mathematical recurrence relation.

The program generates random numbers based on the given seed and parameters, calculates normalized random values, determines the period length, and checks the full-period conditions using the Hull-Dobell Theorem.

**Mathematical Formula:**

```text
Xi = (a * Xi-1 + c) mod m
```

Where:

- `Xi` = Current random integer
- `Xi-1` = Previous random integer
- `a` = Multiplier
- `c` = Increment
- `m` = Modulus
- `X0` = Initial seed

**Normalized Random Number:**

```text
Ri = Xi / m
```

**Key Features:**

- Takes seed and LCG parameters as user input.
- Generates pseudo-random numbers.
- Calculates normalized random values.
- Displays the generated sequence in a formatted table.
- Determines the period length of the generated sequence.
- Checks the full-period conditions using the Hull-Dobell Theorem.

**Hull-Dobell Full-Period Conditions:**

For a mixed LCG (`c != 0`) to have a full period, the following conditions must hold:

1. `gcd(c, m) = 1`
2. Every prime factor of `m` must divide `(a - 1)`.
3. If `m` is divisible by 4, then `(a - 1)` must also be divisible by 4.

---

## Technologies Used

- Python 3
- Basic Mathematical Operations
- Probability Distributions
- Random Number Generation
- Lists and Dictionaries
- Functions and Loops
- Conditional Statements

---

## Project Structure

```text
Simulation-Modeling-Sessional/
│
├── single_server_queue.py
├── newspaper_inventory.py
├── random_number_lcg.py
│
└── README.md
```

*Note: Replace the Python filenames above with the actual filenames used in this repository.*

---

## Requirements

- Python 3.x
- No external Python packages are required.

The programs use Python's built-in features and standard library.

---

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd Simulation-Modeling-Sessional
```

Run an experiment:

**1. Single-Server Queue Simulation**

```bash
python single_server_queue.py
```

**2. Newspaper Inventory Simulation**

```bash
python newspaper_inventory.py
```

**3. Linear Congruential Generator**

```bash
python lcg.py
```

For the LCG program, enter the required values when prompted:

- Seed (X0)
- Multiplier (a)
- Increment (c)
- Modulus (m)
- Number of random numbers

---

## Learning Outcomes

Through these experiments, the following concepts are explored:

- Understanding and implementing single-server queuing systems.
- Analyzing customer arrival and service patterns.
- Calculating queue performance measures.
- Understanding probability-based inventory simulation.
- Evaluating daily and total profit in inventory systems.
- Understanding pseudo-random number generation.
- Analyzing the period of a Linear Congruential Generator.
- Applying the Hull-Dobell theorem to check full-period conditions.

---

## Conclusion

This repository demonstrates the practical implementation of important Simulation & Modeling concepts using Python.

The experiments provide hands-on experience with **queueing systems, inventory management, probability distributions, and pseudo-random number generation**.

Each experiment helps develop a better understanding of how mathematical models and simulation techniques can be applied to solve real-world problems.