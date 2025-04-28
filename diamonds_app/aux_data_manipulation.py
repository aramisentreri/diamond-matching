import glob
import pandas as pd
import numpy as np

def _column_to_int(s):
    #new_s = re.sub('][', '', s)    
    new_s = s.replace("[u'","")
    new_s = new_s.replace("']","")    
    return float(new_s)
def _column_to_string(s):
    new_s = s.replace("[u'","")
    new_s = new_s.replace("']","")    
    return new_s
def _cut_to_string(s):
    new_s = s.replace("[{u'labelSmall': u'", "")
    idx = new_s.find("'")
    new_s = new_s[:idx]
    return new_s

def get_the_data():
    data = []
    
    for name in glob.glob('diamonds_app/data_01_2018/data*'):        
        df = pd.read_csv(name)
        df = df[['carat','clarity','color','cut','price','detailsPageUrl']]
        data.append(df)
    
    data = pd.concat(data, axis=0)
    data['carat'] = data['carat'].apply(_column_to_int) 
    data['clarity'] = data['clarity'].apply(_column_to_string)  
    data['color'] = data['color'].apply(_column_to_string)
    
    data['cut'] = data['cut'].apply(_cut_to_string)
    return data

data = get_the_data()
def linear_model_prediction(color, cut, clarity, carat):

    ## Clearing the exponential relationship
    data['log_carat'] = np.log(data.carat)
    data['log_price'] = np.log(data.price)
    ## select appropiate data
    data2 = data[(data.color==color) & (data.clarity==clarity) & (data.cut == cut)]
    print("Size of data points to interpolate", data2.shape[0])

    from sklearn import linear_model
    regr = linear_model.LinearRegression()
    
    regr.fit(data2.log_carat.values.reshape(-1,1), data2.log_price.values.reshape(-1,1))
    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
          % np.mean((regr.predict(data2.log_carat.values.reshape(-1,1)) - data2.log_price.values.reshape(-1,1)) ** 2))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % regr.score(data2.log_carat.values.reshape(-1,1), data2.log_price.values.reshape(-1,1)))
    predicted_price = np.exp(regr.predict(np.log(carat)))
    graph_data = data2.groupby(by=['carat'],as_index=False).price.mean().values 
    
    links = data2[data2.price <= predicted_price[0][0]].detailsPageUrl.values
    
    return predicted_price, graph_data, links    

