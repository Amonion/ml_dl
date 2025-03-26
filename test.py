import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Hello, Machine Learning!")

data = np.random.randn(100)
plt.hist(data, bins=10)
plt.show()