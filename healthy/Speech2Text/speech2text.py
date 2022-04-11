import pvleopard
import logging
import concurrent.futures as cf
import time
from os import environ, path
from dotenv import load_dotenv, dotenv_values

logging.basicConfig(filename='speech2txt.log', level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s: %(messages)s [in %(filename)s: %(lineno)d]')

load_dotenv()
basedir = path.abspath(path.dirname(__file__))
dotenv_values(path.join(basedir, '.env'))
ACCESS_KEY = environ.get('ACCESS_KEY')
leo = pvleopard.create(access_key=ACCESS_KEY)


def speech2txt_wrapper(audiofile):
    '''
    Simple wrapper for the speech-to-text model. Each thread needs to create a new instance of a model to run.
    The total time used for each thread is also reported along with the translated results.
    '''
    start = time.perf_counter()
    leo = pvleopard.create(access_key=ACCESS_KEY)
    message = leo.process_file(audiofile)
    stop = time.perf_counter()
    leo.delete()
    return message, round((stop - start), 3)


def speech2txt(audiofiles:list):
    '''
    This function takes in a user recorded audio files and returns what was said in the recording
    as text.

    :param audiofiles: list of audio files to feed into the system
    :return:
    '''
    with cf.ThreadPoolExecutor() as cfex:
        results = cfex.map(speech2txt_wrapper, audiofiles)
    return results


if __name__ == "__main__":

    audiolist = [
        './data/audio/TEST_SPEECH_1.wav',
        './data/audio/TEST_SPEECH_2.wav',
        './data/audio/TEST_SPEECH_3.wav'
    ]
    speech = speech2txt(audiolist=audiolist)
    for i in speech:
        print(i)
