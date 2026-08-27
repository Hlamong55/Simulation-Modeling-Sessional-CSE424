# Single-Server Queue Simulation

## 📌 Experiment Overview

This experiment implements a **Single-Server Queue Simulation** using Python.

The simulation models customers arriving at a single service counter/server. Each customer has an **Inter-Arrival Time (IAT)** and **Service Time (ST)** determined from Random Numbers (RN) using predefined probability distributions.

The program calculates:

- Arrival Time
- Inter-Arrival Time (IAT)
- Service Time (ST)
- Time Service Begins (TSB)
- Waiting Time (WT)
- Time Service Ends (TSE)
- Time Spent in System (TSS)
- Idle Time of Server (ITS)

It also calculates important statistical measures such as average waiting time, average service time, average time in system, and total server idle time.

---

## 🎯 Objectives

The main objectives of this experiment are:

1. To understand the concept of **queue simulation**.
2. To simulate a **single-server queuing system** using Python.
3. To convert random numbers into IAT and service time using probability distributions.
4. To calculate customer waiting time and system time.
5. To determine server idle time.
6. To analyze the overall performance of the queue.

---

## 🧰 Technologies Used

- **Python 3**
- Lists
- Functions
- Loops
- Conditional Statements
- Basic Mathematical Calculations

---

## 📊 Random Numbers

### Random Numbers for Inter-Arrival Time

Used for customers **2–8**:

```text
[861, 341, 142, 156, 476, 271, 178]
Random Numbers for Service Time

Used for customers 1–8:

[12, 31, 27, 69, 91, 55, 77, 54]
🔢 Random Number Mapping
Inter-Arrival Time (IAT)
Random Number	IAT
1–125	1
126–250	2
251–375	3
376–500	4
501–625	5
626–750	6
751–875	7
876–999	8

The mapping is implemented using the get_iat() function.

Service Time (ST)
Random Number	ST
1–10	1
11–30	2
31–60	3
61–85	4
86–95	5
96–999	6

The mapping is implemented using the get_st() function.

⚙️ Simulation Logic

The simulation processes each customer sequentially.

1. Arrival Time

For the first customer:

Arrival Time = 0

For subsequent customers:

Arrival Time = Previous Arrival Time + IAT
2. Time Service Begins (TSB)

The server starts serving a customer when both the customer has arrived and the server is available.

TSB = max(Arrival Time, Previous Service End Time)
3. Waiting Time (WT)
WT = TSB - Arrival Time

If the server is busy when the customer arrives, the customer has to wait.

4. Time Service Ends (TSE)
TSE = TSB + Service Time
5. Time Spent in System (TSS)
TSS = TSE - Arrival Time

This represents the total time a customer spends in the system, including waiting and service time.

6. Idle Time of Server (ITS)

If the customer arrives after the previous customer has finished service:

ITS = Arrival Time - Previous Service End Time

Otherwise:

ITS = 0

The program implements this using:

its = max(0, arrival - prev_end)
🧮 Statistical Measures

After processing all customers, the program calculates several performance measures.

Average Waiting Time
Average Waiting Time = Total Waiting Time / Number of Customers
Average IAT
Average IAT = Total IAT / Number of Customers
Average Service Time
Average Service Time = Total Service Time / Number of Customers
Average Time in System
Average Time in System = Total Time in System / Number of Customers
Average Waiting Time of Customers Who Waited

Only customers with WT > 0 are considered.

Average Waiting Time (Waited)
= Total Waiting Time of Waiting Customers
  / Number of Waiting Customers
📋 Simulation Table

The program generates a formatted simulation table:

Cust | RN(IAT) | IAT | Arr | RN(ST) | ST | TSB | WT | TSE | TSS | ITS
Abbreviation	Meaning
Cust	Customer Number
RN(IAT)	Random Number for Inter-Arrival Time
IAT	Inter-Arrival Time
Arr	Arrival Time
RN(ST)	Random Number for Service Time
ST	Service Time
TSB	Time Service Begins
WT	Waiting Time
TSE	Time Service Ends
TSS	Time Spent in System
ITS	Idle Time of Server
📈 Program Features
Converts random numbers into inter-arrival time.
Converts random numbers into service time.
Simulates customer arrivals.
Determines service start and end times.
Calculates customer waiting time.
Calculates time spent in the system.
Tracks server idle time.
Generates a formatted simulation table.
Calculates statistical summaries.

▶️ How to Run

Make sure Python 3 is installed.

Run the program using:

python single_server_queue.py

The program will display:

The complete simulation table.
The statistical summary.

📚 Conclusion

This experiment demonstrates how a single-server queuing system can be modeled using simulation.

By using random numbers and predefined probability distributions, the program generates customer arrival and service times. It then calculates waiting time, service time, time spent in the system, and server idle time.

This experiment provides a practical understanding of how simulation techniques can be used to analyze the performance of real-world queuing systems.