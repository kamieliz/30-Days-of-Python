# recreate statistics module as a class
import math
class Stat:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def min(self):
        return min(self.data)
    def max(self):
        return max(self.data)
    def range(self):
        return max(self.data) - min(self.data)
    def mean(self):
        return round(sum(self.data) / len(self.data))
    def median(self):
        sortedLst = sorted(self.data)
        length = len(self.data)
        index = (length - 1) // 2
        if (length % 2):
            return sortedLst[index]
        else:
            return (sortedLst[index] + sortedLst[index + 1])/2.0
    def mode(self):
        return max(set(self.data), key= self.data.count)
    def var(self):
        n = len(self.data)
        mean = sum(self.data) / n
        deviations = [(x - mean) ** 2 for x in self.data]
        variance = sum(deviations)/n
        return round(variance, 1)
    def std(self):
        var = self.var()
        std_dev = math.sqrt(var)
        return round(std_dev,1)
    def freq_dist(self):
        flist = []
        for item in self.data:
            flist.append(item)
        freq = [flist.count(f) for f in flist]
        return freq
    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum()) 
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode()) 
        print('Standard Deviation: ', self.std()) 
        print('Variance: ', self.var()) 
        print('Frequency Distribution: ', self.freq_dist())
    
    


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
s = Stat(ages)
print(s.describe())
