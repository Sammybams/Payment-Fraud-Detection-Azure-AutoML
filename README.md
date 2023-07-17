# Payment-Fraud-Detection-With-Azure-AutoML

## Description

Welcome to my project! This machine learning app leverages Azure Automated Machine Learning to detect payment fraud in online transactions. The web application has been developed using the Streamlit framework and the model was trained on this [dataset](https://www.kaggle.com/datasets/gopalmahadevan/fraud-detection-example).

## How to Install Dependencies and Run Project Locally

From your terminal:

Clone the repository and name as `paymentFraudDetection`

```
git clone https://github.com/Sammybams/Payment-Fraud-Detection-Azure-AutoML.git paymentFraudDetection
```

Create a virtual environment with the same name (`paymentFraudDetection`)

```
# Windows
python -m venv paymentFraudDetection

# macOS or Linux
python -m venv paymentFraudDetection
```

Activate the created virtual environment
```
# Windows
paymentFraudDetection\Scripts\activate

#macOS or Linux
source paymentFraudDetection/bin/activate
```

Then install the necessary dependencies.

``` 
cd paymentFraudDetection
pip install -r requirements.txt
```


Add the virtual environment to Jupyter Kernel
```
python -m ipykernel install --user --name=paymentFraudDetection
```

Train and Deploy your model using Azure Automated ML<br>
(Get the URL and Key to your endpoint)
![How to Build and Deploy your model using Azure AutoML](https://youtu.be/ymvDq0t68PQ?t=3165)

Run the Streamlit app locally

```
streamlit run Online_Payment_Fraud_Detection.py
```

## Demo

[Demo](https://github.com/Sammybams/Payment-Fraud-Detection-Azure-AutoML/assets/64220829/4e33f762-38d5-4a84-9bfb-5bd2bab24fb0)
