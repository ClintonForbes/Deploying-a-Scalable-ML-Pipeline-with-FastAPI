# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Model Name: Logistic Regression Classifier

Model Version: v1.0

Date: June 2024

Model Type: Supervised Learning, Binary Classification

Model Description: This model is a logistic regression classifier trained to predict whether an individual's income exceeds $50,000 based on various demographic features

## Intended Use

Primary Use Case: The model is designed to predict income levels based on demographic information for decision-making purposes.

Intended Users: Data scientists, analysts, and researchers who need to predict income levels from demographic data.

Out-of-Scope Use Cases: The model should not be used for any purposes outside of income prediction based on demographic data.

## Training Data

Source: Census Income dataset from UCI Machine Learning Repository

Preprocessing: Data preprocessing included one-hot encoding categorical features and label binarization.

Size: 32,561 samples

Description: The training data consists of demographic features such as age, education, occupation, and marital status.

## Evaluation Data

Source: Census Income dataset from UCI Machine Learning Repository

Size: 8,141 samples (20% of the original dataset)

Description: The evaluation data is a subset of the Census Income dataset used to evaluate the model's performance.

## Metrics

Metrics:

Precision: 0.7285
Recall: 0.2699
F1 Score: 0.3939

These metrics were chosen to evaluate the model's performance in predicting high-income individuals (income > $50,000) versus others.

## Ethical Considerations

Potential Bias: The model may exhibit bias based on historical data disparities in income distribution across demographic groups.

Fairness: Mitigating bias and ensuring fairness requires ongoing monitoring and evaluation of model predictions across different subgroups.

Privacy: The model does not explicitly store or process sensitive personal data beyond the scope of the provided dataset.

## Caveats and Recommendations

Caveats:

The model's performance is limited by the quality and representativeness of the training data.
It may not generalize well to populations or contexts not represented in the training data.

Recommendations:

Regularly update and retrain the model to incorporate new data and improve performance.
Conduct ongoing bias and fairness assessments to ensure equitable outcomes.