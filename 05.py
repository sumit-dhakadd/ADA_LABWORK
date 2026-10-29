
def fractional_knapsack(w, v, cap):
    items = [(v[i] / w[i], w[i], v[i]) for i in range(len(w))]
    items.sort(reverse=True)

    profit = 0

    for ratio, weight, value in items:
        take = min(weight, cap)
        profit += take * ratio
        cap -= take

        if cap == 0:
            break

    return float(profit)


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, values, capacity))
