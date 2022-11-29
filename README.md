# Fruit detection using yolov4

This is a streamlit app helps you to detect fruits in images. we have 3 class for which we can detect in images.

1. apple
2. banana
3. orange

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Download and install [Python 3.10.0](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)

### Installation

1. First check python version in terminal, if it's 3.10.0 then go ahead.
   ```sh
   python --version 
   ```

2. Go to folder where you want to clone this repository and use below command to clone this repo to your local machine.
   ```sh
   git clone https://github.com/ipiyushvaghela/FruitDetectionYOLOv4.git
   ```
3. Create virtual Environment 
   ```sh
   python -m venv venv4fruit --system-site-packages
   ```

   To Activate our virtual environment we use 
   ```sh
   venv4fruit/Script/Activate.bat
   ```
4. Install packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
4. Now check if streamlit is installed properly or not.
   ```sh
   streamlit version
   ```

## Usage

1. change your working dir to streamlit and then change paths of model in `app.py` file.
2. Run below command in terminal to run streamlit application. 
   ```sh
   streamlit run app.py
   ```
Now we are all set to go. just upload the image of any given class and it will classify that image and also it gives other 5 possible classes from which image could belong to.

![App Screenshot](https://github.com/ipiyushvaghela/static/blob/main/fruit_detection_yolov4/demo.png?raw=true)
![App Screenshot](https://github.com/ipiyushvaghela/static/blob/main/fruit_detection_yolov4/high_confidence.png?raw=true)
![App Screenshot](https://github.com/ipiyushvaghela/static/blob/main/fruit_detection_yolov4/low_confidence.png?raw=true)

## Info about other folders
1. Folder named `YOLOv4_Setup` contains 3 files from which `yolov4_setup_colab.ipynb` can be used if you want to setup yolov4 to colab. other file is `drawingRctWithText.ipynb` which contains code for drawing ractangle box around the object given that we give image and .txt(yolo4 formate) as input
2. Folder named `fruit_images` contains some fruit images for testing.

## Contact

Piyush Vaghela - [@ipiyushvaghela](https://twitter.com/ipiyushvaghela) - ipiyushvaghela@gmail.com

Project Link -  [github.com/ipiyushvaghela/FruitDetectionYOLOv4](https://github.com/ipiyushvaghela/FruitDetectionYOLOv4.git)