import cv2
import os
import numpy as np

# Define paths
DATASET_PATH = "face_dataset"
MODEL_PATH = "face_recognizer.yml"

recognizer = cv2.face.LBPHFaceRecognizer_create()


if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

def collect_face_data(user_id):
    # Start video capture
    cap = cv2.VideoCapture(0)
    
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            cv2.imwrite(f"{DATASET_PATH}/User.{user_id}.{count}.jpg", face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        cv2.imshow('Face Data Collection', frame)
        
        if cv2.waitKey(1) == 27 or count >= 100: 
            break

    cap.release()
    cv2.destroyAllWindows()

def train_model():
    faces = []
    ids = []
    
    image_paths = [os.path.join(DATASET_PATH, f) for f in os.listdir(DATASET_PATH)]
    
    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        face_id = int(os.path.split(image_path)[-1].split(".")[1])
        faces.append(img)
        ids.append(face_id)
    
    recognizer.train(faces, np.array(ids))
    recognizer.save(MODEL_PATH)
    print("Model training completed and saved.")

def recognize_faces():
    recognizer.read(MODEL_PATH)
    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face_img)
            label_text = f"User {label}" if confidence < 50 else "Unknown"
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, label_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        cv2.imshow('Face Recognition', frame)
        
        if cv2.waitKey(1) == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("1. Collect Face Data")
    print("2. Train Model")
    print("3. Recognize Faces")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        user_id = input("Enter user ID: ")
        collect_face_data(user_id)
    elif choice == 2:
        train_model()
    elif choice == 3:
        recognize_faces()
