


<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple library for tracking objects of various sizes base on their colour

Uses of this project:
* Get color object coordinates on the screen or camera device  
* Real time coordinated of moving color object on the screen or camera
* Detect presence of different colors 



### Built With

This library is bult using python
* [Python](https://python.com)




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Numpy
  ```sh
  pip install numpy
  ```
 * Open CV
    ```sh
  pip install cv2
  ```

<!-- ### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
py setup.py   ```
-->



<!-- USAGE EXAMPLES -->
## Usage

If the video source is Camera 

```sh
import Camera as cr



pointer=cr.ColorTracker()

pointer.set_window(640,480)              #Set camera window size windth and Height default 640 ,480
pointer.set_hue(20,160)                  #set minimum and maximum hue  default  hue_min=20, hue_max=160
pointer.set_saturation(100,255)  	     #Set minimum  and Naximun  saturation default sat_min=100, sat_max=255
pointer.set_display_threshold(True)	      #Set display threshold true of false
pointer.set_value(200,256)				  # Set minimum  and Naximun  saturation values val_min=200, val_max=256

pointer.run()
print("hello")
 ```



If The video Source is Screen 

```sh
import screen as cr


pointer=cr.ColorTracker()

pointer.set_window(640,480)              #Set camera window size windth and Height default 640 ,480
pointer.set_hue(20,160)                  #set minimum and maximum hue  default  hue_min=20, hue_max=160
pointer.set_saturation(100,255)  	     #Set minimum  and Naximun  saturation default sat_min=100, sat_max=255
pointer.set_display_threshold(True)	      #Set display threshold true of false
pointer.set_value(200,256)```





<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/laisonmarko/nukta/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Your contribution is  **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact


Project Link: [https://github.com/laisonmarko/nukta](https://github.com/laisonmarko/nukta)




