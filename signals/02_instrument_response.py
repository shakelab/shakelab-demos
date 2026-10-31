# ****************************************************************************
# Stage response
# ****************************************************************************

from shakelab.signals.response import StageGain, StagePoleZero
from shakelab.signals.io import reader

# Passing response information by dictionary

data = {
    'description': None,
    'sensitivity': 1.0197,
    'frequency': 0.2,
    'stage_number': 1
    }

stage_gain_1 = StageGain(data)

data = {
    'description': None,
    'input_units': 'm/s**2',
    'output_units': 'V',
    'pz_type': None,
    'normalization_factor': 246.0e11,
    'normalization_frequency': 0.2,
    'poles': [-981.-1009.j, -981.+1009.j, -3290.-1263.j, -3290.+1263.j],
    'zeros': [],
    'stage_number': 1
    }

stage_paz = StagePoleZero(data)

data = {
    'description': None,
    'sensitivity': 314573,
    'frequency': 0,
    'stage_number': 2
    }

stage_gain_2 = StageGain(data)


# Correcting a file for instrument response

stream_collection = reader('data/Emilia_1st_shock/MODE.mseed')

record_raw = stream_collection['IV.MODE..HNZ'][0]

record_corrected = record_raw / stage_gain_1 / stage_paz / stage_gain_2


# Passing response information by argument

stage_paz = StagePoleZero(
    input_units = 'm/s**2',
    output_units = 'V',
    pz_type = None,
    normalization_factor = 246.0e11,
    normalization_frequency = 0.2,
    poles = [-981.-1009.j, -981.+1009.j, -3290.-1263.j, -3290.+1263.j],
    zeros = [],
    stage_number = 1
    )

# ****************************************************************************
# Reading response information from station xml file
# ****************************************************************************

from shakelab.signals.stationxml import parse_sxml
from shakelab.signals.response import ResponseCollection

response_collection = parse_sxml("data/Emilia_1st_shock/MODE.xml")
stream_collection = reader('data/Emilia_1st_shock/MODE.mseed')

stream_collection.deconvolve_response(response_collection)

record_corrected = stream_collection['IV.MODE..HNZ'][0]

# ****************************************************************************
# Reading response information from station xml file
# ****************************************************************************

from shakelab.signals.response import ResponseCollection
from shakelab.signals.io import reader

response_collection = ResponseCollection()

response_collection.read("data/Emilia_1st_shock/MODE.xml")
stream_collection = reader('data/Emilia_1st_shock/MODE.mseed')

stream_collection.deconvolve_response(response_collection)

record_corrected = stream_collection['IV.MODE..HNZ'][0]

response_collection.write('data/Emilia_1st_shock/MODE.json')


response_collection = ResponseCollection()
response_collection.read('data/Emilia_1st_shock/MODE.json')

response_collection.response[0].stageset[0].info()
response_collection.response[0].stageset[0].match('2009-04-07T08:00:00')
response_collection['IV.MODE..HNZ']['2009-04-07T08:00:00']

response_collection['IV.MODE..HNZ']['now'].info()