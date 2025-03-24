import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

def load_train(path, img_size=(128, 128)):
    # Загрузка тренировочных данных
    images = []
    labels = []
    
    for label in os.listdir(path):
        label_path = os.path.join(path, label)
        if os.path.isdir(label_path):
            for img_file in os.listdir(label_path):
                img_path = os.path.join(label_path, img_file)
                img = tf.keras.preprocessing.image.load_img(img_path, target_size=img_size)
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                images.append(img_array)
                labels.append(int(label))  # Предполагаем, что метки - это имена папок, преобразованные в числа

    images = np.array(images) / 255.0  # Нормализация
    labels = np.array(labels)
    return images, labels

def load_test(path, img_size=(128, 128)):
    # Загрузка тестовых данных
    images = []
    
    for img_file in os.listdir(path):
        img_path = os.path.join(path, img_file)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=img_size)
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        images.append(img_array)

    images = np.array(images) / 255.0  # Нормализация
    return images

def create_model(input_shape):
    # Создание модели свёрточной нейронной сети
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))  # Предполагаем, что задача регрессии (MAE)
    
    model.compile(optimizer=Adam(), loss='mean_absolute_error', metrics=['mae'])
    return model

def train_model(model, train_data, test_data, batch_size, epochs, steps_per_epoch, validation_steps):
    # Обучение модели
    train_datagen = ImageDataGenerator()
    test_datagen = ImageDataGenerator()
    
    train_generator = train_datagen.flow(train_data[0], train_data[1], batch_size=batch_size)
    test_generator = test_datagen.flow(test_data[0], test_data[1], batch_size=batch_size)
    
    model.fit(train_generator,
              steps_per_epoch=steps_per_epoch,
              epochs=epochs,
              validation_data=test_generator,
              validation_steps=validation_steps)

# Пример использования функций
train_path = 'path/to/train/data'
test_path = 'path/to/test/data'

# Загрузка данных
train_data = load_train(train_path)
test_data = load_test(test_path)

# Создание модели
input_shape = (128, 128, 3)
model = create_model(input_shape)

# Обучение модели
train_model(model, train_data, test_data, batch_size=32, epochs=25, steps_per_epoch=100, validation_steps=20)

# Оценка модели
mae = model.evaluate(test_data[0], test_data[1])
print(f'Test MAE: {mae}')

