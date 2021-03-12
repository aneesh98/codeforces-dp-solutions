# def minnum(sum_req, possible_denoms):
# 	mins_possible = [-1 for i in range(sum_req+1)]
# 	mins_possible[0] = 0
# 	for i in range(1, sum_req+1):
# 		for j in possible_denoms:
# 			if j <= i and mins_possible[i] > mins_possible[i-j] or mins_possible[i] == -1:
# 				mins_possible[i] = 1 + mins_possible[i-j]
# 	return mins_possible[sum_req]

# n=int(input())
# print(minnum(n, [1,5,10,20,50,100]))

def minnum(sum_req, possible_denoms):
	possible_denoms.sort()
	rem = sum_req
	coins = 0
	while rem != 0:
		rem, coin = f(rem, possible_denoms)
		# print(rem, coin)
		coins += coin
	return coins

def f(sum_req, possible_denoms):
	rem = 0
	for i in range(len(possible_denoms) -1, -1, -1):
		# print("Started with ", possible_denoms[i], sum_req)
		m = possible_denoms[i]
		if m<=sum_req:
			rem = sum_req % m
			coins = sum_req // m
			return rem, coins
n=int(input())
print(minnum(n, [1,5,10,20,100]))