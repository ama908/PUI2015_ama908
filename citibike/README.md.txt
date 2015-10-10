Please check HW_Assignement_3_Final Version (1).ipynb and disregard others

For this Assignment, I worked in a group of 3 people. My partners were Erwan LeCun, Miyabi Ishihara. 

My Contributions:
I came up with the NULL Hypothesis. Erwan coded from the z-test and getting zip dataset directly from website , Miyabi and I coded the Chi-Suqare Test on Python Notebook, I wrote up all the markdowns for our notebook.  

IDEA:
Our group did both mean problem and a proportion problem using January 2015 citibike data. 
Using The test flowchart shown by Dr.Federica we came up with testing method:

Test #1
We tested if in any given month the averge tripduration per customer and averge tripduration per subscribers are equal. 
Since is a test to measure the numerical outcome(i.e mean) from two different groups of variables that are indendent of each other we proceeded with a Z-Test. 

Sample used : January 2015, Citibike data

Null Hypothesis: The averge tripduration per customer (u1) and averge tripduration persubscribers(u2), in are equal at a significnace level p = 0.025

Alternetive Hypothesis: The averge tripduration per customer (u1) and averge tripduration persubscribers(u2)

Ho: u1-u2 = 0
Ha: u1-u2 ≠ 0
α =0.025

First we thought about reproducibility so we came up with a code to get the zip file from the internet autmatically, that way the code does everything by itself and the TA doesn't need to download the file first in order to run the code.  

Then we created two samples from the data by sorting trip duration by user type. We modified the z-statistic formual from class notes and calculated the z-value for our sample. Which was 33.7877558335. 
For two tailed z-test and for a significance level of α=0.025, and the critical z-value is 1.96. Since our z-staistic was larger than the critical value we rejected the NULL Hypothesis that the mean ride time for subscriber and customer is equal. 

The Z score was unusually large as the sample sizes of subscriber sample size is significantly larger than the customer sample size.So we wanted to conduct a different test. 

Test #2 

CHI-SQ Test

PROPOSAL : We wanted to test if Subscriber takes longer rides than Customers. For that we divided the trip duration as long ride and short ride. Long ride is anything more than or equal to 10 minutes. Short ride is less than 10 minutes. We  conduted the test at a significnace level p = 0.05


Null Hypothesis: The probability of Subscriber taking long rides (P0) is higher than or equal to the probability of Customer taking long rides (P1).Testing at a significnace level p = 0.05

Ho: P0-P1 ≥ 0

Alternetive Hypothesis: The proportion of Subscriber taking long rides (P0) is lower than the proportion of Customer taking long rides (P1).

Ha: P0-P1 < 0

α =0.05

We created samples for Subscribers taking short and long trips and customers taking short and long trips. 

We used the Chi- Square test formula from class notes and we got Chi-square Value that was greater than 3.84 . So we rejected the null hypothesis. Therefore, the probability of Subscriber taking long rides is lower than the probability of Customer taking long rides. This probably is due to the fact that Subcribers are locals who tend to use bikes for daily commute where as Customers might be tourists who are riding the bikes longer for sightseeing.

