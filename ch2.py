import streamlit as st

'''
# Chapter 2 - Exercises


## 2.1 Conceptual
For each parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning
method to be better or worse than an inflexible method.  
Justify your answer.

### Notes
To answer this we need to first understand the relationship between the _irreducible error_ (or noise), the _variance_ and the _bias_ of the model we are choosing - that is, the _**sources of errors**_.

$$\mathrm{E}[(Y - \hat{f}(x))^2|, X=x_0] = \sigma_\epsilon^2 + \mathrm{Bias}^2[\hat{f}(x_0)] + \mathrm{Var}[ \hat{f}(x_0)],
$$

where $\sigma_\epsilon^2$ is the irreduciblable error,

$$\mathrm{Bias}[\hat{f}(x_0)] = \mathrm{E}[\hat{f}(x_0) - f(x_0)],$$

and

$$\mathrm{Var}[\hat{f}(x_0)] = \mathrm{E}[\hat{f}(x_0)^2] - \mathrm{E}[\hat{f}(x_0)]^2.$$

For regression we have a measure called the _test mean squared error_ (MSE), which can be decomposed into the sum of the _irreducible error_, the _squared bias_ and the _variance_. The irreduciblable error is associated with the inherent uncertainty or natural
variablity in our system, and thus cannot, as the name suggest, be reduced further. It is the lowest achieveable error. Therefor
we seek to minimize the variance and the bias to achieve a good test set performance.

When we try to fit a simple model to a, possibly very complex problem, we introduce an error known as _bias_. An example of this could be approximating a non-linear relationship, by a linear function of parameters and predocitors. Here we will always have a non-zero MSE, regardless of how well we fit the model parameters, how large the training set is, or how small the irreduciblable error is. This happens, because we try to fit - in simple terms - a model as a line, to a true model that is
definitely non-linear, and the more complex the true model, the more _bias_ our predicted linear model will ensue.

_Variance_ can be seen as the amount which our estimation function would change, if we gave our predicted model a different training set. The training set is used to obtain the model parameters, which means that if we change the training set, we expect
different estimates. If the change of estimates is small, after we have changed the training set by a little, we say we have a _low_ variance. On the other hand, if the little change to the training set, has wildly changed the estimated parameters,
the variance is said to be _high_.

In general, more flexible models have less bias, and higher variance. This is refered to as the **_bias-variance tradeoff_**,
as a low test MSE, requires both low bias and low variance.


### 2.1.a extremely large sample, few predictors
A flexible method is expected to be _better_.  
Since the sample size is large, and the number of predictors are small, a more flexible method would be
able to fit the data better, while still not fitting the noise, due to the large sample size. Because it is
more flexible, it would have the upside of less bias, without too much risk of overfitting.

### 2.1.b lots of predictors, small sample size
A flexible method is expected to be _worse_.
When the number of predictors is large and the sample size is small, a flexible method is expected to fit to the noise, meaning that given another random dataset of the same distribution, the fit would most likely be drastically different (higher variance). A less flexible method would be more biased, but at less risk of
overfitting - again, the bias-variance tradeoff.

### 2.1.c Highly non-linear relationship
Here, a flexible method is expected to be _better_.
As we explained earlier, if we have a highly non-linear relationship, a very inflexible method, would cause a
very large amount of bias (imagine trying to fit a straight line to a very complex function). By design, a linear model cannot capture the subtleties of non-linear model. If we had a huge sample size, we would still
expect the highly non-linear relationship to exist, and therefor that would still not change the fact that trying to fit a line to something non-linear would result in a large amount of bias.

### 2.1.d extremely high variance
A flexible method is expected to be _worse_.
When the variance is extremely high, a more flexible model will try to fit all the noise, thus overfitting the data, and if we then change the test data set, we might end up with a completely different estimation of
parameters, thus giving our model a high variance. In this case trying a less flexible model with more bias,
is probably the tradeoff we need, as the variance is much lower.
'''

