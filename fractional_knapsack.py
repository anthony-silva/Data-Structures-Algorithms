'''
 python3
 Author: Anthony Silva

 Description: A thief finds much more loot than his bag can fit. Help him 
	to find the most valuable combination of items assuming that any 
	fraction of a loot item can be put into his bag. (Implement a greedy
	algorithm for the fractional knapsack problem)

 Input: The first line of the input contains the number 𝑛 of items and the 
	capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and 
	weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the 
	value and the weight of 𝑖-th item, respectively.
 
 Output: Output the maximal value of fractions of items that fit into the 
	knapsack. The absolute value of the difference between the answer 
	of your program and the optimal value should be at most 10^(-3).
	To ensure this, output the answer with at least four digits after
	the decimal point
	
 Contraints: 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊  ≤ 2·106; 0 ≤ 𝑣𝑖 ≤2·106, 0 < 𝑤𝑖 ≤2·106 
	for all 1 ≤ 𝑖 ≤ 𝑛. All the numbers are integers.
'''


def get_optimal_value(capacity, weights, values):
    opt_value = 0
    items = list(zip(values, weights))
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    values = [item[0] for item in items]
    weights = [item[1] for item in items]

    for value, weight in zip(values, weights):
        if capacity == 0:
            return opt_value
        min_weight = min(weight, capacity)
        opt_value += min_weight * (value / weight)
        weight -= min_weight
        capacity -= min_weight

    return opt_value


if __name__ == "__main__":
    data = [int(x) for x in input().split()]
    n, capacity = data[0:2]
    values = [0] * n
    weights = [0] * n
    for i in range(n):
    	values[i], weights[i] = map(int, input().split())

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
