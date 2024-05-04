from abc import ABC, abstractmethod


class BranchAndBound(ABC):
    def __init__(self):
        self.best_solution = None
        self.best_cost = float("inf")

    def solve(self):
        self._search(self._initial_state())
        return self.best_solution, self.best_cost

    def _search(self, state):
        if self._is_solution(state) and self._is_better(state):
            self.best_solution = state
            self.best_cost = self._evaluate(state)
            return

        for next_state in self._branch(state):
            if self._bound(next_state) < self.best_cost:
                self._search(next_state)

    def _is_better(self, state):
        current_cost = self._evaluate(state)
        return current_cost < self.best_cost

    @abstractmethod
    def _initial_state(self):
        raise NotImplementedError

    @abstractmethod
    def _is_solution(self, state):
        raise NotImplementedError

    @abstractmethod
    def _evaluate(self, state):
        raise NotImplementedError

    @abstractmethod
    def _branch(self, state):
        raise NotImplementedError

    @abstractmethod
    def _bound(self, state):
        raise NotImplementedError
