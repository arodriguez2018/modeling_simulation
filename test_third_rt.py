import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import datetime as dt

data = [ 
    {'timestamp': '2017-05-11 16:21:55', 'A': 0.724931, 'B': 0.361333, 'C': 0.517720},
    {'timestamp': '2017-05-11 16:22:25', 'A': 0.725386, 'B': 0.360833, 'C': 0.518632},
    {'timestamp': '2017-05-11 16:22:55', 'A': 0.725057, 'B': 0.361333, 'C': 0.521157},
    {'timestamp': '2017-05-11 16:23:25', 'A': 0.724402, 'B': 0.362133, 'C': 0.520002},
]
df = pd.DataFrame(data) 
df.set_index("timestamp")

plt.ion()
fig, ax = plt.subplots()
while True:
    dframe = df.copy()
    dframe['timestamp'] = pd.to_datetime(dframe['timestamp']) + pd.DateOffset(hours=2)
    dframe = dframe.set_index('timestamp')
    end = dframe.index.max()
    start= dt.timedelta(hours=1)
    dframe = dframe.loc[start:end]
    plt.pause(0.0001)
    ax.plot_date(dframe.index.to_pydatetime(), dframe, marker='', linestyle='solid')