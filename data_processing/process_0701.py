import pandas as pd
import os

def select_df(df,threshold=22):
    '''截取注射阶段数据'''
    tf = df[df['weizhi [V]'] > threshold].copy()
    tf['Time [s]'] -= tf.iloc[0,0]
    tf.set_index('Time [s]')
    return tf

def process(source_file, target_file):
    print("source_file:{}".format(source_file))
    print("target_file:{}".format(target_file))

    data = pd.read_csv(source_file)        
    result = select_df(data,22)
    result.to_csv(target_file,index= False)


if __name__ == '__main__':
    source_dir = "C:/Users/hys/Desktop/30"
    target_dir = "C:/Users/hys/Desktop/30"
    #source_dir = "."
    #target_dir = "./result"
    for file_name in os.listdir(source_dir):
        if ('csv' in file_name) and ('result' not in file_name):
            source_file = os.path.join(source_dir, file_name)
            target_file = os.path.join(target_dir, "result_"+file_name)
            process(source_file, target_file)

