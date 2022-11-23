import numpy as np

#x, y = slice_time_series_data(df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])
def slice_time_series_data(df, window_length=4):
    #print(df.shape) #(1225, 7)
    x = []
    y = []
    for i in range(0, len(df) - window_length + 1): #0 ~ (1225 - 4 - 1) 
        window = df.iloc[i:i + window_length, :]
        x.append(window.iloc[:-1, :])
        y.append(window.iloc[-1, :])
    x = np.array(x)
    y = np.array(y)
    #print(x.shape) #(1222, 3, 7)
    #print(y.shape) #(1222, 7)
    return x, y
