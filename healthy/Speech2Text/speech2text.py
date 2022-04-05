import pvleopard
import logging
import concurrent.futures as cf
import time
from os import environ, path
from dotenv import load_dotenv, dotenv_values

logging.basicConfig(filename='speech2txt.log', level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s: %(messages)s [in %(filename)s: %(lineno)d]')


def speech2txt(audiolist):
    '''
    This function takes in a user recorded audio file and returns what was said in the recording
    as text. Eventually, decoded recordings will be stored in the database.

    :param filename: audio file (.wav) format.
    :return:
    '''
    start = time.perf_counter()
    ACCESS_KEY = environ.get('ACCESS_KEY')
    leo = pvleopard.create(access_key=ACCESS_KEY)
    with cf.ThreadPoolExecutor() as cfex:
        results = cfex.map(leo.process_file, audiolist)
    stop = time.perf_counter()
    leo.delete()
    logging.info(f'Audio processed in {round((stop - start), 2)} seconds')
    return results


if __name__ == "__main__":
    load_dotenv()
    basedir = path.abspath(path.dirname(__file__))
    dotenv_values(path.join(basedir, '.env'))
    audiolist = [
        './data/audio/2830-3980-0043.wav',
        #'./data/audio/4507-16021-0012.wav',
        #'./data/audio/28455-210777-0068.wav'
    ]
    speech = speech2txt(audiolist=audiolist)
    for i in speech:
        print(i)
