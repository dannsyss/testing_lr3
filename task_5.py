import matplotlib.pyplot as plt

data = [4, 1, 8, 3, 7]

plt.barh(range(len(data)), data)

plt.show()