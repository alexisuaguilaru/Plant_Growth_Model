# Model for Predicting Growth Milestone of Plants

## Abstract
This project aims to create a supervised learning model for plant growth milestone prediction based on environmental and management factors involved in plant care.

## Author, Affiliation and Contact
Alexis Aguilar [Student of Bachelor's Degree in "Tecnologías para la Información en Ciencias" at Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com

Project developed for the subject "Sistemas Basados en Conocimientos" (Machine Learning: Supervised Learning) for the class taught in semester 2025-2.

## License
Project under [MIT License](LICENSE)

## Introduction
Understanding and being able to predict when plant growth is significant becomes an important task for industrial agriculture, since this leads to an optimization of resources (time, materials and human resources) that results in higher profits and lower losses for the farmer. Therefore, based on the data set [[1]](#references) it will be tested whether it is possible to determine the growth of a plant based on a reduced set of observations and simplified parameters, as well as possible interactions that can be detected based on the different comments and observations made.

## General Aim
The purpose of this work is to present a classification model capable of determining whether a plant will have significant growth based on environmental and management factors.

## About the Dataset
The data set was taken [[1]](#references). It contains the measurements such as the amount of sunlight hours, temperature and humidity, as well as those concerning soil type, irrigation frequency, type of fertilizer and whether there was a significant growth.

## Exploratory Data Analysis (EDA)
The process related to data exploration is found in [Exploratory Data Analysis](./ExploratoryDataAnalysis/ExploratoryDataAnalysis.ipynb), where the procedures carried out to acquire different knowledge and insights about the dataset being worked with are presented. Where it is highlighted how the presence of fertilizers (organic or not) favors the significant growth of plants and that the other factors have complex interactions between them to generate their influence on plant growth. In addition, it was determined that the classes are not linearly separable, that is, that there is an overlap in the values taken by the factors, so that a plant may or may not have significant growth even with the same environmental or care factors.

## Machine Learning Models
The process related to the definition, training, evaluation and selection of Machine Learning models can be found in [Machine Learning Models](./Model/MachineLearningModel.ipynb), where the fundamental part about the metrics for determining when a model is better during the training stage as well as the metrics used for the evaluation and final selection of the model with the best expected behavior is broken down. It is highlighted that the models with the best behaviors in the test set have in common that they are linear models, or that they have linear decision edges, indicating that the generated features favored, in general, for the training of the models.
<div style="text-align: center;">
  <img src="./Resources/ResultsModelsTest.png" width=450>
  <img src="./Resources/ResultsModelsTrain.png" width=450>
</div>

## References
* [1] Plant Growth Data Classification. Kaggle, [gortorozyannnn](https://www.kaggle.com/gorororororo23). https://www.kaggle.com/datasets/gorororororo23/plant-growth-data-classification