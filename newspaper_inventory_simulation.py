
# NEWSPAPER INVENTORY SIMULATION

# Random Numbers (5 days)
newsday_rd = [58, 17, 21, 45, 43]
demand_rd = [93, 63, 31, 19, 91]

# Newspaper Information
purchase_qty = 80
purchase_price = 0.50
selling_price = 0.75
scrap_value = 0.15


# Determine Newsday Type from Random Number
def get_newsday(r):
    if 1 <= r <= 32:
        return "Good"
    elif 33 <= r <= 75:
        return "Fair"
    elif 76 <= r <= 100:
        return "Poor"
    else:
        raise ValueError("Random number must be between 1 and 100")


# Demand Random Number Ranges
demand_ranges = {
    "Good": [
        (1, 3, 40),
        (4, 8, 50),
        (9, 23, 60),
        (24, 43, 70),
        (44, 73, 80),
        (74, 91, 90),
        (92, 100, 100)
    ],

    "Fair": [
        (1, 10, 40),
        (11, 28, 50),
        (29, 68, 60),
        (69, 90, 70),
        (91, 97, 80),
        (98, 100, 90)
    ],

    "Poor": [
        (1, 44, 40),
        (45, 66, 50),
        (67, 82, 60),
        (83, 95, 70),
        (96, 100, 80)
    ]
}


# Determine Demand from Random Number
def get_demand(newsday, r):
    for low, high, demand in demand_ranges[newsday]:
        if low <= r <= high:
            return demand

    raise ValueError("Invalid demand random number")


# Simulation Process
simulation = []

for i in range(5):
    day = i + 1

    rn_type = newsday_rd[i]
    rn_demand = demand_rd[i]

    # Determine Newsday
    newsday = get_newsday(rn_type)

    # Determine Demand
    demand = get_demand(newsday, rn_demand)

    # Calculate Sold and Unsold Newspapers
    sold = min(demand, purchase_qty)
    unsold = max(0, purchase_qty - demand)
    lost_demand = max(0, demand - purchase_qty)

    # Revenue and Cost
    sales_revenue = sold * selling_price
    scrap_revenue = unsold * scrap_value
    cost = purchase_qty * purchase_price

    # Daily Profit
    profit = sales_revenue + scrap_revenue - cost

    simulation.append({
        "day": day,
        "rn_type": rn_type,
        "newsday": newsday,
        "rn_demand": rn_demand,
        "demand": demand,
        "sold": sold,
        "unsold": unsold,
        "lost": lost_demand,
        "sales_revenue": sales_revenue,
        "scrap_revenue": scrap_revenue,
        "cost": cost,
        "profit": profit
    })


# Display Simulation Table
print("\nNEWSPAPER INVENTORY SIMULATION TABLE")
print("-" * 115)

print(
    f"{'Day':<6}"
    f"{'RN(Type)':<11}"
    f"{'Newsday':<10}"
    f"{'RN(Demand)':<12}"
    f"{'Demand':<9}"
    f"{'Sold':<8}"
    f"{'Unsold':<9}"
    f"{'Profit($)':<12}"
)

print("-" * 115)

for s in simulation:
    print(
        f"{s['day']:<6}"
        f"{s['rn_type']:<11}"
        f"{s['newsday']:<10}"
        f"{s['rn_demand']:<12}"
        f"{s['demand']:<9}"
        f"{s['sold']:<8}"
        f"{s['unsold']:<9}"
        f"{s['profit']:<12.2f}"
    )

print("-" * 115)


# Display Revenue Details
print("\nDAILY PROFIT DETAILS")
print("-" * 90)

print(
    f"{'Day':<6}"
    f"{'Sales Revenue':<18}"
    f"{'Scrap Revenue':<18}"
    f"{'Purchase Cost':<18}"
    f"{'Profit':<12}"
)

print("-" * 90)

for s in simulation:
    print(
        f"{s['day']:<6}"
        f"${s['sales_revenue']:<17.2f}"
        f"${s['scrap_revenue']:<17.2f}"
        f"${s['cost']:<17.2f}"
        f"${s['profit']:<11.2f}"
    )

print("-" * 90)


# Statistical Summary
total_demand = sum(s["demand"] for s in simulation)
total_sold = sum(s["sold"] for s in simulation)
total_unsold = sum(s["unsold"] for s in simulation)
total_lost = sum(s["lost"] for s in simulation)

total_sales_revenue = sum(s["sales_revenue"] for s in simulation)
total_scrap_revenue = sum(s["scrap_revenue"] for s in simulation)
total_cost = sum(s["cost"] for s in simulation)
total_profit = sum(s["profit"] for s in simulation)

average_daily_profit = total_profit / len(simulation)


print("\nSTATISTICAL SUMMARY")
print("-" * 45)

print(f"Total Number of Days       : {len(simulation)}")
print(f"Total Demand               : {total_demand}")
print(f"Total Newspapers Sold      : {total_sold}")
print(f"Total Newspapers Unsold    : {total_unsold}")
print(f"Total Lost Demand          : {total_lost}")
print(f"Total Sales Revenue        : ${total_sales_revenue:.2f}")
print(f"Total Scrap Revenue        : ${total_scrap_revenue:.2f}")
print(f"Total Purchase Cost        : ${total_cost:.2f}")
print(f"Total Profit               : ${total_profit:.2f}")
print(f"Average Daily Profit       : ${average_daily_profit:.2f}")

print("-" * 45)
