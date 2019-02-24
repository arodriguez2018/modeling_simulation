import time
import simpy.rt

def example(env):
    start = time.perf_counter()
    yield env.timeout(1)
    end = time.perf_counter()
    print(f'Duration of one simulation time unit: {end - start} sec')

#import simpy.rt
env = simpy.rt.RealtimeEnvironment(factor=1)
proc = env.process(example(env))
env.run(until=proc)
