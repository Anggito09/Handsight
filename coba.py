from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("D:\pekerjaan ito\Tugas dan Analisis\HandSight\Model\keras_model.h5", compile=False)

# Load the labels
class_names = open("D:\pekerjaan ito\Tugas dan Analisis\HandSight\Model\labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

# Set the desired window size (e.g., 800x600 pixels)
window_width = 800
window_height = 600
cv2.namedWindow("Webcam Image", cv2.WINDOW_NORMAL)  # Make the window resizable
cv2.resizeWindow("Webcam Image", window_width, window_height)  # Resize window to desired dimensions

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height, 224-width) pixels for the model
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the larger image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the model's input shape.
    image_resized = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image_resized = (image_resized / 127.5) - 1

    # Predict with the model
    prediction = model.predict(image_resized)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

camera.release()
cv2.destroyAllWindows()
