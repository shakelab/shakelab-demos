# ****************************************************************************
# Downloading data from a FDSN webservice
# ****************************************************************************

from shakelab.signals.fdsnws import FDSNClient

fc = FDSNClient('INGV')

fc.get_waveform(
    'IV.MODE..HN*',
    '2012-05-20T02:03:23.000000Z',
    '2012-05-20T02:06:23.000000Z',
    correct=False,
    file_name = 'data/MODE.mseed'
    )

fc.get_response(
    'IV.MODE..HN*',
    '2012-05-20T02:03:23.000000Z',
    '2012-05-20T02:06:23.000000Z',
    file_name = 'data/MODE.xml'
    )

sc = fc.get_waveform(
    'IV.MODE..HN*',
    '2012-05-20T02:03:23.000000Z',
    '2012-05-20T02:06:23.000000Z',
    )

rc = fc.get_response(
    'IV.MODE..HN*',
    '2012-05-20T02:03:23.000000Z',
    '2012-05-20T02:06:23.000000Z'
    )

sc_corr = sc / rc

record_corrected = sc_corr['IV.MODE..HNZ'][0]


catalogue = fc.get_catalogue(
    starttime='2023-01-01T00:00:00',
    endtime='2025-12-31T23:59:59',
    magnitude=(4.0, 9.0),
    latitude=(35.0, 45.0),
    longitude=(10.0, 20.0),
    depth=(0, 100))


fc.get_catalogue(
    starttime='2023-01-01T00:00:00',
    endtime='2025-12-31T23:59:59',
    magnitude=(4.0, 9.0),
    latitude=(35.0, 45.0),
    longitude=(10.0, 20.0),
    depth=(0, 100),
    file_name='data/catalogue_2023.xml'
)

info = fc.query_info(
    service='station'
    )

event_info = fc.query_info(
    service='event'
    )
