import matplotlib.pyplot as plt

PADDING = 0.0001


def scatterplot(labels, x_coords, y_coords):
    """Creates a scatterplot using the given labels and data"""

    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(labels, x_coords, y_coords):
        plt.annotate(
            label,
            xy=(x, y),
            xytext=(0, 0),
            textcoords='offset points'
        )

    plt.xlim(x_coords.min() + PADDING, x_coords.max() + PADDING)
    plt.ylim(y_coords.min() + PADDING, y_coords.max() + PADDING)

    plt.show()
