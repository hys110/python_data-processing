import sys
import pandas as pd



if __name__ == '__main__':
    source_file = sys.argv[1]
    target_file = sys.argv[2]
    print("source_file:{}".format(source_file))
    print("target_file:{}".format(target_file))

    threshold = 22

    data = pd.read_csv(source_file)
    N = data.shape[0]

    idx = (data["weizhi [V]"] > threshold)  # 判断该列每个数值是否大于阈值
    for i in range(N):   # 0,1,2,...,N-1 一个个判断
        if idx[i]:
            break
    start = i

    for i in range(N-1,-1,-1):    # N-1, ..., 1,0 一个个判断
        if idx[i]:
            break
    finish = i+1

    result = data[start:finish]
    result.to_csv(target_file)
