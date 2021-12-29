# WS2812onRP2040

With this module you can control up to 4 ws2812 LED strips with one rp2040 microcontroller.

The class strip uses a maximum of 4 state machines and both cores to achieve a fast output.

Each strip is represented as an object with number of LEDs, pin number, and brightness.

Example:

import WS2812onRP2040 as np

mystrip = np.strip(100,22,0.5)

The following methods are available for the strip objects:

        Methods to manipulate 2812 stripes:
        
        pset     ( position, color,[optional show(0 or 1)]) 
        
        fill     ( (r,g,b),[optional show(0 or 1)] )
        
        rotate   ( steps,[optional show(0 or 1)] )
        
        shift    ( steps,[optional show(0 or 1)] )
        
        rainbow  ( [starthue , [endhue]],[optional show(0 or 1)] )
        
        show     ()
        
        Properties:
        
        BRIGHTNESS (value between 0 and 1)
        

The WS2812onRP2040 modul has this functions:
        
        hue2col(angle)   #return a rgb tuple from chromatic circle
        
        and predefinded colors COLORS = (RED, YEL, GRE, CYA, BLU, PUR, WHT, BLK)       
