import quandl
quandl.ApiConfig.api_key = 'prs2KduTisTpfjuYrWwU'
import pandas as pdr
import datetime
import matplotlib.pyplot as plt

w = quandl.get('EOD/DIS', start_date="2016-12-01", end_date="2017-12-30")


plt.plot(w)
plt.show()

#user will need to register at the quandl site
#once register, user is provided with an API that is needed. 
#program is created and perform by PyCharm
#Quandl will need to be downloaded by running pip install quandl
