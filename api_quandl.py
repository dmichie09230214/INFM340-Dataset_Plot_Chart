import quandl
quandl.ApiConfig.api_key = 'prs2KduTisTpfjuYrWwU'
import pandas as pdr
import datetime
import matplotlib.pyplot as plt

w = quandl.get('EOD/DIS', start_date="2016-12-01", end_date="2017-12-30")


plt.plot(w)
plt.show()