import numpy as np

#x, y = slice_time_series_data(df, x_columns=['Close'], label_columns=['Close'], window_length=4)
#x, y = slice_time_series_data(df, x_columns=['Open', 'High', 'Low', 'Adj Close', 'Volume', 'Close'], label_columns=['Close'], window_length=4)
def slice_time_series_data(df, x_columns=None, label_columns=None, window_length=4):
    #print(df.shape) #(1225, 7)
    x = []
    y = []
    for i in range(0, len(df) - window_length + 1): #0 ~ (1225 - 4 - 1) 
        window = df.iloc[i:i + window_length, :]
        if x_columns:
            x.append(window[x_columns].iloc[:-1, :])
        else:
            x.append(window.iloc[:-1, :])
        if label_columns:
            y.append(window[label_columns].iloc[-1, :])
        else:
            y.append(window.iloc[-1, :])
    x = np.array(x)
    y = np.array(y)
    #print(x.shape) #(1222, 3, 1)
    #print(y.shape) #(1222, 1)
    return x, y
