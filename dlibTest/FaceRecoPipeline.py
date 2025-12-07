import dlib
import cv2
import numpy as np
import sys
import platform
import os
import glob


imageInput = "./im/recoIm.jpg"


predictor_path = "./weights/shape_predictor_68_face_landmarks.dat"
recognizer_path = "./weights/dlib_face_recognition_resnet_model_v1.dat"

##This is done 1 time because of the size limitations f github

def join_files(input_base_path):
    search_pattern = f"{input_base_path}.part*"
    chunk_files = sorted(glob.glob(search_pattern), key=lambda x: int(x.rsplit('.', 1)[-1].replace('part', '')))
    
    if not chunk_files:
        print(f"No chunk files found matching pattern: {search_pattern}")
        return

    print(f"Found {len(chunk_files)} parts. Rebuilding to {output_file_path}...")

    with open(input_base_path, 'wb') as outfile:
        for part_file in chunk_files:
            print(f"Appending {part_file}...")
            with open(part_file, 'rb') as infile:
                outfile.write(infile.read())
            os.remove(part_file)
    print("Rebuilding complete.")

if not os.path.exists(predictor_path):
    join_files(predictor_path, predictor_path)

print("\nPython version (platform):")
print(platform.python_version())
print(f"dlib version: {dlib.__version__}")
print(f"dlib.DLIB_USE_CUDA: {dlib.DLIB_USE_CUDA}")
print(f"dlib.cuda.get_num_devices(): {dlib.cuda.get_num_devices()}")


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
recognizer = dlib.face_recognition_model_v1(recognizer_path)


image_path = imageInput # Replace with your image file
image = cv2.imread(image_path)
black_image = np.zeros_like(image)

if image is None:
    print(f"Error: Could not load image {image_path}")
    exit()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print("Detecting faces...")
faces = detector(rgb_image,1)
print(f"Found {len(faces)} faces.")

embeddings = []
for face in faces:
    landmarks = predictor(rgb_image, face)
    landmarks_np = np.array([[p.x, p.y] for p in landmarks.parts()])
    face_descriptor = recognizer .compute_face_descriptor(rgb_image, landmarks)

    for (x, y) in landmarks_np:
        cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
        cv2.circle(black_image, (x, y), 2, (0, 255, 0), -1)

    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 0, 255), 2)
    
    face_descriptor_numpy = np.array(face_descriptor)
    embeddings.append(face_descriptor_numpy)

print(f"Generated {len(embeddings)} of shape: {face_descriptor_numpy.shape}")


# Example of comparing two embeddings
if len(embeddings) >= 2:
    distance = np.linalg.norm(embeddings[0] - embeddings[1])

    print(f"Distance between first two faces: {distance}")

    threshold = 0.6
    if distance < threshold:
        print("Faces match (likely the same person).")
    else:
        print("Faces do not match (likely different people).")





cv2.imwrite('./results/result.jpg',image)
cv2.imwrite('./results/black_result.jpg',black_image)

cv2.imshow("Dlib Model Test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

##If you want th built-in help for the dlib used functions

#help(dlib.get_frontal_face_detector)
#help(dlib.shape_predictor)
