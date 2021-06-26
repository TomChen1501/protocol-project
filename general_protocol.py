
class General_Protocol():
    def __init__(self, protocol):
        self.__protocol = protocol
        self.__pack_data = [0]*max([pack['length'] for pack in protocol['pack_list']]) #self.__protocol['max_length']
        self.__pack_length = {}
        self.__pack_id = {}
        self.__unpack_data = {}
        self.__pick_data = {}
        for pack in protocol['pack_list']:
            self.__pack_length[pack['id']] = pack['length']
            self.__pack_id[pack['id']] = pack
            for data in pack['data_list']:
                self.__unpack_data[data['name']] = data['value']
                self.__pick_data[data['name']] = self.__position_to_pick(data['position_list'])

    def unpack_data(self, data):
        self.__pack_data = self.__pack_data[1:] + [data]
        id = 0
        if self.__is_full_pack(self.__pack_data,self.__protocol['sync_bit'],self.__pack_length):
            id = self.__pack_data[0] & 0x7f
            if id in self.__pack_id:
                self.__data_calculation(id)
        return id

    def __is_full_pack(self, pack_data,sync_bit,pack_length):
        if (pack_data[0] & 0x80) >> 7 == sync_bit:
            pack_id = pack_data[0] & 0x7f
            if pack_id in pack_length:
                for i in range(1,pack_length[pack_id]):
                    a = pack_data[i] & 0x80
                    value = a >> 7
                    if value == sync_bit:
                        return False
                return True
        return False

    def __position_to_pick(self, position_list):
        test_list = []
        for pos in position_list:
            test = 0x00
            for i in range(pos[1], pos[1] + pos[2]):
                num = 0x01 << i
                test = test | num
            test_list.append([pos[0], pos[1], pos[2], pos[3], test])
        return test_list

    def __data_calculation(self, id):
        pack = self.__pack_id[id]
        for data in pack['data_list']:
            sum = 0
            for each in self.__pick_data[data['name']]:
                value = ((self.__pack_data[each[0]] & each[4]) >> each[1]) << each[3]
                # value = ((self.__pack_data[pos[0]] & test) >> pos[1]) << pos[3]
                sum = sum | value
            self.__unpack_data[data['name']] = sum

    def get_data(self, name):
        if name in self.__unpack_data:
            return self.__unpack_data[name]
        else:
            print('error name')
            return 'error name'


if __name__ == '__main__':
    pass
