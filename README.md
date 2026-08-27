# Simulation & Modeling Sessional
A Python-based simulation of a **single-server queuing system** using predefined random numbers for customer inter-arrival time and service time.

---

## 📌 Experiment: Single-Server Queue Simulation

This experiment demonstrates how a **Single-Server Queue** can be modeled and analyzed using simulation.

The program simulates **8 customers** and calculates:

* Inter-Arrival Time (IAT)
* Arrival Time
* Service Time (ST)
* Time Service Begins (TSB)
* Waiting Time (WT)
* Time Service Ends (TSE)
* Time Spent in System (TSS)
* Idle Time of Server (ITS)

Finally, the program generates a **simulation table** and calculates several **statistical measures**.

---

## 🎯 Objectives

The main objectives of this experiment are:

1. To understand the basic concept of queue simulation.
2. To simulate a single-server queuing system using Python.
3. To convert random numbers into inter-arrival and service times.
4. To calculate customer waiting time.
5. To calculate the total time spent by customers in the system.
6. To determine the idle time of the server.
7. To analyze the performance of the queuing system.

---

## 🧰 Technologies Used

* **Python 3**
* Lists
* Functions
* Loops
* Conditional Statements
* Basic Arithmetic Operations

---

## 📊 Random Numbers

The simulation uses two sets of random numbers.

### Random Numbers for Inter-Arrival Time

Used for **customers 2–8**:

```text
[861, 341, 142, 156, 476, 271, 178]
```

### Random Numbers for Service Time

Used for **customers 1–8**:

```text
[12, 31, 27, 69, 91, 55, 77, 54]
```

---

## 🔢 Random Number Mapping

Random numbers are converted into **Inter-Arrival Time (IAT)** and **Service Time (ST)** using predefined ranges.

### Inter-Arrival Time (IAT)

| Random Number | IAT |
| ------------- | --: |
| 1–125         |   1 |
| 126–250       |   2 |
| 251–375       |   3 |
| 376–500       |   4 |
| 501–625       |   5 |
| 626–750       |   6 |
| 751–875       |   7 |
| 876–999       |   8 |

The mapping is implemented using the `get_iat()` function.

### Service Time (ST)

| Random Number | ST |
| ------------- | -: |
| 1–10          |  1 |
| 11–30         |  2 |
| 31–60         |  3 |
| 61–85         |  4 |
| 86–95         |  5 |
| 96–999        |  6 |

The mapping is implemented using the `get_st()` function.

---

## ⚙️ Simulation Logic

The simulation processes each customer sequentially.

### 1. Arrival Time

For the first customer:

```text
Arrival Time = 0
```

For subsequent customers:

```text
Arrival Time = Previous Arrival Time + IAT
```

---

### 2. Time Service Begins (TSB)

The server starts serving a customer when both the customer has arrived and the server is available.

```text
TSB = max(Arrival Time, Previous Service End Time)
```

---

### 3. Waiting Time (WT)

Waiting time is calculated as:

```text
WT = TSB - Arrival Time
```

If the server is busy when a customer arrives, the customer has to wait.

---

### 4. Time Service Ends (TSE)

The service end time is calculated as:

```text
TSE = TSB + Service Time
```

---

### 5. Time Spent in System (TSS)

The total time spent in the system is:

```text
TSS = TSE - Arrival Time
```

This includes both **waiting time and service time**.

---

### 6. Idle Time of Server (ITS)

If a customer arrives after the server has finished serving the previous customer:

```text
ITS = Arrival Time - Previous Service End Time
```

Otherwise:

```text
ITS = 0
```

The program implements this using:

```python
its = max(0, arrival - prev_end)
```

---

## 📋 Simulation Table

The program generates a formatted table containing the following information:

| Column  | Description                          |
| ------- | ------------------------------------ |
| Cust    | Customer Number                      |
| RN(IAT) | Random Number for Inter-Arrival Time |
| IAT     | Inter-Arrival Time                   |
| Arr     | Arrival Time                         |
| RN(ST)  | Random Number for Service Time       |
| ST      | Service Time                         |
| TSB     | Time Service Begins                  |
| WT      | Waiting Time                         |
| TSE     | Time Service Ends                    |
| TSS     | Time Spent in System                 |
| ITS     | Idle Time of Server                  |

The output format is:

```text
Cust  RN(IAT)   IAT   Arr   RN(ST)   ST   TSB   WT   TSE   TSS   ITS
```

---

## 🧮 Statistical Summary

After completing the simulation, the program calculates the following statistics.

### Average Waiting Time

```text
Average Waiting Time
= Total Waiting Time / Number of Customers
```

### Average Inter-Arrival Time

```text
Average IAT
= Total IAT / Number of Customers
```

### Average Service Time

```text
Average Service Time
= Total Service Time / Number of Customers
```

### Average Time in System

```text
Average Time in System
= Total Time in System / Number of Customers
```

### Total Server Idle Time

```text
Total Server Idle Time
= Sum of all Idle Times
```

### Average Waiting Time of Customers Who Waited

Only customers whose waiting time is greater than zero are considered.

```text
Average Waiting Time (Customers Who Waited)
= Total Waiting Time of Waiting Customers
  / Number of Waiting Customers
```

---

## 📈 Program Features

* Converts random numbers into inter-arrival times.
* Converts random numbers into service times.
* Simulates customer arrivals.
* Determines when the server starts serving each customer.
* Calculates customer waiting time.
* Calculates service completion time.
* Calculates total time spent in the system.
* Tracks server idle time.
* Generates a formatted simulation table.
* Calculates statistical performance measures.

---

## ▶️ How to Run

### Prerequisites

Make sure **Python 3** is installed on your system.

### Run the Program

Open the project directory in a terminal and run:

```bash
python single_server_queue.py
```

The program will display:

1. The complete simulation table.
2. The statistical summary.

---

## 📁 Project Structure

```text
Single-Server-Queue-Simulation/
│
├── single_server_queue.py
└── README.md
```

> Replace `single_server_queue.py` with your actual Python filename if it is different.

---

## 📚 Conclusion

This experiment demonstrates the implementation of a **single-server queuing system using Python simulation**.

By using predefined random numbers and probability-based mappings, the program determines customer arrival and service times. It then calculates waiting time, service time, time spent in the system, and server idle time.

The experiment provides a practical understanding of how **simulation techniques can be used to analyze and evaluate the performance of queuing systems**.
