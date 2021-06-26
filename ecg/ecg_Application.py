from protocol.general_application import General_Application
from protocol.ecg.ecg_protocol import Ecg_Protocol


class Ecg_Application(General_Application):
    def __init__(self):
        super().__init__(Ecg_Protocol())
        self.set_pack_fun(0x01,self.__on_pack_wave1)
        self.__on_pack_wave1()

    def __on_pack_wave1(self):
        pass


if __name__ == '__main__':
    import os

    ecg = Ecg_Application()
    file = 'ECG_20140402092639.bin'
    filesize = os.path.getsize(file)
    packsize = 0
    length = 100
    if length > 0:
        filesize = min(filesize, length)
    with open(file, 'rb') as f:
        for i in range(filesize):
            pack_id = ecg.unpack_realtime_data(ord(f.read(1)))  #ecg.unpack_data(ord(f.read(1)))
            if pack_id == 1:
                print(ecg.get_protocol_data('wave1_ecg1'))
