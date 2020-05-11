import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data_t.csv', skiprows = 1, header = None)
df.columns = ['ts', 'dur', 'srcIP', 'dstIP', 'bytes']

df.bytes = df.bytes.apply(lambda row: int(row) if 'M' not in row else (int(float(row[:-1])*10**6)))

ts = df.ts.apply(lambda row: row[:15])

df.ts = pd.to_datetime(ts, format='%Y-%m-%d%H:%M')

df.plot(x='ts', y='bytes')
plt.title('График зависимости объема трафика от времени')
plt.ylabel('Количество байт')
plt.xlabel('Время')
plt.show()




