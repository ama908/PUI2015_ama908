<<<<<<< HEAD
﻿# PUI2015_ama908 repo
=======
Include a README.md which describes what you are doing, and, if appropriate, how to run the notebook (input variables? global variables that need to be setup?).

In this assignment I'm generating  100 samples of different sizes N (N>10 & N<2000) from each of 6 different distributions (600 samples in total), all with the same population mean of 100.Distributions I'm using are Normal, Poisson, Binomial, Chi-Squared, Gamma, Geometric.                                       

I imported the following packages  

1.print_function from future
2.curve_fit, minimize from scipy.optimize 
3.norm from scipy.stats 
4.os
5.numpy and named it np
6.pylab and named it pl
7.matplotlib.mlab and named it mlab
import matplotlib.pyplot as plt


2. For each sample plot the sample mean against the sample size N (if you want you can do it with the sample standard deviation as well). 
Describe the behavior you see in the plots - do they look as you expected? why?

3. PLOT the distributions of all sample means (together for all distributions). 
Mandatory  - plot is as a histogram, 
Optional - plot it  in any other way you think is convincing

Optional: FIT a gaussian to the distribution of means             
 e.g. how to fit function to data in numpy:
http://glowingpython.blogspot.com/2012/07/distribution-fitting-with-scipy.html
http://stackoverflow.com/questions/7805552/fitting-a-histogram-with-python
Delivery: create a new Github directory called HW3 inside of your PUI2015_<your name> repo.
upload an ipython notebook, with the rendered plots. 
Include a README.md which describes what you are doing, and, if appropriate, how to run the notebook (input variables? global variables that need to be setup?).
75% of the grade will be based on the rendered version of the plot, 25% will be awarded if the TA can download and run the notebook (if you include any package that was not in the standard Anaconda distribution state that in your README.md, so that the TAs can install them).
Assignment 2 :  Hypothesis testing

Follow and understand the notebook https://github.com/fedhere/PUI2015_fbianco/blob/master/HW3/effectivenes%20of%20NYC%20Post-Prison%20Employment%20Programs.ipynb
and repeat the z-test and chisq test for other data included in the paper we are working with. 
by fill in missing cells in (your own copy of) the notebook

Delivery: upload the notebook on your   PUI2015_<your name>/HW3 github repo (see Assignment 1) 


## HW 3 Assignment 1
###Author Anita Ahmed - ama908@nyu.edu

#####Question 1. GENERATE  100 samples of different sizes N (N>10 & N<2000) from each of 6 different distributions (600 samples in total), all with the same population mean. 

##### 

2. For each sample plot the sample mean against the sample size N (if you want you can do it with the sample standard deviation as well).
3. ####Describe the behavior you see in the plots - do they look as you expected? why?
4. ##### In all the plots we can observe one thing in common that as the sample size is increased the sample mean approached the expeced mean value. This is completely in agreement with  the central limit theorem (CLT) which states that, given certain conditions, the arithmetic mean of a sufficiently large number of iterates of independent random variables, each with a well-defined expected value and well-defined variance, will be approximately normally distributed, regardless of the underlying distribution. [1]

######Reference: Wikipedia.https://en.wikipedia.org/wiki/Central_limit_theorem
>>>>>>> 3638db07006503a7e195151691b2fcc590fddb1d
