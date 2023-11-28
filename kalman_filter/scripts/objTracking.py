#!/usr/bin/python3

import cv2
from Detector import detect
from KalmanFilter import KalmanFilter
from std_msgs.msg import Float64MultiArray
import rospy
import csv
import matplotlib.pyplot as plt
import numpy as np

def main():
    rospy.init_node('obj_tracking')

    VideoCap = cv2.VideoCapture('video/randomball.avi')
    ControlSpeedVar = 100
    pub = rospy.Publisher('kalman_filter/position', Float64MultiArray, queue_size=1)

    HiSpeed = 100
    KF = KalmanFilter(0.1, 1, 1, 1, 0.1, 0.1)
    debugMode = 1

    # Lists to store data for plotting
    x_values = []
    y_values = []
    x1_values = []
    y1_values = []

    while True:
        ret, frame = VideoCap.read()

        if not ret:
            print("Error: Couldn't read frame. Exiting...")
            break

        centers = detect(frame, debugMode)

        if len(centers) > 0:
            cv2.circle(frame, (int(centers[0][0]), int(centers[0][1])), 10, (0, 191, 255), 2)

            (x, y) = KF.predict()
            cv2.rectangle(frame, (int(x - 15), int(y - 15)), (int(x + 15), int(y + 15)), (255, 0, 0), 2)

            (x1, y1) = KF.update(centers[0])

            # Create message with the correct syntax
            coords = Float64MultiArray(data=[x1, y1, x, y])
            pub.publish(coords)

            # Append data for plotting
            x_values.append(x)
            y_values.append(y)
            x1_values.append(x1)
            y1_values.append(y1)

            cv2.rectangle(frame, (int(x1 - 15), int(y1 - 15)), (int(x1 + 15), int(y1 + 15)), (0, 0, 255), 2)
            cv2.putText(frame, "Estimated Position", (int(x1 + 15), int(y1 + 10)), 0, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, "Predicted Position", (int(x + 15), int(y)), 0, 0.5, (255, 0, 0), 2)
            cv2.putText(frame, "Measured Position", (int(centers[0][0] + 15), int(centers[0][1] - 15)), 0, 0.5, (0, 191, 255), 2)

        cv2.imshow('image', frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            VideoCap.release()
            cv2.destroyAllWindows()
            break

        cv2.waitKey(HiSpeed - ControlSpeedVar + 1)

    # Plot the data after the loop
    plt.plot(np.ravel(x_values), np.ravel(y_values), label='Measured Position')
    plt.plot(np.ravel(x1_values), np.ravel(y1_values), label='Estimated Position')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
