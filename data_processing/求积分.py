# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:33:30 2018

@author: hys
"""

import pandas as pd
import os

time_1 = 6.87
time_2 = 15.8
file_names = []
columns_need = ['away [V]', 'close [V]', 'far [V]']

#floder_path = input('请输入文件路径：')
floder_path =  "C:/Users/hys/Desktop/30"
files = os.listdir(floder_path)

def get_integral(df):
    ing_1 = df[columns_need].apply(lambda x: 0.005*x.loc[:time_1].sum())   
    ing_2 = df[columns_need].apply(lambda x: 0.005*x[:time_2].sum())   
    max_d = df[columns_need].apply(lambda x: x[:time_1].max()) 
    df_ing = pd.DataFrame([max_d, ing_1, ing_2]).T
    df_ing.columns = ['max', 'sum1', 'sum2']
    return df_ing

df_deal = pd.DataFrame(columns=['max', 'sum1', 'sum2', 'file_name'])

for fl in files:
    file_path = os.path.join(floder_path,fl)
    if 'csv' in fl :
        
        data = pd.read_csv(file_path,engine='python')#读取每个csv数据
        data_hys = data.set_index("Time [s]")        
        
        temp = get_integral(data_hys)
        temp['file_name'] = [fl[:-4]] * 3        
        df_deal = pd.concat([df_deal, temp] ,axis=0)
        
        
df_deal.sort_index().to_excel(os.path.join(floder_path,'求积分.xlsx'))
        
        
        
