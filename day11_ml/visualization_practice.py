import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv


def matplotlib_basic():
    """선 그래프 (y=x, y=x^2)"""
    x = np.arange(10)

    fig, ax = plt.subplots()

    ax.plot(x, x, marker='o', color='blue', linestyle=':', label='y=x')
    ax.plot(x, x**2, marker='^', color='red', linestyle='--', label='y=x^2')

    ax.set_title('Line Graph')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 100)

    ax.legend(loc='upper left', shadow=True, fancybox=True)

    fig.savefig("line_plot.png")
    plt.show()


def matplotlib_multi():
    """여러 그래프 (scatter, bar, stacked bar, histogram)"""

    data_x = []
    data_y = []

    with open('C:/msj/0317/Pandas-practice-main/data/data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_x.append(float(row[0]))
            data_y.append(float(row[1]))

    fig, axes = plt.subplots(2, 2)

    # Scatter
    colors = np.random.randint(0, 100, 500)
    axes[0, 0].scatter(data_x, data_y, c=colors, s=2, alpha=0.7)
    axes[0, 0].set_title("Scatter")

    # Bar
    bar_x = np.arange(10)
    axes[0, 1].bar(bar_x, bar_x**2)
    axes[0, 1].set_title("Bar")

    # Stacked Bar
    x = np.array([3, 2, 1])
    y = np.array([2, 3, 2])
    z = np.array([1, 3, 4])

    data1 = [x, y, z]
    x_ax = np.arange(3)

    for i in range(len(data1)):
        axes[1, 0].bar(x_ax, data1[i], bottom=np.sum(data1[:i], axis=0))

    axes[1, 0].set_xticks(x_ax)
    axes[1, 0].set_xticklabels(['A', 'B', 'C'])
    axes[1, 0].set_title("Stacked Bar")

    # Histogram
    data = np.array(data_x)
    axes[1, 1].hist(data, 50)
    axes[1, 1].set_title("Histogram")

    fig.tight_layout()
    fig.savefig("multi_plot.png")
    plt.show()


def seaborn_plot():
    """Seaborn 시각화"""

    df = sns.load_dataset('tips')

    # regplot
    sns_plot = sns.regplot(
        x='total_bill',
        y='tip',
        data=df,
        color='orange',
        line_kws={'color': 'red'}
    )

    fig = sns_plot.get_figure()
    fig.savefig("regplot.png")
    plt.show()

    # countplot
    sns_plot_size = sns.countplot(x="size", data=df)

    fig = sns_plot_size.get_figure()
    fig.savefig("countplot.png")
    plt.show()

    # jointplot
    g = sns.jointplot(x='total_bill', y='tip', kind='resid', data=df)
    g.savefig("jointplot.png")
    plt.show()


def main():
    matplotlib_basic()
    matplotlib_multi()
    seaborn_plot()


if __name__ == "__main__":
    main()