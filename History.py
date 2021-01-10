import matplotlib.pyplot as plt


class History:
    def __init__(self, history):
        self.history = history

    def print_plot(self):
        start = 5
        stop = len(self.history)
        step = 2
        plt.figure(figsize=(12, 8))
        plt.plot([i for i in range(start, stop, step)], self.history[start:stop:step], color='black')
        plt.grid(True)
        plt.show()
