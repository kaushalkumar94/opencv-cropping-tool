import cv2
import  numpy as np
# Global variables
ref_point = []
cropping = False

# Mouse callback function
def click_and_crop(event, x, y, flags, param):
    global ref_point, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE and cropping:
        temp_img = clone.copy()
        cv2.rectangle(temp_img, ref_point[0], (x, y), (0, 255, 0), 2)
        cv2.imshow("window", temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False
        cv2.rectangle(clone, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("window", clone)

# Load image
img = cv2.imread("D:\\PROJECT\\PythonProject\\opencv-cropping-tool\\sample.jpg.jpg")

if img is None:
    print("Image not found!")
    exit()

clone = img.copy()

# Create resizable window
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.imshow("window", img)

cv2.setMouseCallback("window", click_and_crop)

# Main loop
while True:
    key = cv2.waitKey(1) & 0xFF

    # Press 'r' to reset
    if key == ord("r"):
        clone = img.copy()
        cv2.imshow("window", clone)
        ref_point = []

    # Press 'c' to crop and show/save
    elif key == ord("c") and len(ref_point) == 2:
        roi = img[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
        cv2.imshow("Cropped", roi)
        cv2.imwrite("cropped_output.jpg", roi)

    # Press ESC to exit
    elif key == 27:
        break

cv2.destroyAllWindows()
