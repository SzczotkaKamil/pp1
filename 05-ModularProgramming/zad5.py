import statistics
zarobki = [21600,4350,3920,5590,3250,4010]
m = statistics.mean(zarobki)
print(m)
print(statistics.median(zarobki))
print(statistics.variance(zarobki,m))