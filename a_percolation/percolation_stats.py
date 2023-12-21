import math
import random

from a_percolation.percolation import Percolation


class PercolationStats:

    def __init__(self, n: int, trials: int):
        """perform independent trials on an n-by-n grid"""
        self.n = n
        self.trials = trials
        self.percolation = Percolation(self.n)

    def mean(self, number_of_open_sites: int) -> float:
        """sample mean of a_percolation threshold"""
        return number_of_open_sites / (self.n * self.n)

    @staticmethod
    def stddev(percolation_thresholds: list, mean_threshold: float) -> float:
        """sample standard deviation of a_percolation threshold"""
        variance_threshold = sum(
            (x - mean_threshold) ** 2 for x in percolation_thresholds) / (len(percolation_thresholds) - 1)
        return math.sqrt(variance_threshold)

    @staticmethod
    def confidence_lo(mean_threshold: float, margin_of_error: float) -> float:
        """low endpoint of 95% confidence interval"""
        return mean_threshold - margin_of_error

    @staticmethod
    def confidence_hi(mean_threshold: float, margin_of_error: float) -> float:
        """high endpoint of 95% confidence interval"""
        return mean_threshold + margin_of_error

    @staticmethod
    def margin_of_error(mean_threshold: float, s: float) -> float:
        """returns the margin of error"""
        return 1.96 * s / math.sqrt(mean_threshold)

    def run(self):
        """Run the simulation"""
        # open random sites until the system percolates
        percolation_thresholds = []

        for i in range(self.trials):
            percolation = Percolation(self.n)
            percolates = False
            while not percolates:
                percolation.open(random.randint(0, self.n - 1), random.randint(0, self.n - 1))
                percolates = percolation.percolates()

            threshold = self.mean(number_of_open_sites=percolation.number_of_open_sites())
            percolation_thresholds.append(threshold)

        mean_threshold = sum(percolation_thresholds) / len(percolation_thresholds)
        std_dev_threshold = self.stddev(percolation_thresholds=percolation_thresholds, mean_threshold=mean_threshold)
        margin_of_error = self.margin_of_error(mean_threshold=mean_threshold, s=std_dev_threshold)

        low_confidence_interval = self.confidence_lo(mean_threshold=mean_threshold, margin_of_error=margin_of_error)
        hi_confidence_interval = self.confidence_hi(mean_threshold=mean_threshold, margin_of_error=margin_of_error)

        print(f"mean\t\t\t\t= {mean_threshold}")
        print(f"stddev\t\t\t\t= {std_dev_threshold}")
        print(f"95% confidence interval\t= [{low_confidence_interval}, {hi_confidence_interval}]")
