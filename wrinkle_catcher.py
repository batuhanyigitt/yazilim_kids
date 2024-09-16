import cv2

class WrinkleCatcher:
    def __init__(self):
        self.wrinkle_count = 0
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.wrinkle_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  # Using eye cascade as a placeholder

    def detect_wrinkles(self, gray, face):
        x, y, w, h = face
        face_region = gray[y:y+h, x:x+w]
        wrinkles = self.wrinkle_cascade.detectMultiScale(face_region, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (wx, wy, ww, wh) in wrinkles:
            self._report_wrinkle((x + wx, y + wy, ww, wh))

    def _report_wrinkle(self, rect):
        self.wrinkle_count += 1
        x, y, w, h = rect
        print(f"Wrinkle #{self.wrinkle_count} detected at: x={x}, y={y}, width={w}, height={h}")

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for face in faces:
            self.detect_wrinkles(gray, face)
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return frame

def main():
    catcher = WrinkleCatcher()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = catcher.process_frame(frame)
        cv2.imshow('Wrinkle Catcher', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Total wrinkles detected: {catcher.wrinkle_count}")

if __name__ == "__main__":
    main()
