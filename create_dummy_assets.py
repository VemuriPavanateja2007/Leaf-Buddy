import os
import json
import numpy as np
import tensorflow as tf
from PIL import Image

def build_and_save_dummy_model():
    model_path = "plant_model.keras"
    if not os.path.exists(model_path):
        print("Creating lightweight dummy plant_model.keras for testing...")
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(shape=(128, 128, 3)),
            tf.keras.layers.Rescaling(1./255),
            tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(38, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy')
        model.save(model_path)
        print("Successfully created plant_model.keras")
    else:
        print("plant_model.keras already exists.")

def create_sample_leaf_image():
    sample_path = "sample_leaf.jpg"
    if not os.path.exists(sample_path):
        # Create a simple green image with leaf pattern
        img_arr = np.ones((256, 256, 3), dtype=np.uint8) * 240
        # Green center circle
        y, x = np.ogrid[:256, :256]
        mask = (x - 128)**2 + (y - 128)**2 <= 80**2
        img_arr[mask] = [46, 125, 50] # Forest green
        img = Image.fromarray(img_arr)
        img.save(sample_path)
        print("Created sample_leaf.jpg for testing.")

if __name__ == "__main__":
    build_and_save_dummy_model()
    create_sample_leaf_image()
