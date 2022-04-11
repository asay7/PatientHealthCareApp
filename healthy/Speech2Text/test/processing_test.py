import pytest
from healthy.Speech2Text.processing import multi_exec, thread_exec
from healthy.Speech2Text.speech2text import speech2txt
import time
import os


def test_thread() -> None:
    """
    Test the threading performance and compares it to the multiprocessing performance
    """
    #print(os.path.abspath(os.getcwd()))
    work = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert multi_exec(work) > thread_exec(work)


def test_multi() -> None:
    work = [1, 1, 1, 1]
    assert multi_exec(work) > thread_exec(work)


def test_speech2text() -> None:
    """
    Tests the speech2text functionality running as a queue system.
    The total runtime time should be less than the sum of all audio,
    and the audio should be translated correctly.
    """

    ans = ['EXPERIENCE PROVES THIS',
           'WHY SHOULD ONE HALT ON THE WAY',
           'YOUR POWER IS SUFFICIENT I SAID'
           ]
    audiolist = [
        '../data/audio/TEST_SPEECH_1.wav',
        '../data/audio/TEST_SPEECH_2.wav',
        '../data/audio/TEST_SPEECH_3.wav'
    ]
    total_time = 0
    start = time.perf_counter()
    speech = speech2txt(audiolist=audiolist)
    stop = time.perf_counter()

    for i in speech:
        # print(i[0])
        total_time += float(i[-1])
        assert i[0] in ans
    assert (stop - start) < total_time
