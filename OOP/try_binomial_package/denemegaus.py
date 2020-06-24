from bg_dist import Gaussian, Binomial

binomial = Binomial()
print(binomial.pdf(5))
binomial.read_data_file('numbers_binomial.txt')
print(binomial.calculate_mean())
print(binomial.calculate_stdev())
print(binomial.pdf(2))
binomial.plot_pdf()


gaus = Gaussian()
gaus.read_data_file('numbers.txt')
print(gaus.calculate_stdev())
print(gaus.calculate_mean())
print(gaus.plot_histogram())
print(gaus.pdf(2))
print(gaus.plot_histogram_pdf(2))

