exec(open('imports.py').read())
def check_stationarity(timeseries):
  """
  Performs an Augmented Dickey-Fuller test to check stationarity of a time series.

  Args:
    timeseries: A pandas Series representing the time series data.

  Returns:
    None. Prints the results of the ADF test.
  """
  result = adfuller(timeseries)
  print('ADF Statistic: %f' % result[0])
  print('p-value: %f' % result[1])
  print('Critical Values:')
  for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))

def set_plotcolor(x,y):
    fig,ax = plt.subplots(facecolor='slategray',figsize=(x,y))
    ax=plt.gca()
    ax.set_facecolor('lightgrey')
