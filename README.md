# Cam-Scanner-Uni
# License Plate Recognition Camera
This project builds a camera that can automatically read and recognize license plates on cars.
### Overview
The camera uses computer vision and machine learning models to detect and read license plates in real-time video streams. Key features:
Uses OpenCV for computer vision techniques like image processing, object detection etc.
Employs a custom trained YOLO v5 model to detect license plates in video frames
Applies optical character recognition (OCR) to extract the license plate text
Can achieve 90%+ accuracy in ideal lighting conditions

### Features
License Plate Recognition: Utilizes image processing to read and extract information from car license plates.
Python Backend: Employs Python for the backend logic and handling of the recognition process.
Roboflow Integration: Utilizes Roboflow for its image processing capabilities and optimizations.
HTML/CSS Frontend: Provides a user-friendly interface designed using HTML and CSS.
## Getting Started
### Prerequisites
You need Python 3.6 or later and the following packages:
- OpenCV
- NumPy
- TensorFlow (for YOLOv5 model)
- easyOCR (for OCR)
 
 It's recommended to use a GPU for efficient performance.
### Usage
1. Clone the repo
1. Install dependencies
1. Download pre-trained YOLOv5 weights file (provided in repo/models dir)
1. Run python app.py with appropriate command line args
1. Point camera at cars to detect and recognize license plates!
### Custom Training
The pre-trained model works well but you can improve accuracy by re-training the YOLOv5 model on your own license plate datasets. The repo includes the scripts and annotations for re-training.
### Contributing
Pull requests are welcome! Feel free to contribute to this project.
### License
MIT


# server

### quick run

1. ``` git clone https://github.com/NaviW-D/Cam-Scanner-Uni.git ```

2. ``` cd  Cam-Scanner-Uni```
    or ``` cd Cam-Scanner-Uni-navid```
3. ``` cd server ```
4. ``` pip install -r requirements.txt ```
5. ``` cd camscan ```
6. ``` ./manage.py makemigrations ```
7. ``` ./manage.py migrate ```
8. ``` ./manage.py createsuperuser ```
9. complete answer
10. ``` ./manage.py runserver ```
11. open http://127.0.0.1:8000/admin/



# todo
- [x] Start
- [x] make simple backend
- [x] create ui and front
- [ ] create computer vision to get automatic car tag

# video 
[![Watch the video](https://i.stack.imgur.com/IMG_0349.HEIC)](IMG_0350%20copy.mp4)
https://github.com/NaviW-D/Cam-Scanner-Uni/blob/main/static/IMG_0349.HEIC
