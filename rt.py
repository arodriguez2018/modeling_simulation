import time
import simpy

def example(env):
    start = time.perf_counter()
    yield env.timeout(1)
    end = time.perf_counter
    print('Duration of one sim {end - start}')

import simpy.rt
env = simpy.rt.RealtimeEnvironment(factor=2)
proc = env.process(example(env))
env.run(until=proc)
