# 🖼️ Image Classification Application using CNN

A Deep Learning-based Image Classification Application developed using **TensorFlow**, **Keras**, and **Flask**. The model is trained on the **CIFAR-10** dataset using a Convolutional Neural Network (CNN) and deployed as a web application for real-time image classification.

---

## 📌 Project Overview

This project demonstrates the complete workflow of an image classification system, including data preprocessing, data augmentation, CNN model training, evaluation, model saving, and deployment using Flask.

Users can upload an image through the web interface, and the application predicts the corresponding class with a confidence score.

---

## 🚀 Features

* Image Classification using CNN
* Trained on the CIFAR-10 Dataset
* Data Preprocessing and Normalization
* Data Augmentation
* Model Evaluation
* Save Trained Model (.h5)
* Flask Web Application
* Upload and Predict New Images
* Confidence Score Display
* Simple and User-Friendly Interface

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib
* Flask
* Pillow
* Google Colab
* Visual Studio Code

---

## 📊 Dataset Information

**Dataset:** CIFAR-10

### Dataset Statistics

* Total Images: 60,000
* Training Images: 50,000
* Testing Images: 10,000
* Image Size: 32 × 32
* Number of Classes: 10

### Classes

* Airplane
* Automobile
* Bird
* Cat
* Deer
* Dog
* Frog
* Horse
* Ship
* Truck

---

## 🧠 Model Architecture

The CNN model consists of the following layers:

* Data Augmentation
* Conv2D (32 Filters)
* MaxPooling2D
* Conv2D (64 Filters)
* MaxPooling2D
* Conv2D (128 Filters)
* MaxPooling2D
* Flatten Layer
* Dense Layer (128 Units)
* Dropout (0.5)
* Output Layer (Softmax)

---

## ⚙️ Training Configuration

| Parameter        | Value                           |
| ---------------- | ------------------------------- |
| Optimizer        | Adam                            |
| Loss Function    | Sparse Categorical Crossentropy |
| Epochs           | 15                              |
| Batch Size       | 64                              |
| Validation Split | 20%                             |

---

## 📈 Model Performance

| Metric        | Value      |
| ------------- | ---------- |
| Test Accuracy | **74.51%** |
| Test Loss     | **0.7883** |

The trained CNN model achieved good performance on the CIFAR-10 dataset and successfully classified unseen images.
