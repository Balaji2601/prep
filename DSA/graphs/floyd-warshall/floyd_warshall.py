# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

class Solution:
	def floydWarshall(self, dist):
		#Code here
		n = len(dist)

        # for shortest path between i,j we are going through each other vertex via 
        # ie i ---> via ---> j
		for via in range(n):
		    for i in range(n):
		        for j in range(n):
					# read qn why this if condition is written 
                    # after reading it we can see
                    # 10**8 + 10**8 will become something instead of 10**8 right
		            if dist[i][via] != 10**8 and dist[via][j] != 10**8:
		                dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])