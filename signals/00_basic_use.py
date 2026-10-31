# ****************************************************************************
# Creating a simulated Record object from scratch
# ****************************************************************************

import numpy as np
from shakelab.signals.base import Record, Stream

# creating a Dirac pulse signal
dirac_pulse = np.zeros(10001)
dirac_pulse[5001] = 1

rec0 = Record(data=dirac_pulse, delta=0.001,
              time='2024-06-20T12:00:00.0000', sid='DIR01')

# or identically
rec1 = Record()
rec1.delta = 0.001
rec1.time = '2024-06-20T12:00:10.0010'
rec1.data = dirac_pulse

# Note that record parameters are stored in the record's header
rec1.head.sid = 'DIR01'
print(rec1.head)


# ****************************************************************************
# Adding Record to a Stream
# ****************************************************************************

from shakelab.signals.base import Stream

st = Stream('DIR01')

# Contiguous and overlapping records are merged
st.append(rec0)
st.append(rec1)

# Non-contiguous record are append as independent chunks
rec2 = Record(data=dirac_pulse, delta=0.001,
              time='2024-06-20T15:00:00.0000', sid='DIR01')

st.append(rec2)
print(st)