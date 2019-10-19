#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd

def RSI(df, column="Close", period=14):
    # Wilder's RSI
    delta = df[column].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    rUp = up.ewm(com=period - 1, adjust=False).mean()
    rDown = down.ewm(com=period - 1, adjust=False).mean().abs()
    rsi = 100 - 100 / (1 + rUp / rDown)
    df = df.join(rsi.to_frame('RSI'))
    df['RSI_p1'] = df['RSI'].shift()
    df['RSI_p2'] = df['RSI_p1'].shift()
    return df

def MACD(df, column="Close", fast=12, slow=26, line=9):
    exp1 = df[column].ewm(span=fast, adjust=False).mean()
    exp2 = df[column].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()
    df = df.join(macd.to_frame('MACD'))
    df['MACD_p1'] = df['MACD'].shift()
    df['MACD_p2'] = df['MACD_p1'].shift()
    return df

def ml_input(df, VIX, trend='up', types='train'):
    df1 = RSI(df)[['RSI', 'RSI_p1', 'RSI_p2']]
    df2 = MACD(df)[['MACD', 'MACD_p1', 'MACD_p2']]
    if trend=='up' and types =='train':
        df3 = VIX['Close']
    if trend=='down' and types =='train':
        df3 = VIX['Close']
    if trend=='up' and types =='test':
        df3 = VIX['Close']
    if trend=='down' and types =='test':
        df3 = VIX['Close']
    df1 = df1.join(df2)
    df1 = df1.join(df3)
    df1.rename(columns={"Close": "VIX"},inplace=True)
    df1['VIX_p1'] = df1['VIX'].shift()
    df1['VIX_p2'] = df1['VIX_p1'].shift()
    df1['S&P_change'] = df['Close'].diff()
    
    df1.drop(index=df1.index[:26], inplace=True)
    df1.drop(index=df1.index[-5:], inplace=True)

    return df1

def ml_output(data, shift_forward=5):
    df = data.copy()
    diff = (df['Close'].shift(-shift_forward) - df['Close'])
    df['Trading Signal'] = -1
    df.loc[diff>=0, 'Trading Signal'] = 1
    
    df.drop(index=df.index[:26], inplace=True)
    df.drop(index=df.index[-5:], inplace=True)
    
    return df[['Trading Signal']]

def rsi_cal(row):
    if row['RSI']<30:
        order = 1
    elif row['RSI']>70:
        order = -1
    else:
        order = 0
    return order

def macd_cal(row):
    if row['MACD']>0:
        order = 1
    elif row['MACD']<0:
        order = -1
    else:
        order = 0
    return order

def mom_cal(row):
    if row['Mom']<15:
        order = 1
    elif row['Mom']>85:
        order = -1
    else:
        order = 0
    return order

from sklearn.ensemble import RandomForestClassifier
def rf_analysis(X,y):
    n_trees = 100
    rf = RandomForestClassifier(n_estimators=n_trees, max_depth=3, random_state=42)
    rf.fit(X.values, y.values.ravel())
    return rf

def backtester(prices, orders, trend='up', initial_cap=10000, commission=0.0035):
    position = 0
    shares = 0
    capital = initial_cap
    capital_list = []

    if trend == 'down' or trend == 'up':

        for order, price in zip(orders, prices):

            if order == -1 and position == 0:
                position = -1
                shares = capital / price[0]
                capital = capital + capital * (1 - commission) - shares * price[1]  
                
            elif order == 1 and position == 0:
                position = 1
                capital = capital * (1 - commission)
                shares = capital / price[0]
                
            elif (order == -1 or order == 0) and position == -1:
                capital = capital - shares * (price[1]-price_p)
                shares = shares
                position = position

            elif order == 1 and position == -1:
                position = 0
                capital = capital - shares * price[0] * commission
                shares = 0                         
                
            elif order == -1 and position == 1:
                position = 0
                capital = shares * price[0] * (1 - commission)
                shares = 0
                
            elif (order == 1 or order == 0) and position == 1:
                position = position
                shares = shares
                capital = shares * price[1]
            else:
                position = position
                shares = shares
                capital = capital
                
            price_p = price[1]
            capital_list.append(capital)
    
    return capital_list

def AnnualizedReturn(capitals, initial_cap=10000):

    cumulative_return = (capitals[-1] - initial_cap) / initial_cap
    days_held = len(capitals)
    annualized_return = (1 + cumulative_return)**(365 / days_held) - 1
    
    return annualized_return

def AnnualizedVolatility(capitals):

    daily_returns = np.diff(capitals) / capitals[1:]
    sigma = np.std(daily_returns)
    annualized_volatility = sigma * np.sqrt(252)
    
    return annualized_volatility

def SharpeRatio(capitals):
    
    sharpe_ratio = AnnualizedReturn(capitals) / AnnualizedVolatility(capitals)
    
    return sharpe_ratio

def MaxDrawdown(capitals):
    
    cap = pd.Series(capitals)
    max_drawdown = ((cap.cummax() - cap) / cap.cummax()).max()
    
    return max_drawdown

def CalulateStatistics(capitals, name='StrategyName'):
    
    ret = AnnualizedReturn(capitals)
    vol = AnnualizedVolatility(capitals)
    sharpe = SharpeRatio(capitals)
    drawdown = MaxDrawdown(capitals)
    
    df = pd.DataFrame([[ret*100, vol*100, sharpe, drawdown*100]], 
                      columns=['Annualized Return(%)', 'Annualized Volatility(%)', 
                               'Sharpe Ratio', 'Max Drawdown(%)'], 
                      index=[name])
    
    return df