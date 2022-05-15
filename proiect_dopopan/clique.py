# Python3 implementation of the approach
MAX = 100;
n = 0;

# Stores the vertices
store = [0] * MAX;

# Graph
graph = [[0 for i in range(MAX)] for j in range(MAX)];

# Degree of the vertices
d = [0] * MAX;

# Function to check if the given set of
# vertices in store array is a clique or not
def is_clique(b):

	# Run a loop for all set of edges
	for i in range(1, b):
		for j in range(i + 1, b):

			# If any edge is missing
			if (graph[store[i]][store[j]] == 0):
				return False;
	
	return True;

# Function to find all the sizes
# of maximal cliques
def maxCliques(i, l):

	# Maximal clique size
	max_ = 0;

	# Check if any vertices from i+1
	# can be inserted
	for j in range(i + 1, n + 1):

		# Add the vertex to store
		store[l] = j;

		# If the graph is not a clique of size k then
		# it cannot be a clique by adding another edge
		if (is_clique(l + 1)):

			# Update max
			max_ = max(max_, l);

			# Check if another edge can be added
			max_ = max(max_, maxCliques(j, l + 1));
		
	return max_;
	
# Driver code
if __name__ == 'clique':
	edges = [[ 1, 2 ],[ 2, 3 ],[ 3, 1 ],[ 4, 3 ],[ 4, 1 ],[ 4, 2 ]];
	size = len(edges);
	n = 4;

	for i in range(size):
		graph[edges[i][0]][edges[i][1]] = 1;
		graph[edges[i][1]][edges[i][0]] = 1;
		d[edges[i][0]] += 1;
		d[edges[i][1]] += 1;
	
	print(maxCliques(0, 1));
