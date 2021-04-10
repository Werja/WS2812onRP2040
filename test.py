import neopixel2040 as np
import time

strip1 = np.strip(1000,22,0.1)
strip2 = np.strip(1000,21,0.1)
strip1.rainbow()
strip2.rainbow(90)
start =  time.time_ns() // 1_000_000
for i in range(100):
    strip1.show()
    strip2.show()
print((time.time_ns() // 1_000_000)-start,"ms")
strip1.clear()
strip2.clear()
time.sleep(1)