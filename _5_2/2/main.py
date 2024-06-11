import cartopy.crs as ccrs
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.Mollweide())
ax.stock_img()
plt.show()

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
plt.show()
