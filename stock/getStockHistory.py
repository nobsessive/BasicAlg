
# import modules
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
  
# initialize parameters
start_date = datetime(2023, 9, 7)
end_date = datetime(2023, 9, 7)
  
# get the data
data = yf.download('SPY', start = start_date,
                   end = end_date)
  
# display
plt.figure(figsize = (20,10))
plt.title('Opening Prices from {} to {}'.format(start_date,
                                                end_date))
plt.plot(data['Open'])
plt.show()

