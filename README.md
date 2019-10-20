# Application of SVM on Algo Trading

# Contents:

- [Introduction](#Introduction)
- [Background](#Background)
  * [Technical Analysis](##Technical-Analysis)
  * [Machine Learning](##Machine-Learning)
- [Strategy Scope](#Strategy-Scope)
- [Design of Experiments](#Design-of-Experiments)
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

__Support Vector Machines (SVM)__ are classification or regression methods of supervised learning based in the construction a hyperplane as the decision surface. This hyperplane can be built by the use of kernel functions, which are functions that transform a vector space in another one of superior dimension. Equation represents the problem that SVM must resolve, being  𝜔  the normal vector to the hyperplane, and C the cost of misclassification.  

# Strategy Scope
The proposed system has been designed as a mid-term strategy, rather than an intraday system, due to the cost of the real time data needed for the intraday one. The strategy presented in this paper is recommended for the index S&P500 due to the relationship with the VIX index which is also studied. The data from both indexes is obtained from [Yahoo Finance](https://finance.yahoo.com/).

# Design of Experiments

## Up Trend

## Down Trend


# Results

# Reference
