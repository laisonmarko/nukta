import camera as cr


pointer=cr.ColorTracker()

# pointer.set_window(640,480)              #Set camera window size windth and Height default 640 ,480
# pointer.set_hue(20,160)                  #set minimum and maximum hue  default  hue_min=20, hue_max=160
# pointer.set_saturation(100,255)  	     #Set minimum  and Naximun  saturation default sat_min=100, sat_max=255
# pointer.set_display_threshold(True)	      #Set display threshold true of false
# pointer.set_value(200,256)				  # Set minimum  and Naximun  saturation values val_min=200, val_max=256

pointer.run()
print("hello")