# Student Score Prediction Attempt
---

## Introduction
Personal attempt on the StudentScorePrediction question from AIAP

## Prerequsities
Refer to requirements.txt for required Python libraries <br>

## Overview
### Task 1
Use Jupyter notebook (eda.ipynb) to do Exploratory Data Analysis (EDA) on the provided SQL database (score.db) <br> <br>
Requirements:
- Use SQLite or similar to open and read the SQL database
- Clean up and process data to produce some form of correlation between students' score and the other data sets
- For details on the feature engineering done to the data from the SQL database, please refer to the table below
    - Perform data set standardization and one-hot encoding
- Plot heatmap to visualize dimension reduction and drop features with correlation values that are too low
- Test machine learning models with remaining data
- Perform machine learning with 95% variance features (PCA)

#### Summarized Details
1. Use SQLite to connect to SQL database, score.db, and check the structure, column data type and data in 'score' table
2. Get the row_count of 'score' table to assess size of data set
3. Extract 'score' table into a DataFrame using SQLite for further processing
4. Clean up DataFrame of empty cells by dropping the rows
5. Use sleep_time and wake_time to calculate the number of hours of sleep, then drop sleep_time and wake_time columns
6. Check the summary statistics of the DataFrame to get a sense of the benchmark value of weak students ('final_test' value <  25% metric)
7. Perform data set standardization on columns with numeric data
8. Perform one-hot encoding on columns with non-numeric data
9. Visualize data set dimension reduction using feature correlation heatmap and drop features that have correlation value < 0.1
10. Test Linear Regression, Random Forest Regression and XG Boost machine learning models with remaining data set
11. Perform Random Forest Regression machine learning with 95% variance data (PCA)
12. Perform cross-validation with PCA feature


#### Feature Engineering Table
| No. | Column Name | Value |
| :-: | :---------: | :---: |
|  1  | direct_admission  |         No        |
|     |                   |        Yes        |
|  2  |       CCA         |       Sports      |
|     |                   |        Arts       | 
|     |                   |        Clubs      |
|     |                   |        None       |
|  3  |  learning_style   |       Visual      |
|     |                   |      Auditory     |
|  4  |      tuition      |        No/N       |
|     |                   |       Yes/Y       |
|  5  | mode_of_transport |        Walk       |
|     |                   | Public Transport  |
|     |                   | Private Transport |
|  6  |    bag_color      |       Yellow      |
|     |                   |        Red        |
|     |                   |       Green       |
|     |                   |       White       |
|     |                   |       Black       |
|     |                   |       Blue        |
|     |                   |                   |

<br>

----

### Task 2
Use Python scripts (*.py) to create an End-to-End Machine Learning pipeline <br> <br>
Requirements:
- Appropriate data processing and feature engineering
- Appropriate use and optimization of at least 3 algorithms/models
- Appropriate explanation for choice of algorithms/models
- Appropriate use of evaluation metrics
- Appropriate explanation of evaluation metrics

User config - Located in cfg/config.yaml

#### Folder Structure
```md
./src
├── cfg
|   └── config.yaml
├── EDA
|   └── eda_step.py
├── model_eval
|   └── model_eval.py
├── model_select
|   └── model_select.py
├── setup
|   └── setup.py
├── main.py
└── requirements.txt
```

#### Pipeline Execution and Parameter Modification Flow
- TODO: Not done

#### Pipeline Flow
- TODO: Not done

#### Model Choice Evaluation
- Linear Regression
    - Parameters: None
    - Evaluation:
        - This model is also a quick and interpretable model that can be used as a benchmark for comparison
- Random Forest Regression
    - Parameters:
        - Number of estimators - Number of decision trees in the random forest
        - Max depth - Number of splits that each decision tree is allowed to make
    - Evaluation:
        - Since the current data set has many features and having insight on the important features, random forest regression is optimal
        - This model has better model accuracy, at the expense of intepretabiity and computational resources available
        - Number of estimators parameter determines the number of decision trees
            - Increasing the parameter generally improves performance up to a certain point before more trees reduce variance by averaging the predictions
            - Ideal method is to start at a value (example: 100) and increase the parameter value until performance stabilizes
        - Max depth parameter is tweaked to limit the depth of each decision tree, which controls the complexity of trees
            - A deeper tree captures more complex patterns but there is a risk of overfitting the training data
            - Ideal method is to start at a value (example: 3) and increase until the performance peaks
- Support Vector Regression (SVR)
    - Parameters:
        - C - Regularization parameter (Regularization strength is inversely proportional to C)
        - Kernel - Kernel type to be used in algorithm
    - Evaluation:
        - As the datasets has a non-linear relationship between the features and 'final_test' and also requires precise predictions, support vector regression is optimal
        - Since the priority in this case is high accuracy but the relationships in the data are not well-understood, this model also stands out as an excellent choice
        - C parameter controls trade-off between achieving low error on training data and minimizing model complexity to improve generalization
            - Higher values allow model to focus more on minimizing training error, while lower values emphasize simpler models that generalize better
            - Ideal method is to start at a value (exmple: 1) and tune across a wide range (example: 0.1 to 200)
        - Kernel parameter defines how the input space is transformed to capture relationships between features and target variable, 'final_test'
            - Different kernels are suited for different types of data and relationships
            - Ideal method is to start with radial basis function (RBF) kernel and switch to other kernels if other relationships are suspected

<br>

## Reference
https://github.com/aisingapore/AIAP-Technical-Assessment-Past-Years-Series/tree/main/StudentScorePrediction