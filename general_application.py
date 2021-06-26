

class General_Application():
    def __init__(self, protocol):
        self.__protocol = protocol
        self.__fun_dict = {}
        self.__unpack_data_value = {}

    def set_pack_fun(self, id, fun):
        self.__fun_dict[id] = fun

    def unpack_protocol_file(self, filename, readsize=0):
        print('exec unpack_protocol_file')

    def unpack_realtime_data(self, data):
        pack_id = self.__protocol.unpack_data(data)
        if pack_id in self.__fun_dict:
            self.__fun_dict[pack_id]()
        return pack_id

    def get_protocol_data(self, name):
        return self.__protocol.get_data(name)
