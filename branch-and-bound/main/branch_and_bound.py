from abc import ABC, abstractmethod


class BranchAndBound(ABC):
    def __init__(self):
        self.best_solution = None
        self.best_cost = float('inf')
        self.root_node = None

    def solve(self):
        self._search(self.root_node)
        return self.best_solution, self.best_cost

    def _search(self, node):
        if self._is_solution(node) and self._is_better(node, self.best_solution):
            self.best_solution = node
            self.best_cost = self._evaluate(node)
            return

        for next_state in self._branch(node):
            if self._bound(next_state) < self.best_cost:
                self._search(next_state)

    def _is_better(self, node, best_solution):
        current_cost = self._evaluate(node)
        return current_cost < self.best_cost

    @abstractmethod
    def _is_solution(self, node):
        raise NotImplementedError

    @abstractmethod
    def _evaluate(self, node):
        raise NotImplementedError

    @abstractmethod
    def _branch(self, node):
        raise NotImplementedError

    @abstractmethod
    def _bound(self, node):
        raise NotImplementedError
