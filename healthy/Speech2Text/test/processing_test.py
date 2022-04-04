import pytest
from processing import multi_exec, thread_exec


def test_thread() -> None:
    work = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert multi_exec(work) > thread_exec(work)


def test_multi() -> None:
    work = [1, 1, 1, 1]
    assert multi_exec(work) > thread_exec(work)
