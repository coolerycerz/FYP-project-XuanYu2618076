This is a Final Year Project (FYP) made by Xuan Yu, Glasgow university, student number: 2618076Y. All contents are completely made by Xuan Yu.

1. For YOLOv5 results obtained in the FYP, please refer to the folder named "YOlOv5 experiment", deatils including
Kaggle traffic sign dataset downloading are mentioned in "road-sign-detection-yolov5.ipynb".

2. If you would like to test the SD-CSNN light-weighted model that can be deployed on OpenMv, please prepare a singtown OpenMv with least version of H7,
and then refer to the folder "ei-FYPproject-1-openmv-v1", connect OpenMv to your PC, then drag the files named "labels.txt" and "trained.tflite" 
into the OpenMv, and run "ei_image_classification.py" on the OpenMv IDE on your PC. You can use the samples stored in "KAGGLEdatabase" to verify the results.

3. For SURF or SIFT key point detection method with proposed RGB filter, you can refer to folder "SD-CSNNwithRGB" and run "SURFandSIFTwithRGB.py" 
directly. In folder "SD-CSNNwithRGB/demo" you can find some examples of the processed images. If you want to explore SD-CSNN, set up the paddle environment first, you can refer to "https://github.com/PaddlePaddle/PaddleDetection?tab=readme-ov-file"
to set up. The SD-CSNN model can be loaded by the file located "SD-CSNNwithRGB/best_model/45test_precision0.9481851357.pl".

4. To show the original design and drawing of the figures, every figure shown in the FYP report are collected in the folder named 
"figures of FYP report".