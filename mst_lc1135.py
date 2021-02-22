class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        parents = [-1 for _ in range(N+1)] # -1 means itself is the source of this subset/pool
        total_costs = 0

		# total number of sources (subsets) is N at beginning, every node is disjoint
        num_of_sources = N

        # sort connections based on costs
        sorted_connects = sorted(connections, key = lambda x: x[2])

        for edge in sorted_connects:
            u, v, cost = edge
            # add this edge
            if self.find_source(u, parents) != self.find_source(v, parents):
                self.union(parents, u, v)
                total_costs += cost
                num_of_sources -= 1

        if num_of_sources > 1:
            return -1
        return total_costs

    # find step
    def find_source(self, v, parents):
        if parents[v] == -1:
            return v
        else: # through a valid path backtracking the source node
            return self.find_source(parents[v], parents)

    # union step
    # if two nodes are not in the same pool yet,
    # connect their source nodes
    def union(self, parents, u, v):
        source_u, source_v = self.find_source(u, parents), self.find_source(v, parents)
        parents[source_u] = source_v
