class Solution:
    def __edge_dfs_helper (self, curr_node, graph, ans):
        while (len(graph[curr_node]) > 0):
            next_node = heappop(graph[curr_node])
            self.__edge_dfs_helper(next_node, graph, ans)
        ans.appendleft(curr_node)
        return ans

    def findItinerary (self, tickets: List[List[str]]) -> List[str]:
        graph, ans = {}, deque()
        for start, end in tickets:
            if (start not in graph):
                graph[start] = [end]
            else: heappush(graph[start], end)
            if (end not in graph): graph[end] = []
        return self.__edge_dfs_helper("JFK", graph, ans)
        