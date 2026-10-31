"""
rec2 = rec.copy()
rec3 = rec.copy()

rec2.filter(0.1,1, minphase=False)
rec3.filter(0.1,1, minphase=True)

plt.plot(rec.data/rec.peak_amplitude, 'k', label='dirac')
plt.plot(rec2.data/rec2.peak_amplitude, 'r', label='zero phase')
plt.plot(rec3.data/rec3.peak_amplitude, 'b', label='min phase')
plt.legend()
plt.show(block=False)
"""