# SINGLE - SERVER QUEUE SIMULATION

arrival_rd = [861, 341, 142, 156, 476, 271, 178]  # RN(IAT) customers 2-8
service_rd = [12, 31, 27, 69, 91, 55, 77, 54]  # RN(ST) customers 1-8


def get_iat(r):
    if r <= 125:
        return 1
    elif r <= 250:
        return 2
    elif r <= 375:
        return 3
    elif r <= 500:
        return 4
    elif r <= 625:
        return 5
    elif r <= 750:
        return 6
    elif r <= 875:
        return 7
    else:
        return 8


def get_st(r):
    if r <= 10:
        return 1
    elif r <= 30:
        return 2
    elif r <= 60:
        return 3
    elif r <= 85:
        return 4
    elif r <= 95:
        return 5
    else:
        return 6


customers = []
arrival = 0
prev_end = 0

for i in range(8):
    cust = i + 1

    if cust == 1:
        rn_iat_val, iat = "-", 0
    else:
        rn_iat_val = arrival_rd[i - 1]
        iat = get_iat(rn_iat_val)
        arrival += iat

    rn_st_val = service_rd[i]
    st = get_st(rn_st_val)

    tsb = max(arrival, prev_end)       # Time Service Begins
    wt = tsb - arrival                 # Waiting Time
    tse = tsb + st                     # Time Service Ends
    tss = tse - arrival                # Time Spent in System
    its = max(0, arrival - prev_end)   # Idle Time of Server

    customers.append({
        "cust": cust,
        "rn_iat": rn_iat_val,
        "iat": iat,
        "arr": arrival,
        "rn_st": rn_st_val,
        "st": st,
        "tsb": tsb,
        "wt": wt,
        "tse": tse,
        "tss": tss,
        "its": its
    })

    prev_end = tse


# Display simulation table

print("\nSINGLE-SERVER QUEUE SIMULATION TABLE")
print("-" * 95)

print(
    f"{'Cust':<6}"
    f"{'RN(IAT)':<10}"
    f"{'IAT':<6}"
    f"{'Arr':<6}"
    f"{'RN(ST)':<10}"
    f"{'ST':<6}"
    f"{'TSB':<6}"
    f"{'WT':<6}"
    f"{'TSE':<6}"
    f"{'TSS':<6}"
    f"{'ITS':<6}"
)

print("-" * 95)

for c in customers:
    print(
        f"{c['cust']:<6}"
        f"{str(c['rn_iat']):<10}"
        f"{c['iat']:<6}"
        f"{c['arr']:<6}"
        f"{c['rn_st']:<10}"
        f"{c['st']:<6}"
        f"{c['tsb']:<6}"
        f"{c['wt']:<6}"
        f"{c['tse']:<6}"
        f"{c['tss']:<6}"
        f"{c['its']:<6}"
    )

print("-" * 95)


# Statistical Summary

total_waiting = sum(c["wt"] for c in customers)
total_iat = sum(c["iat"] for c in customers)
total_service = sum(c["st"] for c in customers)
total_system = sum(c["tss"] for c in customers)
total_idle = sum(c["its"] for c in customers)

average_waiting = total_waiting / len(customers)
average_iat = total_iat / len(customers)
average_service = total_service / len(customers)
average_system = total_system / len(customers)

waited_customers = [c["wt"] for c in customers if c["wt"] > 0]

if waited_customers:
    average_waiting_when_waited = (
        sum(waited_customers) / len(waited_customers)
    )
else:
    average_waiting_when_waited = 0


print("\nSTATISTICAL SUMMARY")
print("-" * 40)

print(f"Average Waiting Time        : {average_waiting:.2f} min")
print(f"Average IAT                 : {average_iat:.2f} min")
print(f"Average Service Time        : {average_service:.2f} min")
print(f"Average Time in System      : {average_system:.2f} min")
print(f"Total Server Idle Time      : {total_idle} min")
print(
    f"Average Waiting Time "
    f"(Customers Who Waited)     : {average_waiting_when_waited:.2f} min"
)

print("-" * 40)