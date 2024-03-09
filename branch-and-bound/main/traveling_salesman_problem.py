import networkx as nx
from main.branch_and_bound import BranchAndBound


class TravelingSalesmanProblemSolver(BranchAndBound):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.n = graph.number_of_nodes()
        self.root_node = []

    def _is_solution(self, nodes):
        return len(nodes) == self.n and len(set(nodes)) == self.n

    def _evaluate(self, nodes):
        current_cost = sum(
            self.graph[nodes[i]][nodes[i + 1]]["weight"] for i in range(len(nodes) - 1)
        )
        current_cost += self.graph[nodes[-1]][nodes[0]]["weight"]
        return current_cost

    def _branch(self, nodes):
        if not nodes:
            return [[next_node] for next_node in range(self.n)]
        else:
            return [
                nodes + [next_node]
                for next_node in range(self.n)
                if next_node not in nodes
            ]

    def _bound(self, nodes):
        if not nodes:
            return 0
        cost = sum(
            self.graph[nodes[i]][nodes[i + 1]]["weight"] for i in range(len(nodes) - 1)
        )
        last_node = nodes[-1]
        min_outgoing_edge = (
            min(
                [
                    self.graph[last_node][v]["weight"]
                    for v in range(self.n)
                    if v not in nodes
                ]
            )
            if len(nodes) < self.n
            else 0
        )
        return cost + min_outgoing_edge
