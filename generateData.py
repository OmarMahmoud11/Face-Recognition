import cv2
import numpy as np
import os

def image_to_vector(image_path, size=(112, 92)):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, size)
    img_vector = img_resized.flatten()
    return img_vector

def images_in_folders_to_vectors(folder_paths):
    image_vectors = []
    i=0
    for folder_path in folder_paths:
        i+=1
        for filename in os.listdir(folder_path):
            if filename.endswith(".pgm"):  # Filter images by extension
                image_path = os.path.join(folder_path, filename)
                vector = image_to_vector(image_path)
                vec = np.append(vector,i)
                image_vectors.append(vec)
    return image_vectors

########################
folder_paths = []
for i in range(40):
    folder_paths.append("Subjects/s"+''+str(i+1))
vectors = images_in_folders_to_vectors(folder_paths)
print("Number of images processed:", len(vectors))
print("Shape of each vector:", vectors[0].shape)
print("Shape of each vector:", vectors[1])