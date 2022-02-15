from importlib.resources import path
import json
import logging
import sys

logging.basicConfig(level=logging.INFO, filename="./app.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("appdata")

#will need to do alot of checking with the data management module at some point
class DeviceModule:
    def __init__(self, path_in, path_out)-> None:
        self.TX = path_out 
        self.RX = path_in

        '''
         Loads data from an external JSON file into the device module.
        '''
    def ReceiveData(self, file)-> None:
        jf = open(f'{self.RX}{file}')
        data = json.load(jf)
        logger.info(f'Finished reading {file}.')
        return 0

        '''
         Sends data to data management module
        '''
    def TransmitData(self)-> None:
        with open(f'{self.TX}DM_Message.txt', 'w') as ft:
            ft.write("Hello There")
        logger.info("Message sent to Data Manager.")
        return 0

def run()-> None:
    dm  = DeviceModule("./Test/Data/", "./")
    dm.TransmitData()

if __name__ == "__main__":
    run()