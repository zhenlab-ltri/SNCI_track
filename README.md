## SNCI_track
Align GCaMP and RFP channels, autotrack, and generate traces for C. elegans small-number calcium imaging (SNCI) videos on a single 2D plane.



## Installation

1. Clone git repository:
    navigate to dir you want to clone to

    ```bash
    git clone https://github.com/zhenlab-ltri/SNCI_track
    ```


2. Install following libraries to current environment (prefer conda over pip):
    - cv2 (version 4.2.0 -- otherwise SNCI_track won't run)
    - ffmpeg (use pip to install)
    - imutils
    - numpy
    - matplotlib
    - pandas
    - PIL
    - skimage
    - threading
    


## Running SNCI_track

1. Run JM_areaBasedAlignment.py
    - save input video as single .tif
    - open JM_areaBasedAlignment.py in python IDE of choice (e.g. VScode)
    - follow instructions in script's doc string
    - run


