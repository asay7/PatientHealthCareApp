from importlib.resources import path
import json
import logging

logging.basicConfig(level=logging.INFO, filename="./app.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("appdata")

#will need to do alot of checking with the data management module at some point
class DeviceModule:
    def __init__(self, path_in, path_out)-> None:
        self.TX = path_out 
        self.RX = path_in

        self.DevType = {1:"Temperature", 2:"Heartrate"}
        self.UIDs = {"U9193902":("D2017868", "D2017468")} #data base check if user is registered with current device 
        self.DevIDs = {"D2017868":1, "D2017468":2} #list of device IDs and the type of device they belong to
        self.jdata = "Empty"
        self.meas = 0
        '''
         Loads data from an external JSON file into the device module.
        '''
    def ReceiveData(self, file)-> None:
        jf = open(f'{self.RX}{file}')
        self.jdata = json.load(jf)
        if(self.CheckUID() == 1):#basic user check of data
            return -1
        logger.info(f'Finished reading {file}.')
        dtp = self.jdata["DeviceType"]
        self.data = self.jdata["MeasurementData"][self.DevType[dtp]]
        
        jf.close()
        return 0

        '''
         Sends data to data management module
        '''
    def TransmitData(self)-> None:
        with open(f'{self.TX}DM_Message.txt', 'w') as ft:
            ft.write(f'{self.DevType[self.jdata["DeviceType"]]} = {self.data}')
        logger.info("Message sent to Data Manager.")
        ft.close()
        return 0

        '''
        Does a basic check of the user ID by comparing it to the database. If an ID is detected as unknown, an error is generated
        '''
    def CheckUID(self) -> None:
        user_id = self.jdata["UserID"]
        device_id = self.jdata["DeviceID"]
        device_type = self.jdata 
        if(self.jdata["UserID"] not in self.UIDs):
            logger.error(f'Unknown user with ID="{self.jdata["UserID"]}')
            return 1
        else:
            return 0

def run()-> None:
    dm = DeviceModule("./Test/Data/", "./")
    dm.ReceiveData("BadUID.json")
    dm.TransmitData()

if __name__ == "__main__":
    run()