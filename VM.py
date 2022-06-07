import statistics
import matplotlib.pyplot as plt


class VM:

    def __init__(self):
        self.glob = []
        self.local = []
        self.temp = []
        self.pointer = []
        self.gosub = []
        self.curr_func = None
        self.era = 0
# pendiente de dise;ar
