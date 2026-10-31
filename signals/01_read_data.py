# ****************************************************************************
# Reading data within an initialised Stream Collection
# ****************************************************************************

from shakelab.signals.base import StreamCollection

# Initialise the stream collection
sc = StreamCollection()

# Import data to an existing collection
sc.read('data/Emilia_1st_shock/ESM/IV.MODE..HNZ.IT-2012-0008.ACC.MP.mseed')

# Adding new data to the collection
sc.read('data/Emilia_1st_shock/ESM/IV.MODE..HNN.IT-2012-0008.ACC.MP.mseed')
sc.read('data/Emilia_1st_shock/ESM/IV.MODE..HNE.IT-2012-0008.ACC.MP.mseed')

# ****************************************************************************
# Reading data using the reader function
# ****************************************************************************

from shakelab.signals.io import reader

sc = reader('data/Emilia_1st_shock/ESM/IV.MODE..HNZ.IT-2012-0008.ACC.MP.mseed')

# Adding new data to an existing collection
reader('data/Emilia_1st_shock/ESM/IV.MODE..HNN.IT-2012-0008.ACC.MP.mseed',
        stream_collection=sc)
reader('data/Emilia_1st_shock/ESM/IV.MODE..HNE.IT-2012-0008.ACC.MP.mseed',
        stream_collection=sc)

# ****************************************************************************
# Reading multiple files from a folder
# ****************************************************************************

from shakelab.signals.io import reader

# just directory
sc = reader('data/Emilia_1st_shock/ESM/')

# all files in a directory (files can be of different format)
sc = reader('data/Emilia_1st_shock/ESM/*')

# only specific files
sc = reader('data/Emilia_1st_shock/ESM/*ACC.*.mseed')

# note: the same can be obtained within the Stream Collection

# ****************************************************************************
# Obtaining information from a Stream Collection
# ****************************************************************************

# Method 1
sc.info()
sc.stream[0].info() # single stream
sc.stream[0].record[0].info() # single record
# or
sc[0].info() # single stream
sc[0][0].info() # single record

# Method 2
print(sc)
print(sc.stream[0]) # single stream
print(sc.stream[0].record[0]) # single record
# or
print(sc[0]) # single stream
print(sc[0][0]) # single record