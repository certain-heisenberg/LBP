Dependencies:
Running the program requires python 3 and the following packages at their latest versions to be installed,
-matplotlib
-cv2
-shapely
-scipy
#NOTE : system must have scipy version:1.1.0 not latest version, higher version has issue with imread module

#Running the program:
Extract the training data under folder train ie. ../code/train/.. and use python main.py to run the program.

The masks for the images will be created and saved in the masks folder.

#Instuctions to run main.py in TERMINAL:
(1) Type command cd (Folder to which 'code' folder is downloaded)/code in TERMINAL
(2) Fill 'train' folder in 'code' with training data
(3) Type python3 main.py
(4) Go to 'mask' folder in 'code' to see the output.

#NOTE: (1)Output for pre-disaster images are binary masked images in gray scale.
       (2)Output for post-disaster images are colored images with color coding representing damage level of buildings.
          Following colors are used to represent damage level:
             RED: Destroyed
             BLUE: Major-damage
             YELLOW: Minor-damage
             PINK: No-damage
