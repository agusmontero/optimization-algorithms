import networkx as nx
from main.branch_and_bound import BranchAndBound


class TravelingSalesmanProblemSolver(BranchAndBound):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.n = graph.number_of_nodes()

    def _initial_state(self):
        return []

    def _is_solution(self, state):
        return self._visited_cities(state) == self.n

    def _visited_cities(self, state):
        return len(set(state))

    def _evaluate(self, state):
        current_cost = sum(
            self.graph[state[i]][state[i + 1]]["weight"] for i in range(len(state) - 1)
        )
        current_cost += self.graph[state[-1]][state[0]]["weight"]
        return current_cost

    def _branch(self, state):
        if not state:
            return [[next_city] for next_city in range(self.n)]
        else:
            return [
                state + [next_city]
                for next_city in range(self.n)
                if next_city not in state
            ]

    def _bound(self, state):
        if not state:
            return 0

        cost = sum(
            self.graph[state[i]][state[i + 1]]["weight"] for i in range(len(state) - 1)
        )
        last_state = state[-1]
        min_outgoing_edge = (
            min(
                [
                    self.graph[last_state][v]["weight"]
                    for v in range(self.n)
                    if v not in state
                ]
            )
            if len(state) < self.n
            else 0
        )
        return cost + min_outgoing_edge
