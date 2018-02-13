import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdate

# x = np.arange(1, 11, 1)
#
# plt.plot(x, x)
#
# # plt.locator_params(nbins=20)
#
# plt.locator_params('x', nbins=5)
#
# plt.show()

fig = plt.figure()

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 1, 1)
delta = datetime.timedelta(days=1)

dates = mdate.drange(start, end, delta=delta)

date_format = mdate.DateFormatter('%Y-%m-%d')

y = np.random.randn(len(dates))

ax = plt.gca()

plt.plot_date(dates, y, linestyle='-')

fig.autofmt_xdate()

plt.show()