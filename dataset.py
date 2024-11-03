import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 20
imgSize = 300
folder = r"C:\\Users\\LENOVO\\OneDrive\\Documents\\HandSight\\Dataset\\a"

counter = 0

def process_and_save_hand(hand, img, folder, counter):
    x, y, w, h = hand['bbox']
    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
    imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

    # Ensure the cropping is within the image bounds
    if y - offset < 0: y = offset
    if x - offset < 0: x = offset
    if y + h + offset > img.shape[0]: h = img.shape[0] - y - offset
    if x + w + offset > img.shape[1]: w = img.shape[1] - x - offset

    imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
    aspectRatio = h / w

    if aspectRatio > 1:
        k = imgSize / h
        wCal = math.ceil(k * w)
        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
        wGap = math.ceil((imgSize - wCal) / 2)
        imgWhite[:, wGap:wCal + wGap] = imgResize
    else:
        k = imgSize / w
        hCal = math.ceil(k * h)
        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
        hGap = math.ceil((imgSize - hCal) / 2)
        imgWhite[hGap:hCal + hGap, :] = imgResize

    cv2.imshow(f"ImageCrop_{counter}", imgCrop)
    cv2.imshow(f"ImageWhite_{counter}", imgWhite)

    # Save the processed hand image
    cv2.imwrite(f'{folder}/Image_{time.time()}_{counter}.jpg', imgWhite)
    print(f'Saved image {counter}')

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        for i, hand in enumerate(hands):
            process_and_save_hand(hand, img, folder, counter)
            counter += 1
    
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        for hand in hands:
            process_and_save_hand(hand, img, folder, counter)
            counter += 1

cap.release()
cv2.destroyAllWindows()
