import math
import matplotlib.pyplot as plt

from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    def __init__(self, probability=0.5, size=10):

        self.p = probability
        self.n = size
        Distribution.__init__(self, mu=0, sigma=1)

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        binomial_mean = self.p * self.n
        self.mean = binomial_mean
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        self.stdev = round(math.sqrt(self.n * self.p * (1 - self.p)), 2)
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        self.n = len(self.data)
        self.p = sum(self.data) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        fig, ax = plt.subplots()
        ax.hist(self.data)
        ax.set_xlabel = 'data'
        ax.set_ylabel = 'count'
        ax.set_title = 'Histogram of the data'
        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        factorial_part = math.factorial(self.n) / ((math.factorial(self.n - k)) * math.factorial(k))
        probability_part = (self.p ** k) * ((1 - self.p) ** (self.n - k))

        return factorial_part * probability_part

    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        list_x, list_y = [], []
        for k in range(self.n+1):
            y = self.pdf(k)
            list_x.append(k)
            list_y.append(y)

        fig, ax = plt.subplots()
        ax.bar(list_x, list_y)
        ax.set_xlabel = 'data'
        ax.set_ylabel = 'count'
        ax.set_title = 'Pdf plot'
        plt.show()

        return list_x, list_y

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n

        return result

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """
        return 'mean {}, standart deviation {}, p {}, n {}'.format(self.mean, self.stdev, self.p, self.n)
