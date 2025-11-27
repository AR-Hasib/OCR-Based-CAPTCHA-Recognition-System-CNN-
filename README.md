# CAPTCHA Recognition

## Overview
This project implements a complete CAPTCHA recognition pipeline as part of a university experiment. The process includes dataset generation, preprocessing, segmentation, labeling, model training, evaluation, and prediction using a Convolutional Neural Network (CNN).

## Steps and Plan

### 1. Fetching CAPTCHA Images
- Automatically generate a large collection of CAPTCHA images.
- Each image filename contains the correct 4-character CAPTCHA text.
- This dataset will be used for training and testing.

### 2. Showing Sample Data
- Load a sample CAPTCHA image using OpenCV.
- Display the image to visually confirm the data.
- Print the image’s dimensions (height, width, channels).

### 3. Processing (Grayscale Conversion → Binarization → Noise Removal)
- Convert the image to grayscale to simplify color information.
- Apply binary thresholding to get a clear black-white image.
- Remove noise using 4- or 8-neighborhood rules to eliminate isolated pixels.

### 4. Segmentation
- Use vertical projection to detect character boundaries.
- Split the CAPTCHA image into four separate character images.
- Each image now contains a single clean character.

### 5. Batch Processing and Labeling
- Run preprocessing and segmentation on every CAPTCHA in the dataset.
- Use the CAPTCHA filename to determine the correct labels.
- Place each segmented character image into its label folder (0–9, A–Z, a–z = 62 classes).

### 6. Reading the Dataset
- Load all labeled character images from folders.
- Normalize pixel values and encode labels.
- Prepare the dataset for deep learning (train/test split).

### 7. Train CNN Model
- Build a Convolutional Neural Network for character classification.
- Train the model using the labeled segmented characters.
- Save the trained model (.h5 file) for later prediction.

### 8. Model Evaluation
- Load the trained model and test it on validation data.
- Print accuracy and inspect sample predictions.
- Ensure the model can correctly classify CAPTCHA characters.

### 9. Use the Model for CAPTCHA Recognition
- Load a new CAPTCHA image.
- Preprocess, binarize, denoise, and segment into 4 characters.
- Pass each character into the trained CNN.
- Combine the four predictions to form the final CAPTCHA text.

### 10. Summary and Conclusion
- The task builds a complete CAPTCHA recognition pipeline: dataset creation → preprocessing → segmentation → labeling → CNN model → evaluation → prediction.

---


