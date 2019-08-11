import audioop
from datetime import datetime

from util import *

p = pyaudio.PyAudio()
frames = []
barks = 0

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

logger.info('Started recording')
start_time = datetime.now()
is_barking = False

try:
    while True:
        data = stream.read(CHUNK)
        rms = audioop.rms(data, 2)
        # Not sure why this is spiking at the beginning of each recording session...
        if rms > CRAZY_THRESHOLD:
            logger.debug('ignoring anomaly')
        else:
            frames.append(rms)
            if rms > RMS_THRESHOLD:
                if not is_barking:
                    barks += 1
                    logger.info('Bark!')
                    is_barking = True
            elif is_barking:
                is_barking = False

except KeyboardInterrupt as e:
    logger.debug(e.message)

finally:
    logger.info('Stopped recording')
    stop_time = datetime.now()
    logger.info('{} barks in {} seconds'.format(barks, stop_time - start_time))

    stream.stop_stream()
    stream.close()
    p.terminate()

    logger.info('Pass frames to front end for data visualization')

    plot_signal(frames, RATE / CHUNK, start_time.strftime('%Y%m%d_%H%M%S'))
