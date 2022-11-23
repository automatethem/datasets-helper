import numpy as np

'''
transformer = MinMaxScaler()
train_np_array = transformer.fit_transform(train_df[['Close']])
val_np_array = transformer.transform(val_df[['Close']])
train_x, train_label = slice_time_series_data_from_np_array(train_np_array, x_column_indexes=[0], label_column_indexes=[0], window_length=4)
#print(train_x.shape) #
#print(train_labels.shape) #
#print(val_x.shape) #
#print(val_labels.shape) #
'''
'''
transformer = MinMaxScaler()
train_np_array = transformer.fit_transform(train_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])
val_np_array = transformer.transform(val_df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])
train_x, train_label = slice_time_series_data_from_np_array(train_np_array, x_column_indexes=[0, 1, 2, 3, 4], label_column_indexes=[3], window_length=4)
#print(train_x.shape) #(973, 7, 6)
#print(train_labels.shape) #(973, 1)
#print(val_x.shape) #(238, 7, 6)
#print(val_labels.shape) #(238, 1)
'''
def slice_time_series_data_from_np_array(np_array, x_column_indexes=None, label_column_indexes=None, sequence_length=3):
    #print(np_array.shape) #(980, 1)
    window_length = sequence_length + 1
    x = []
    labels = []
    for i in range(0, len(np_array) - window_length + 1): #0 ~ (980 - 4 - 1) 
        window = np_array[i:i + window_length, :]
        if x_column_indexes:
            x.append(window[:-1, x_column_indexes])
        else:
            labels.append(window[:-1, :])
        if label_column_indexes:
            labels.append(window[-1, label_column_indexes])
        else:
            labels.append(window[-1, :])
    x = np.array(x)
    labels = np.array(labels)
    #print(x.shape) #(977, 3, 1)
    #print(labels.shape) #(977, 1)
    return x, labels 

#x, y = slice_time_series_data_from_df(df, x_columns=['Close'], label_columns=['Close'], sequence_length=3)
#x, y = slice_time_series_data_from_df(df, x_columns=['Open', 'High', 'Low', 'Adj Close', 'Volume', 'Close'], label_columns=['Close'], window_length=4)
def slice_time_series_data_from_df(df, x_columns=None, label_columns=None, window_length=4):
    #print(df.shape) #(1225, 7)
    window_length = sequence_length + 1
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
