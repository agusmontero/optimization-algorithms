import unittest
import numpy as np
import networkx as nx
from main.traveling_salesman_problem import TravelingSalesmanProblemSolver


class TestTravelingSalesmanProblemSolver(unittest.TestCase):
    def test_small_instance(self):
        costs_matrix = np.array(
            [
                [0, 29, 20, 21],
                [29, 0, 15, 17],
                [20, 15, 0, 28],
                [21, 17, 28, 0],
            ]
        )
        optimal_solution = [0, 2, 1, 3]
        optimal_cost = 20 + 15 + 17 + 21

        tsp_instance = nx.from_numpy_array(costs_matrix)

        solver = TravelingSalesmanProblemSolver(tsp_instance)
        best_solution, best_cost = solver.solve()

        self.assertEqual(best_cost, optimal_cost)
        self.assertEqual(best_solution, optimal_solution)


if __name__ == '__main__':
    unittest.main()