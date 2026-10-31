from shakelab.libutils.geodetic import read_geometry, write_geometry
import matplotlib.pyplot as plt

collection = read_geometry('data/ISTAT_Italy_Regions_2018.geojson')

for poly in collection:
    x, y = poly.to_array()
    plt.plot(x, y)

plt.show(block=False)


write_geometry(collection, 'test.geojson')
