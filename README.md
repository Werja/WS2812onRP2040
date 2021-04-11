# rp2040-neopixel

With this module you can control up to 4 ws2812 LED strips with one rp2040 microcontroller.

The class uses a maximum of 4 state machines and both cores to achieve a fast output.

Each strip is represented as an object with number of LEDs, pin number, and brightness.

Example:
mystrip = neopixel2040.strip(100,22,0.5)

The following methods are available for the object:

        pset ( position, color ) sets the color at a specific position

        fill ( color ) fills the whole strip with a color

        rotate ( steps ) rotates all pixels forward or backward (+-)

        shift ( steps ) moves all pixels forward or backward (+-)

        rainbow ( [starthue , [endhue]] ) creates the colors of a rainbow (segment)

        show ( ) displays everything

        clear ( ) clears everything
