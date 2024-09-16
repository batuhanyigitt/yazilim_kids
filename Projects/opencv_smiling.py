import cv2 
def detect_faces():
    face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    cap = cv2.VideoCapture(0)
    if not cap.isOpened:
        print("Error! Coulnd't open the camera")
        return 
    window_name = 'Face Detection'
    while True:
        ret, frame = cap.read()
        if not ret: 
            print("ERROR: Couldnt' read the frame")
            break 
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in face: 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:w+w]
            roi_color = frame[y:y+h, x:x+w]
            
            smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
            for (mx, my, mw, mh) in smiles: 
                cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 255, 0), 2)
                cv2.putText(frame, 'Smiling', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)
            
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_faces()