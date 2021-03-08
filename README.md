# Interpretability_of_LinearRegression
it provides a basic information about the interpretability of Linear Regression Algorithm by using python.

**Interpretability of ML models is a new trend to explain these models to human to make them understand why a certain prediction is occured.. This is a part of XAI**

In this project, we will learn the following: 
* Linear Regeession Theory.
* How to implement Linear regression in Python.
* Linear Regression Interpretability.

**Linear Regression Theory:**
-----------------------------------------------------------------------------------------------------------------
One of the supervised Machine Learning Algorithms is Linear Regression which is used for Regression and Classification. Linear Regression Model expresses the linear relation 
between one or more variables. If Te dataset is in 2-Dimensional Space the result would be a stragiht line. If the data set in 3-D space, the result would be a plane. 

Rhe equation of simple Linear Regression Model is as following  **y = mx + b** 
where the y is the dependent varaible, x is the independent varaible, m is the solope and b is the intercept.

So bacially,  Linear Regression Model attempts to give the most optimal value for the intercept and slop in 2-d spac and returns the line with the leaset error.

-----------------------------------------------------------------------------------------------------------------
**How to implement Linear regression in Python.**

Our problem is take from https://stackabuse.com/linear-regression-in-python-with-scikit-learn/ that simply represents the simplest linear regression model 
where we deal with number of hour that students studies and their perecenteges of marks that a certain student score in certain exam. 
The goal of this project is by giving a number of hours, how high score can the student acheive? 

The code of this project could be found in the shared link and in this github. 


-----------------------------------------------------------------------------------------------------------------

# Linear Regression Interpretability

Before we go into some explaiantion of our predicted values in this project , let talk abouts some features about what makes the interpretation of Linear Regression quiet simple: 

1. Linearity
The linear regression model forces the prediction to be a linear combination of features. Linearity leads to interpretable models. 
Linear effects are easy to quantify and describe. They are additive, so it is easy to separate the effects. 

2. Normality
It is assumed that the target outcome given the features follows a normal distribution. If this assumption is violated, 
the estimated confidence intervals of the feature weights are invalid.

3. Independence
It is assumed that each instance is independent of any other instance.

4.Fixed features
The input features are considered "fixed". Fixed means that they are treated as "given constants" and not as statistical variables. 
This implies that they are free of measurement errors. 
----------------------------------------------------------------------------------------------------------------------

Now, we will try to interpret our model by using simple code without moving to some XAI techniques or other complex methods. 

Let's show some of the output that we got from the code: 

1. Output of the Model: 

      Actual      	Predicted
	20	        16.884145
	27	        33.732261
	69	        75.357018
	30	        26.794801
 	62	        60.491033
  
2. if we apply print(regressor.intercept_)
    - The resulting value you see should be approximately 2.01816004143.

3. if we apply print(regressor.coef_)
    - The result should be approximately 9.91065648.
   
Now , putting everything togather and to able to answer one question: 
**How these results come out and to interpret them?**

Simply, we can use the following code 

      Model = sm.Ols(y_train,X_train).fit()
      print(Model.summary) 
      
 we can notice the coeffiencts of our only one variable "hours" is approximately 9.91065648 which tells us This means that for every one unit of change in hours studied, 
 the change in the score is about 9.91%. Or in simpler words, if a student studies one hour more than they previously studied for an exam,
 they can expect to achieve an increase of 9.91% in the score achieved by the student previously.
 
 So, in Linear Regression Models, the coeffiencts can provide could meaning why and how such predicted value is came out. This is still a very simple way to interpret and alot of 
 techniques and methods could be used to interpret our model.
 
 we can also depends on other values to interpret our model. we could also do the following: 
  - We can plot the coefficient’s values and standard errors. Start by computing an error term equal to the difference between the parameter’s value and the lower confidence 
 interval bound for this parameter, and build a single table with the coefficient, the error term and the name of the variable.
 
 By this work , we could done a simple step to explain why a certain model results in this prediction values.. moreover could be improved to explain more about our data and model. 
 
      
   
    
    
    
    
    
    
    
    
    
    
    
    
