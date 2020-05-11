#Протарифицировать абонента с IP-адресом 192.0.73.2
#с коэффициентом k: 0,5руб/Мб первые 200Мб, далее 1руб/Мб
import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
import math



ip = '192.0.73.2'
k = 0.5

#nfdump -r nfcapd.202002251200 -o \"fmt:%td %sa %da %byt\" > data.csv
def bill(Q):
    X = (Q - 200) + 200 * k
    return X


df = pd.read_csv('data_t.csv', skiprows = 1, header = None)
df.columns = ['ts', 'dur', 'srcIP', 'dstIP', 'bytes']

#in_trf = (df[df.dstIP == ip].bytes.sum())
#in_trf = int(in_trf) / 2 ** 20

in_trf = (df[df.dstIP == ip].bytes.values.astype(int))
in_trf = np.sum(in_trf)
in_trf = in_trf / 2 ** 10


out_trf = (df[df.srcIP == ip].bytes.values.astype(int))
out_trf = np.sum(out_trf)
out_trf = out_trf / 2 ** 10

trf =  out_trf + in_trf

connection_calc_src = df[df.srcIP == ip].bytes.count()
connection_calc_dst = df[df.dstIP == ip].bytes.count()
connection_calc = connection_calc_src + connection_calc_dst



print(f'Количество соединений с {ip} = {connection_calc}. В том числе {connection_calc_dst} входящих и {connection_calc_src} исходящих')
print(f'Счет составил {bill(trf):.2f} руб. за {trf:.2f} КБ')






