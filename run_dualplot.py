#%%
from dualplot import DualPlot
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["grid.linestyle"] = "-"
plt.rcParams["grid.alpha"] = 0.5

#%%

change = pd.read_excel(
    # "http://www.rbnz.govt.nz/-/media/ReserveBank/Files/Statistics/Key%20graphs/graphdata.xlsx",
    "data/graphdata.xlsx",
    sheet_name="NZDUSD",
    header=0,
    skiprows=3,
    skipfooter=2,
    usecols=[1, 2, 3],
    parse_dates=True,
).rename(columns={"Unnamed: 1": "Date"})
#%%

# create the dual plot object
dp = DualPlot(figsize=(7, 4))
# plot data on the left axis
dp.plot_left(
    change["Date"],
    change["NZD/USD Exchange Rate"],
    label="NZD / USD exchange rate (left axis)",
)
# plot data on the right axis
dp.plot_right(change["Date"], change["TWI"], label="Trade-weighted index (right axis)")

# set range of the x axis
# dp.axleft.set_xlim(["1984-01-01", "2016-01-01"])
# add legend
dp.legend(frameon=False)
# add labels
dp.set_ylabel_left("US dollars for one NZD dollar")
dp.set_ylabel_right("Index")
# set the number of major ticks
dp.axleft.locator_params(axis="y", nbins=4)
dp.axright.locator_params(axis="y", nbins=4)

plt.show()


#%%
