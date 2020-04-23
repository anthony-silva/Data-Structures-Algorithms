'''
 python3
 Author: Anthony Silva

 Description: You are going to travel to another city that is located 𝑑 miles 
	away from your home city. Your car can travel at most 𝑚 miles on a full
 	tank and you start with a full tank. Along your way, there are gas 
	stations at distances stop1, stop2, . . . , stop𝑛 from your home city. 
	What is the minimum number of refills needed?

 Input: The first first line contains an integer 𝑑. The second line contains 
	an integer 𝑚. The third line specifies an integer 𝑛. Finally, the last 
	line contains integers stop1, stop2, . . . , stop𝑛.
 
 Output: Assuming that the distance between the cities is 𝑑 miles, a car can 
	 travel at most 𝑚 miles on a full tank, and there are gas stations at 
	 distances stop1 , stop2 , . . . , stop𝑛 along the way, output the 
	 minimum number of refills needed. Assume that the car starts with a 
	 full tank. If it is not possible to reach the destination, output −1.
'''

def MinRefills(stops, n, L):
	# initialize values
	numRefills = 0
	currentRefill = 0

	# implement greedy algorithm for optimal refuel
	while currentRefill <= n:
		lastRefill = currentRefill
		while (currentRefill <= n and stops[currentRefill+1]-stops[lastRefill] <= L):
			currentRefill += 1
		if currentRefill == lastRefill: # case impossible to reach next stop
			return -1
		if currentRefill <= n:
			numRefills += 1

	return numRefills


if __name__ == "__main__":
	d = int(input()) # total length of drive from origin
	L = int(input()) # max mileage on full tank
	n = int(input()) # number of gas stops on the route
	stops = [int(x) for x in input().split()] # distance of each gas stop from origin
	stops.insert(0,0) # insert initial distance from origin
	stops.append(d) # append distance of destination from origin

	print(MinRefills(stops, n, L))
