from time import perf_counter

start = perf_counter()
for i in range(1_000_000):
    pass
end = perf_counter()

print("Elapsed:", end - start)
