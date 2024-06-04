import cv2
import pyrealsense2
from realsense_depth import *

selected_point = (400, 300)

def show_distance(event, x, y, args, params):
    global selected_point
    selected_point = (x, y)


depth_camera = DepthCamera()


cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

while True:
    ret, depth_frame, color_frame = depth_camera.get_frame()

    
    cv2.circle(color_frame, selected_point, 4, (0, 0, 255))
    distance = depth_frame[selected_point[1], selected_point[0]]

    cv2.putText(color_frame, "{}mm".format(distance), (selected_point[0], selected_point[1] - 20), 
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("Depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
