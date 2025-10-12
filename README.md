# Assignment: Customer feedback analysis software demo

> **Author : Yang Yi**
> 
> **Matricular Number : N2504320D**
***
## Description
This project is a demo of customer feedback analysis software. Including text sentiment analysis
and image anomaly detection.<br>

**Model Used :** 
- Self-trained text sentiment model, dataset from kaggle (See appendix below)
- Transformer pipeline for text sentiment analysis
- The pre-trained WideResNet50 model of PyTorch [Download .pth file](https://download.pytorch.org/models/wide_resnet50_2-95faca4d.pth)

## Result Presenting
<p align="center">
  <img src="readme_pic/result.png" alt="Chart Example">
</p>

## Environment Settings
**Python Interpreter :** ```Python 3.13.2```  
**Install Libraries :**
```powershell
# Windows PowerShell
pip install uv
uv sync
pip install anomalib[vlm_clip]
```
**Demo Entrance :** ```main.py```
**Model Training Entrance :** ```model_trainer/main_model_train.py```

## How to Use
1. Set up environment
2. Download model file from [here](https://drive.google.com/drive/folders/1HtzvoRDriXeo3ltXju0zfeuOQiz39XEF?usp=drive_link)
3. Insert model file, where the file path should be put into folder ```Customer-feedback-analysis-software-demo/model```
4. Run ```main.py``` to start the demo.

## Trained Source Used
1. Mark Kaghazgarian : Sentiment Labelled Sentences Data Set, Kaggle. [Redirect](https://www.kaggle.com/datasets/marklvl/sentiment-labelled-sentences-data-set?resource=download)
2. Rahul Kumar : Sentiment Labelled Sentences Data Set, Kaggle. [Redirect](https://www.kaggle.com/datasets/rahulin05/sentiment-labelled-sentences-data-set/data)
3. Wali M. Ahmad : Amazon Sentiment Spectrum: Reviews Dataset. [Redirect](https://www.kaggle.com/datasets/walimuhammadahmad/amazone-reviews/data)

***

## Project Structure

### 1. Root Directory
- [main.py](main.py) - Main entry point to start the demo application
- [pyproject.toml](pyproject.toml) - Project dependencies and configuration
- [README.md](README.md) - Project documentation

### 2. GUI Module ([gui/](gui/))
Contains all user interface related files:

- [console.py](gui/console.py) - Handles text output to the GUI console widget
- [ui_function.py](gui/ui_function.py) - Button and Widget slot functions
- [ui_main.py](gui/ui_main.py) GUI code,  using PySide6 (PyQt)
- [ui_mainwindow.py](gui/ui_mainwindow.py) - Main window class that connects UI elements with their functions

### 3. Model Directory ([model/](model/))
**Model Files should be pasted in this folder!**</br>
Contains pre-trained models and tokenizer configurations:

### 4. Model Trainer Module ([model_trainer/](model_trainer/))
Contains scripts for training models and performing inference:

- [data_cleaning.py](model_trainer/data_cleaning.py) - Text data preprocessing and cleaning utilities
- [main_model_train.py](model_trainer/main_model_train.py) - Main entry point for training the text sentiment analysis model
- [pic_model_trainer.py](model_trainer/pic_model_trainer.py) - Implementation of ResNet50-based image anomaly detector
- [text_model_trainer.py](model_trainer/text_model_trainer.py) - Implementation of BERT-based text sentiment analyzer