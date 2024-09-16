import cv2
import numpy as np
def detect_colors(frame, colors):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    detected_colors = []
    for color, values in colors.items():
        lower_bound = values['lower']
        upper_bound = values['upper']
        color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
        if cv2.countNonZero(color_mask) > 0:  # Check if any pixels of this color are detected
            detected_colors.append(color)
    return detected_colors
def main():
    cap = cv2.VideoCapture('Projects/couple.mp4')
    if not cap.isOpened():
        print("Error: Couldn't open video file")
        return
    window_name = 'Color Detection'
    colors_to_detect = {
        'green': {'lower': np.array([40, 40, 40]), 'upper': np.array([70, 255, 255])},  # Standard green
        'green_tones': {'lower': np.array([25, 40, 40]), 'upper': np.array([70, 255, 255])},  # Green tones
        'blue': {'lower': np.array([100, 50, 50]), 'upper': np.array([130, 255, 255])},
        'red': {'lower': np.array([0, 50, 50]), 'upper': np.array([10, 255, 255])}
    }
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detected_colors = detect_colors(frame, colors_to_detect)
        if detected_colors:
            color_message = ", ".join(detected_colors)
            cv2.putText(frame, f"Detected color(s): {color_message}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
