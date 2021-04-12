import neopixel2040 as np
import utime
# the 100 pixel stripe needs 3ms for the ws2812 outputting on pin
# 360 x 3ms = 1080ms output time
strip1 = np.strip(100,22,0.1)
start =  utime.ticks_ms()
np_thread_active = True
for i in range(360):
    strip1.fill(np.hue2col(i))
print("script runtime",utime.ticks_ms()-start,"ms without outputting")
start =  utime.ticks_ms()
for i in range(360):
    strip1.fill(np.hue2col(i))
    strip1.show()
print("script runtime",utime.ticks_ms()-start,"ms with outputting")
print("core0 puts",np.core0time)
print("core1 puts",np.core1time)
while np.thread_user != None:
    pass
strip1.clear()