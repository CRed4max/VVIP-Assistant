# importing the module
import screen_brightness_control as sbc
# x = int(input("Enter the brightness level of the screen\n"))
# sbc.set_brightness(x, display=0)
def BrightnessInc():
    current_brightness = sbc.get_brightness()
    sbc.set_brightness(current_brightness[0]+20, display=0)
def BrightnessDec():
    current_brightness = sbc.get_brightness()
    sbc.set_brightness(current_brightness[0]-20, display=0)