# Overview
Implements a Healthcare application one module at a time. Currently only the device module has been designed.

# Branching Strategy
- Main branch will be for release ready code only.
- Development of features will occur in separate branches. This approach will be used for all of the modules in the project.
- Merging of a development branch can only occur if the code in the development branch is fully functional and completed unit testing.
- Updates to the devlopment branch will occur on a CI basis.


# Device Module
A device module a block that receives measurement data from different device types. The recieived data is checked for any error then is pushed to the data data management module for storage in the main database.

The types of devices are as follows :
- Type 1 : Temperature 
- Type 2 : Blood Pressure
- Type 3 : Blood Oxygen
- Type 4 : Heartrate
- Type 5 : Weight
- Type 6 : Glucometer

All measurement data is recievd in the form a JSON file. Depending on the device type, we expect certain data to be reported.

## JSON File
The contents of the JSON file always contain the following minumum information
- Device ID --> (DevID)
- Patient/User ID --> (UID)
- Device Type --> (DTxx)
- Key --> (TBD)
- Checksum --> (TBD)

## TODO
- Currently all errors are handled in the log file. Later, the errors will be sent to the error module instead.
- The output of the data now is just a txt file. This will need to change to be compatable with the database manager module.
- Will move to Java for the rest of the project. Provides better protection of user data.

