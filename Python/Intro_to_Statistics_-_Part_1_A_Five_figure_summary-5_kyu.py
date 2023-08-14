# https://www.codewars.com/kata/555c7fa8d8cb57834a000028
# 2023-06-13T08:29:24.057+0000
from math import floor, ceil
class StatisticalSummary(object):
    def __init__(self, seq):
        self.seq = seq
        # Clean sequence
        self.seq = [elem for elem in self.seq if isinstance(elem, (int, float))]
        self.seq = sorted(self.seq)
        
    def get_N(self):
        return len(self.seq)
    
    def get_lower_extreme(self, precision=None):
        return min(self.seq) if precision is None else round(self.get_lower_extreme(), precision)
    
    def get_upper_extreme(self, precision=None):
        return max(self.seq) if precision is None else round(self.get_upper_extreme(), precision)
    
    def get_median(self, precision=None):
        med = self.seq[int((len(self.seq) - 1)/2)] if len(self.seq) % 2 == 1 else 0.5 * (self.seq[int(len(self.seq)/2)] + self.seq[int(len(self.seq)/2 - 1)])
        return med if precision is None else round(self.get_median(), precision)
    
    def get_lower_quartile(self, precision=None):
        # Get the quarter point
        quarter_point = (len(self.seq) - 1) / 4
        q1 = self.seq[floor(quarter_point)] + quarter_point % 1 * (self.seq[ceil(quarter_point)] - self.seq[floor(quarter_point)])
        return q1 if precision is None else round(self.get_lower_quartile(), precision)
    
    def get_upper_quartile(self, precision=None):
        # Get the 3/4 point
        three_quarter_point = (len(self.seq) - 1) * 3 / 4
        q3 = self.seq[floor(three_quarter_point)] + three_quarter_point % 1 * (self.seq[ceil(three_quarter_point)] - self.seq[floor(three_quarter_point)])
        return q3 if precision is None else round(self.get_upper_quartile(), precision)

    def five_figure_summary(self, precision=None):
        N = self.get_N()
        LE = self.get_lower_extreme(precision)
        UE = self.get_upper_extreme(precision)
        LQ = self.get_lower_quartile(precision)
        med = self.get_median(precision)
        UQ = self.get_upper_quartile(precision)
            
        return (N, LE, UE, LQ, med, UQ)
