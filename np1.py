# Zadanie 1
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-4, 4, 100)
# y = np.sin(x)
# y1 = 2*np.sin(x)
# y2 = np.sin(2*x)
# plt.plot(x, y2, 'blue', linestyle="-", label="sinx")
# plt.plot(x, y1, 'red', linestyle=":", label="2sin(x)")
# plt.plot(x, y, 'green', linestyle="--", label="sin(2x)")
# plt.legend(title='Wykres')
# plt.show()

# Zadanie 2 -----------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# import math
# a)
# x = np.linspace(-10, 10, 100)
# y = 1/(1+x**2)
# plt.plot(x, y, 'green', linestyle="-", label="1/(1+x^2)")
# plt.legend(title='Wykres')
# plt.show()
# b)
# x = np.linspace(0, 4, 100)
# y1 = x**2
# y2 = math.e**x
# y3 = x**x
# plt.plot(x, y1, 'cyan', linestyle="-", label="x^2")
# plt.plot(x, y2, 'green', linestyle="--", label="e^x")
# plt.plot(x, y3, 'magenta', linestyle="-.", label="x^x")
# plt.legend(title='Wykresy')
# plt.show()
# c)
# x = np.linspace(0, 4, 100)
# y1 = x**2
# y2 = math.e**x
# y3 = x**x
#
# fig, [ax, ax1, ax2] = plt.subplots(nrows=3, ncols=1)
# ax.plot(x, y1, c='green', linestyle="--")
#
# ax.set_xlim([0, 3])
# ax.set_ylim([0, 20])
# ax1.plot(x, y2, c='red', linestyle=":")
#
# ax1.set_xlim([0, 3])
# ax1.set_ylim([0, 20])
# ax2.plot(x, y3, c='cyan', linestyle="-")
#
# ax2.set_xlim([0, 3])
# ax2.set_ylim([0, 20])
# fig.legend([ax, ax1, ax2], title="Wykres", labels=["x^2", "e^x", "x^x"], loc="upper center")
#
# plt.show()

# Zadanie 3
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# a)
# def sinplot(flip=1):
#     x = np.linspace(0, 14, 100)
#     for i in range(1, 5):
#         plt.plot(x, np.sin(x + i* .5)*(7 - i)* (flip))
# sns.set_style("whitegrid")
# sns.set_palette("husl")
# sinplot()
# print(sns.axes_style())
# plt.show()
# b)
# x = np.linspace(-2, 2, 100)
# x_sqrt = np.linspace(0, 2, 100)
# y_x = x
# y_x2 = x**2
# y_x3 = x**3
# y_sqrt = np.sqrt(x_sqrt)
# y_sqrt3 = np.cbrt(x_sqrt)
# sns.set_style("darkgrid")
# plt.figure(figsize=(8, 6))
# plt.plot(x, y_x)
# plt.plot(x, y_x2)
# plt.plot(x, y_x3)
# plt.plot(x_sqrt, y_sqrt)
# plt.plot(x_sqrt, y_sqrt3)
# plt.show()

# Zadanie 4
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import matplotlib.ticker as mtick

# glue = sns.load_dataset("glue")
# # print(glue)

# glue_df = sns.catplot(
# data= glue,
# kind="violin",
# x = 'Year',
# y ='Score',
# hue = 'Encoder',
# col = 'Encoder',
# row = 'Year',
# height=3,
# aspect = 1.5,
# palette=sns.color_palette(['green', 'orange']))

# glue_df.set_axis_labels('Year', 'Scores')
# plt.show()