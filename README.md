<<<<<<< HEAD
﻿# PUI2015_ama908 repo
=======
ASSIGNEMENT 1

Include a README.md which describes what you are doing, and, if appropriate, how to run the notebook (input variables? global variables that need to be setup?).

I imported the following packages  

1.print_function from future
2.curve_fit, minimize from scipy.optimize 
3.norm from scipy.stats 
4.os
5.numpy and named it np
6.pylab and named it pl
7.matplotlib.mlab and named it mlab
import matplotlib.pyplot as plt

The notebook has given values so no input/global variable is needed to run the notebook. 

Then I'm generated  100 samples of different sizes N (N>10 & N<2000) from each of 6 different distributions (600 samples in total), all with the same population mean, which is dist_mean =100. Distributions I'm using are Normal, Poisson, Binomial, Chi-Squared, Gamma, Geometric.

For each distribution mean is calculated using differnt variables. 

In normal distribution, the distibution variable is equal to the given sample mean and standarddeviation which I set to 1  i.e. Distribution mean is 100, sd=1
In poisson distribution, the distibution variable is Labmda which is equal to the given value, i.e. Distribution lamda is 100
In binomal distribution, the distibution variable is sample size, n and the probability of success, p. the distibution mean is equal to n*p i.e.since distribution mean is predetermined I set the value p=.25 and set n =mean/p
In chi-squared distribution, the distibution variable is degree of freedom, df which is equal to sample mean , i.e. df is 100
In gamma distribution, the distibution variable is a shape parameter k and a scale parameter theta. the distibution mean is equal to k*theta i.e.since distribution mean is predetermined I set the value k=10 and set theta =mean/k
In gamma distribution, the distibution variable is the probability of success, p. the distibution mean is equal to 1/p i.e.since distribution mean is predetermined I set the value p=1/mean


For each sample I plotted the sample mean against the sample size N . 

Describe the behavior you see in the plots - do they look as you expected? why?
In all the plots we can observe one thing in common that as the sample size is increased the sample mean approached the expeced mean value. This is completely in agreement with the central limit theorem (CLT) which states that, given certain conditions, the arithmetic mean of a sufficiently large number of iterates of independent random variables, each with a well-defined expected value and well-defined variance, will be approximately normally distributed, regardless of the underlying distribution. [1]¶
Reference: Wikipedia.https://en.wikipedia.org/wiki/Central_limit_theorem

I have PLOTTED the mandatory histogram plot of the distributions of all sample means (together for all distributions). 
And also an optional that is showing each distibution mean frequencied separately but on the same plot. 
In both plots we an observe larger sample sizes have sample mean close to 100. 

Optional: FIT a gaussian to the distribution of means             
 I have also fitted a gaussian to the histigram of all means 


ASSIGNMENT 2

Assigment 2 is submitted in a separate ipython notebook. 
