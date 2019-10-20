# Application of SVM on Algo Trading

# Contents:

- [Introduction](#Introduction)
- [Background](#Background)
  * [Technical Analysis](##Technical-Analysis)
  * [Machine Learning](##Machine-Learning)
- [Strategy Scope](#Strategy-Scope)
  * [Indexs and Data Resources](##Indexs-and-Data-Resources)
  * [Analyzed Periods](##Analyzed-Periods)
- [Experiments Design](#Experiments-Desgin)
  * [Quantitative Algorithms](##Quantitative-Algorithms)
  * [Machine Learning Algorithms](##Machine-Learning-Algorithms)
_ [Backtesting Process](#Backtesting-Process)
  * [Up Trend](##Up-Trend)
  * [Down Trend](##Down-Trend)
- [Results](#Results)
- [Reference](##Reference)

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
## Up Trend

## Down Trend


# Results

# Reference
