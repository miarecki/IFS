from random import choices
import matplotlib.pyplot as plt

class Ifs:

    def __init__(self, transformations, probabilities):
        if len(transformations) == 0 or len(probabilities) == 0:
            raise ValueError('Transformations and probabilities lists cannot be empty.')
        if len(transformations) != len(probabilities):
            raise ValueError('Transformations and probabilities lists must have the same length.')

        self.transformations = transformations
        self.probabilities = probabilities

    def new_position(self, x, y):
        trans, = choices(self.transformations, weights=self.probabilities)
        return trans(x, y)

    def make_trajectory(self, iterations):
        x, y = 0, 0
        xs, ys = [], []
        for i in range(iterations):
            xs.append(x)
            ys.append(y)
            x, y = self.new_position(x, y)
        return xs, ys

    def draw(self, iterations = 10000, size = .1, c = 'orange', bgc = 'black', save = ''):
        xs, ys = self.make_trajectory(iterations)
        frac = plt.figure()
        frac.patch.set_facecolor(bgc)
        plt.axis('off')
        plt.scatter(xs, ys, s = size, color = c)
        if save != '': plt.savefig(save)
        plt.show()

#some well known fractals
sierpinski_triangle = Ifs([lambda x, y: (.5 * x, .5 * y),
                lambda x, y: (.5 * x + .5, .5 * y + .5),
                lambda x, y: (.5 * x + 1, .5 * y)],
                [1,1,1])

parsley = Ifs([lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6),
                lambda x, y: (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6),
                lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44),
                lambda x, y: (0, 0.16 * y)],
                [0.25, 0.25, 0.25, 0.25])

dragon_curve = Ifs([lambda x, y: (.5 * x - .5 * y, .5 * x + .5 * y),
                lambda x, y: (1 -.5 * x - .5 * y, .5 * x - .5 * y)],
                [1,1])
