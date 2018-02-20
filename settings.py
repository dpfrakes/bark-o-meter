import pyaudio

from logger import setup_logger

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
DELAY_SECONDS = 0

RMS_THRESHOLD = 1000
CRAZY_THRESHOLD = 5000

logger = setup_logger()
