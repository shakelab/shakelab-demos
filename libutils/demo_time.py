from shakelab.libutils.time import Date

d1 = Date([1985, 10, 26, 1, 21, 0.0])
print('Current date: {0}'.format(d1))

seconds = d1.to_seconds()
print('Elapsed seconds from reference time: {0}s'.format(seconds))

d2 = Date(seconds + 10)
print('Date from seconds + 10: {0}'.format(d2))

seconds = d2 - d1
print('Seconds between two date objects: {0}s'.format(seconds))

d2.shift_time(3, units='h')
print('Date shifted of 3h: {0}'.format(d2))

d3 = d1 + 50
print('New date with increment of 50s: {0}'.format(d3))


