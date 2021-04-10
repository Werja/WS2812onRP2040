# Using PIO to drive a set of WS2812 LEDs.

import array, time, _thread
from machine import Pin
import rp2

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

thread_active = False
class strip:
    ''' Methods to manipulate neopixel stripes
        pset     ( position, color) 
        fill     ( color )
        rotate   ( steps )
        shift    ( steps )
        rainbow  ( [starthue , [endhue]] )
        show     ()
        clear    ()
        '''
    counter = 0
    def __init__(self,NUM_LEDS, PIN_NUM, brightness):
        self.NUM_LEDS = NUM_LEDS
        self.PIN_NUM = PIN_NUM
        self.brightness = brightness
        if strip.counter < 4:
            # Create the StateMachine with the ws2812 program, outputting on pin
            self.sm = rp2.StateMachine(strip.counter, ws2812, freq=8_000_000, sideset_base=Pin(self.PIN_NUM))
            # Start the StateMachine, it will wait for data on its FIFO.
            self.sm.active(1)
            # Display a pattern on the LEDs via an array of LED RGB values.
            self.ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
            print("Strip with state machine",strip.counter,"on pin",self.PIN_NUM,"active")
        else:
            print("the maximum of 4 state machines was reached ")
        strip.counter += 1
    
    def dimm(self,col):
        r = int(((col >> 8) & 0xFF) * self.brightness)
        g = int(((col >> 16) & 0xFF) * self.brightness)
        b = int((col & 0xFF) * self.brightness)
        return (g<<16) + (r<<8) + b
        
    def show(self):
        global thread_active
        if thread_active:
            self.sm.put(self.ar, 8)
        else:
            thread_active = True
            _thread.start_new_thread(self.put_thread,())
 
    def put_thread(self):
        global thread_active
        self.sm.put(self.ar, 8)
        thread_active = False
        
    def pset(self,i, color):
        self.ar[i] = self.dimm((color[1]<<16) + (color[0]<<8) + color[2])
    
    def fill(self,color):
        for i in range(len(self.ar)):
            self.pset(i, color)
            
    def rotate(self,step):
        cp = array.array("I", self.ar[-step:])
        cp.extend(self.ar[:-step])
        self.ar = cp
        
    def shift(self,step):
        if step >= 0:
            cp = array.array("I",[0 for _ in range(step)])
            cp.extend(self.ar[:-step])
        else:
            cp = array.array("I",self.ar[-step:])
            blackpix = array.array("I",[0]*-step)
            cp.extend(blackpix[:])           
        self.ar = cp
        
    def rainbow(self, start=0, end=360):
        for i in range(self.NUM_LEDS):
            self.pset(i, hue2col(start+(i*(end-start)/self.NUM_LEDS)))
            
    def clear(self):
        self.ar = array.array("I", [0 for _ in range(self.NUM_LEDS)])
        self.sm.put(self.ar, 8)
        time.sleep_ms(10)

##########################################################################

def hue2col(angle):
    rgb = [0,0,0]
    sec = ((0,1),(1,2),(2,0))
    rgb[sec[int(angle/120)][1]]=int(255/120*(angle%120))
    rgb[sec[int(angle/120)][0]]=int(255/120*(120-(angle%120)))
    return (rgb[0],rgb[1],rgb[2])
