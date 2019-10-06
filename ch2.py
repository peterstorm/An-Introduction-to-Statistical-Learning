import streamlit as st
import numpy as np
import time


'''
# Chapter 2 - Exercises


## 2.1 Conceptual
For each parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning
method to be better or worse than an inflexible method.  
Justify your answer.

### Notes
To answer this we need to first understand the relationship between the _irreducible error_ (or noise), the _variance_ and the _bias_ of the model we are choosing - that is, the _**sources of errors**_.

Write a lot of latex here when supported in `streamlit`.

For regression we have a measure called the _test mean squared error_ (MSE), which can be decomposed into the sum of the _irreducible error_, the _squared bias_ and the _variance_. The irreduciblable error is associated with the inherent uncertainty or natural
variablity in our system, and thus cannot, as the name suggest, be reduced further. It is the lowest achieveable error. Therefor
we seek to minimize the variance and the bias to achieve a good test set performance.



a. The sample size is extremely large, and the
'''

with st.spinner("Wait for it..."):
        time.sleep(5)
st.info('This is a purely informational message')
st.success("Done")
st.balloons()

