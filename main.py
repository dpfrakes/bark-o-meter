import audioop
from util import *


p = pyaudio.PyAudio()
frames = []
barks = 0
is_barking = False

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

rec_frames = int(RATE / CHUNK * RECORD_SECONDS)
delay = int(RATE / CHUNK * DELAY_SECONDS)

try:
    logger.info('Started recording')
    for _ in range(rec_frames):
        if _ > delay:
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
                        is_barking = True
                        logger.info('Bark!')
                elif is_barking:
                    is_barking = False
finally:
    logger.info('Stopped recording')

    logger.info('Total barks: {}'.format(barks))

    stream.stop_stream()
    stream.close()
    p.terminate()

    logger.debug('{} / {} = {}'.format(len(frames), RECORD_SECONDS, len(frames) / RECORD_SECONDS))
    logger.debug('{} total frames'.format(len(frames)))
    plot_signal(frames, RATE / CHUNK)
