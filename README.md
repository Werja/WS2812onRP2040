# WS2812onRP2040

With this module you can control up to 4 ws2812 LED strips with one rp2040 microcontroller.

The class strip uses a maximum of 4 state machines and both cores to achieve a fast output.

Each strip is represented as an object with number of LEDs, pin number, and brightness.

Example:

import neopixel2040 as np

mystrip = np.strip(100,22,0.5)

The following methods are available for the strip objects:

        pset ( position, color ) sets the color at a specific position

        fill ( color ) fills the whole strip with a color

        rotate ( steps ) rotates all pixels forward or backward (+-)

        shift ( steps ) moves all pixels forward or backward (+-)

        rainbow ( [starthue , [endhue]] ) creates the colors of a rainbow (segment)

        show ( ) displays everything

        clear ( ) clears everything

The neopixel2040 modul has this functions:

        Wait4ThreadEnd() #wait while core1 is in use
        
        hue2col(angle)   #return a rgb tuple from chromatic circle
        
and predefinded colors COLORS = (RED, YEL, GRE, CYA, BLU, PUR, WHT, BLK)       
