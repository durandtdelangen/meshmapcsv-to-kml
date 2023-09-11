
second = {'Point Num': '', 'Latitude': '', 'Longitude': '', 'Serial': '', 'Name': '', 'IP': '', 'Wlan': '', 'RSSI (SNR)': '', 'Cost': '', 'Signal': '', 'MAC Address': '', 'Channel': '', 'Frequency': '', 'Timestamp': ''}


class DataPoint:
    PointNum = None
    Latitude = None
    Longitude = None
    Serial = None
    Name = None
    IP = None
    Wlan = None
    RSSI = None
    Cost = None
    Signal = None
    Mac = None
    Channel = None
    Frequency = None
    Timestamp = None


    def toString(self):
        return f'{self.PointNum},{self.Signal},{self.Serial}'