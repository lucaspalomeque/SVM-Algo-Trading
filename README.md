# Application of SVM on Algo Trading

# Contents:

- [Introduction](#Introduction)
- [Background](#Background)
  * [Technical Analysis](#Technical-Analysis)
  * [Machine Learning](#Machine-Learning)
- [Strategy Scope](#Strategy-Scope)
  * [Indexs and Data Resources](#Indexs-and-Data-Resources)
  * [Analyzed Periods](#Analyzed-Periods)
- [Experiments Design](#Experiments-Desgin)
  * [Quantitative Algorithms](#Quantitative-Algorithms)
  * [Machine Learning Algorithms](#Machine-Learning-Algorithms)
- [Backtesting Process](#Backtesting-Process)
  * [Up Trend](#Up-Trend)
  * [Down Trend](#Down-Trend)
- [Statistics Analysis](#Statistics-Analysis)
  * [Up Trend](#Up-Trend)
  * [Down Trend](#Down-Trend)
- [Conclusion](#Conclusion)

# Introduction
The following research replicates the paper [Application of Support Vector Machine on Algorithmic Trading](https://search.proquest.com/docview/2136876869?pq-origsite=gscholar) published on Int'l Conf. Artificial Intelligence (ICAI'18). The paper provides a thoughtful analysis regarding the use of machine learning techniques applied to algorithmic trading using common indexes such as the S&P500 and the Chicago Board Options Exchange Market Volatility Index (VIX). A trading simulation is carried out in order to test the efficiency of the algorithms in up trending and down trending periods. Statistical and economic performance measures are compared in order to discuss the most effective technique. The inputs used in the analysis are well-known quantitative indicators such as the Relative Strength Index and the Moving Average Convergence-Divergence. The relevance of the results lies in the use of separated training models for each kind of trend.

# Background
## Technical Analysis
The technical indicators that are used are the following ones.  
The __Relative Strength Index (RSI)__ is an oscillator that compares the magnitude of a stock's recent gains to the magnitude of its recent losses and turns that information into a number that ranges from 0 to 100.  

The __Moving Average Convergence Divergence (MACD)__ is an oscillator that turns two moving averages, into a momentum oscillator by subtracting the longer moving average from the shorter moving average. It also relies in a third moving average called the MACD line in order to trigger the operation signals.  

The __momentum__ is an oscillator designed to identify the speed (or strength) of price movement. It simply deducts the current closing price minus the closing price n days ago, being n a user-defined parameter.  

## Machine Learning
__Random Forest (RF)__ is a supervised classification algorithm which is based in the generation of a random number of decision trees. As opposing to a single decision tree method, the information gain ratio is not taken in consideration, but the result of a voting algorithm using random test data is obtained instead.  

__Support Vector Machines (SVM)__ are classification or regression methods of supervised learning based in the construction a hyperplane as the decision surface. This hyperplane can be built by the use of kernel functions, which are functions that transform a vector space in another one of superior dimension.  

# Strategy Scope
## Indexs and Data Resources
The proposed system has been designed as a mid-term strategy, rather than an intraday system, due to the cost of the real time data needed for the intraday one. The strategy presented in this paper is recommended for the index S&P500 due to the relationship with the VIX index which is also studied. The data from both indexes is obtained from [Yahoo Finance](https://finance.yahoo.com/).  
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/spy_vix.png)

## Analyzed Periods
The presented strategy requires at least four periods for the testing phase, two training and two testing periods, although it is advisable to use more periods, the research has been conducted using only two due to time constraints. The periods selected are presented in the below table.  
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/periods.png)

# Experiments Desgin
## Quantitative Algorithms
The quantitative algorithms follow the same structure: each one of them returns an indicator with a value inside a specific range. The selling (buying) orders will get triggered when that value crosses above (or below) a threshold. The algorithm will finally output a vector of trading orders (+1) for purchases and (-1) for sales that will be later evaluated by a backtester module.  

The table below shows the trading rules for each one of the quantitative algorithms.  
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/indicator.png)

## Machine Learning Algorithms
Machine learning algorithms require a different approach. In first place, a training process is performed. This training is equal for every machine learning algorithm used in this paper, including SVM one. This training requires a set of inputs and an expected output for the training period. The 10 inputs to the training are the following ones:  

- RSI (14) at close.
- RSI (14) at previous day’s close.
- RSI (14) at previous two day’s close.
- MACD (26, 12, 9) at close.
- MACD (26, 12, 9) at previous day’s close.
- MACD (26, 12, 9) at previous two days’ close. 
- VIX data at close.
- VIX data at previous day’s close.
- VIX data at previous two day’s close.
- S&P500 change at close.  

An expected output is also needed in order to feed the training process. This output is obtained by designing a special algorithm which runs taking in consideration the whole training data vector (making it non-realistic for a test period). The trading rules used by the algorithm are as follows: “__Purchase orders are generated when the price from five days later has increased, whereas, sell orders are generated when it has decreased__”.

The table below shows the parameters configuration for the SVM algorithm.  
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/svm_para.png)

# Backtesting Process
To evaluate the proposed algorithms a backtester system is designed. Backtester is a tool that can output performance measures receiving as inputs the price data and the algorithm order vectors. Backtester must be configured with an initial capital input and commissions, which are chosen to be __$10000__ and __0.35%__ of the cost from each operation, as it is an average value for brokerage fees. Also the backtester requires a logic in order to perform the operations. In this research, the chosen logic is as follows:  

“In up trending markets, there can be only one long operation ongoing that must be exited in order to start a new one, in down trending markets there can be only one short operation on going that must be exited in order to start a new one. In either situation, the operation must be opened with the total capital available in the account at each moment”.  

This module also provides the performance of the Buy and Hold (BH) strategy as a benchmark for the evaluation. BH strategy uses the following rule: “A purchase is made during the first day of evaluation and sale is made at last day”.   
## Up Trend
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/up.png)
## Down Trend
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/down.png)

# Statistical Analysis
The measures used in this paper are the following ones.  

- The __return (R)__ is obtained subtracting the equity of each day from evaluation period. It is also presented as a percentage over the base capital, adding the sum of returns and subtracting them from the initial capital set.  

- The __Sharpe Ratio (SR)__ is a measure of risk of the investment which is calculated as the returns divided by their standard deviation.  

- The __Maximum Drawdown (MDD)__ is a measure of risk which displays the biggest performance fall of the return. It is calculated by subtracting the peak minus the valley after each fall, and getting the maximum from them.  

- The __volatility (Vol)__ is a measure of risk which displays the variation of the returns over time. It is calculated as the standard deviation of the return divided by their mean.  

R and SR are required to be as high as possible, with a negative cipher denoting loss, and a positive one denoting benefit. MDD and Vol are required to be as low as possible, and must be necessarily positive numbers. They are usually presented in percentage.  

## Up Trend
As shown in table, most algorithms output a positive income, except RSI one, which incurs in losses. So far, the volatility and MDD from all algorithms tend to be similar, which is caused due to the short size of the testing period However, this size was required due to the short duration of the trends that were required to analyze.  

The B&H strategy outperforms every algorithm in the up trending period, which is the expected result due to the strong dependence with price movement presented by this strategy, which is also a weakness in a down trend.  

The SVM algorithm has a pretty high performance in the up trending period, although not being able to beat the B&H.  
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/up_stat.png)

## Down Trend
In down trending periods, the first fact to notice is the greatly performance loss that all quantitative algorithms presents compared to the up trending periods. This fact supports the initial premise regarding the need of machine learning techniques in order to adapt to changing situations in the stock market.  

Furthermore, SVM and Random Forest shows a strong performance. The machine learning algorithm is able to make profitable decision, especially in down trending period.  
![](https://github.com/VictorXXXXX/SVM-Algo-Trading/blob/master/images/down_stat.png)  

# Conclusion
The SVM and Random Forest algorithm has been trained using different trainings for each period, and fed with common technical indicators such as RSI and MACD, and the VIX index.  

The results show that the SVM and Random Forest doesn’t return the best results in up trending periods, being outperformed by B&H systems. However, it shows a strong performance in down trending periods making it more suitable than quantitative techniques and other machine learning systems.  

As further work, it would be advisable to apply the Stop Loss filter as well as a more detailed parameter-optimization process.
