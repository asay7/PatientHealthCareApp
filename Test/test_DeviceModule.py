import pytest
from DeviceModule import DeviceModule

def test_ReadTempDevice() -> None:
    dm  = DeviceModule("./Test/Data/", "./")
    assert dm.ReceiveData("BasicTempData.json") == 0
    dm.TransmitData()
    

def test_ReadPulseDevice() -> None:
    dm  = DeviceModule("./Test/Data/", "./")
    assert dm.ReceiveData("BasicPulseData.json") == 0
    dm.TransmitData()

def test_BadID() -> None:
    dm = DeviceModule("./Test/Data/", "./")
    assert dm.ReceiveData("BadUID.json") == -1