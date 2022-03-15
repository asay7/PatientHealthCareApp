class DeviceModule:
    def __init__(self) -> None:
        self.json_bodylength = 7
        self.json_measlength = 4

        self.mvalues = {
            "Temperature": {'device_type': 1, 'units': {'C': {'min': 0, 'max': 40}, 'F': {'min': 32, 'max': 200}}},
            "Heartrate": {'device_type': 2, 'units': {'BPM': {'min': 20, 'max': 200}}},
            'Glucometer': {'device_type': 3,
                           'units': {'mm/dL': {'min': 0, 'max': 100}, 'mmol/L': {'min': 0, 'max': 100}}},
            'BloodPressure': {'device_type': 4, 'units': {
                'mmHg': {'min_systolic': 0, 'max_systolic': 120, 'min_diastolic': 0, 'max_diastolic': 120}}},
            'Oximeter': {'device_type': 5, 'units': {'%SpO2': {'min': 0, 'max': 100}}},
            'Weight': {'device_type': 6, 'units': {"lbs": {'min': 0, 'max': 500}, 'kg': {'min': 0, 'max': 250}}}
        }

    def validFormat(self, jsonfile) -> bool:

        if len(jsonfile) != self.json_bodylength:
            print(len(jsonfile))
            return False
        if len(jsonfile['MeasurementData']) != self.json_measlength:
            print(len(jsonfile["MeasurementData"]))
            return False
        return True

    def validMeasurement(self, data, devtype) -> bool:

        # Verify that the type of measurement mode is supported.
        meas_type = "none"
        for ty in self.mvalues:
            if data['MeasType'] in self.mvalues:
                meas_type = data["MeasType"]
                break

        if meas_type == 'none':
            return False

        # Check the device type is correct for the given measurement.
        if self.mvalues["MeasType"]["device_type"] != devtype:
            return False

        # Check the units given
        meas_units = 'none'
        for un in self.mvalues[meas_type]['units']:
            if data["Units"] in self.mvalues[meas_type]['units']:
                meas_units = data["Units"]
                break

        if meas_units == 'none':
            return False

        # Check the range of given measurement values
        meas_value = data["Value"]
        if meas_type != "BloodPressure":
            meas_min = self.mvalues[meas_type]['units'][meas_units]['min']
            meas_max = self.mvalues[meas_type]['units'][meas_units]['max']
            if (meas_value[0] < meas_min) or (meas_value[0] > meas_max):
                return False
        else:
            meas_value_sy = meas_value[0]
            meas_value_di = meas_value[-1]
            meas_min_sy = self.mvalues[meas_type]['units'][meas_units]['min_systolic']
            meas_max_sy = self.mvalues[meas_type]['units'][meas_units]['max_systolic']
            meas_min_di = self.mvalues[meas_type]['units'][meas_units]['min_diastolic']
            meas_max_di = self.mvalues[meas_type]['units'][meas_units]['max_diastolic']
            if (meas_min_sy < meas_value_sy) or (meas_value_sy > meas_max_sy):
                return False
            if (meas_min_di < meas_value_di) or (meas_value_di > meas_max_di):
                return False
        return True
