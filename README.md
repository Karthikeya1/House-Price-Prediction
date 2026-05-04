This is a simple Regression project to predict the price of the house based on the data provided by the user.

**Models Used:**
  - Random Forest Regression
  - Gradient Boosting Regression
  - XG Bosting Regression

**Data Needed for prediction:**
  - Number of Bedrooms
  - Number of bath rooms
  - Living Area
  - Number of Floors
  - Water Font Present (1:Present, 0:Absent)
  - Number of Views
  - Grade of the house
  - Area of the house (excluding the basement)
  - Area of the basement
  - Renovation Year
  - Postal Code
  - Livin Area Renovation


**Parameter used for the models:**

  ***Random Forest Regressor***
    - n_estimators=100
    - min_samples_split=8
    - max_features=8
  
  ***Gradient Boosting Regressor***
    - n_estimators=500
    - min_samples_split=15
    - max_depth=5
    - loss="squared_error"
    - criterion="friedman_mse"
  
  ***XG Boosting Regressor***
    - n_estimators=200
    - max_depth=5
    - learning_rate=0.1
    - colsample_bytree=0.5


**Performance Metrics of the models**

  **Random Forest**
    ***Training Data***
      - Accuracy:0.93265
      - Mean Squared Error : 9670319866.76582
      - Mean Absolute Error : 52576.1559568629
      - Root Mean Squared Error : 98337.78453252757
    ***Testing Data***
      - Accuracy : 0.812277834137626
      - Mean Squared Error : 21469534624.568684
      - Mean Absolute Error : 88545.94220490157
      - Root Mean Squared Error : 146524.86009059584
  
  **Gradient Boosting**
      ***Training Data***
        - Accuracy : 0.970721511736131
        - Mean Squared Error : 4204300431.5277715
        - Mean Absolute Error : 46899.498298471604
        - Root Mean Squared Error : 64840.577044993755
      ***Testing Data***
        - Accuracy : 0.8663403836004384
        - Mean Squared Error : 15286472692.3126
        - Mean Absolute Error : 73406.14930105624
        - Root Mean Squared Error : 123638.47577640465

  **XG Boosting**
      ***Training Data***
        - Accuracy : 0.9444630146026611
        - Mean Squared Error : 7974942208.0
        - Mean Absolute Error : 61848.8359375
        - Root Mean Squared Error : 89302.53125
      ***Testing Data***
        - Accuracy : 0.8654305934906006
        - Mean Squared Error : 15390521344.0
        - Mean Absolute Error : 75957.65625
        - Root Mean Squared Error : 124058.5390625
