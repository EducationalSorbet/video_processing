import cv2
import os
vid = cv2.VideoCapture("./movie.mp4")

count, success = 0, True
os.makedirs("./path_to_images", exist_ok = True)
while success:
    success, image = vid.read() # Read frame
    if success:
        print("|", end='')
        cv2.imwrite(f"./path_to_images/frame{count}.jpg", image) # Save frame
        count += 1

vid.release()
print("\n\tDONE\n")