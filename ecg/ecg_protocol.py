from protocol.general_protocol import General_Protocol
#把wave1，pack_rate写完

class Ecg_Protocol(General_Protocol):
    def __init__(self):
        super().__init__(self.__define_protocol())

    def __define_protocol(self):
        position_ecg1 = [[2,0,7,0],[1,0,1,7]]  # 第2个字节,bit0开始，走7位，放到dataecg1的bit0
        data_ecg1 = {'name':'wave1_ecg1','length':8,'position_list':position_ecg1,'value':0}
        pack_wave1 = {'name':'wave1','id':0x01,'length':7,'data_list':[data_ecg1]}
        pack_wave2 = {'name':'wave2','id':0x02,'length':6,'data_list':[]}
        pack_rate = {'name':'rate','id':0x04,'length':6,'data_list':[]}
        self.__protocol = {'sync_bit':0,'pack_list':[pack_wave1,pack_wave2,pack_rate]}
        return self.__protocol


if __name__ == '__main__':
    import os
    ecg = Ecg_Protocol()
    file = 'ECG_20140402092639.bin'
    filesize = os.path.getsize(file)
    packsize = 0
    length = 0
    if length > 0:
        filesize = min(filesize, length)
    with open(file, 'rb') as f:
        for i in range(filesize):
            pack_id = ecg.unpack_data(ord(f.read(1)))
            # if pack_id > 0:
            #     print(pack_id)
