#1sh# -*- coding: utf-8 -*-
#

import pandas as pd
import os
#import matplotlib.pyplot as plt
#floder_path = r'D\learning-file\项目文件\论文资料汇总\实验原始数据\工艺参数对模腔压力影响-更换螺杆后20180504\hys\工艺参数对模腔压力影响-更换螺杆后20180504\数据处理\注射阶段\zs60'


'''
合并所给文件夹下的csv文件
'''
floder_path = input('请输入文件路径：')

files = os.listdir(floder_path)
df = pd.DataFrame(index=range(10001))


for fl in files:
    if fl[-3:] == 'csv':#辨识文件名字内容,fl字符串末尾起始第三个字符
        file_path = os.path.join(floder_path,fl)
        
        data=pd.read_csv(file_path,engine='python')#读取每个csv数据
        
        df = pd.concat([df,data[:10001]], axis =1)#截取至10001行的数据
name_list = list(df.columns.unique())


'''导出到不同工作簿的一个excel'''
outfile_path = os.path.join(floder_path,'汇总.xlsx')
writer = pd.ExcelWriter(outfile_path) 
for name in name_list[1:]:
    tf = df[name]
    tf.columns = list(range(10))
    tf.index = df.iloc[:,0]     #加入时间列
    tf.to_excel(writer,name[:-4])
writer.save()

