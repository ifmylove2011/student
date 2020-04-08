# -*- coding: utf-8 -*-

import os


class Constant_Base:
    tag = 0
    length = 0
    data = bytes()

    def __init__(self, tag, length):
        self.tag = tag
        self.length = length
        self.data = bytes(self.offset())

    def len(self):
        return self.length

    def offset(self):
        return self.length - 1

    def print(self):
        print('{0} {1}'.format(self.bytes_hex(bytes([self.tag])), self.bytes_hex(self.data)))

    def bytes_hex(self, s):
        lin = ['%02X' % i for i in s]
        return " ".join(lin)


class Constant_Class_info(Constant_Base):
    name_index = 0  # u2

    def __init__(self, ):
        Constant_Base.__init__(self, 7, 3)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nname_index= {1} \r\n'.format(self.tag, self.name_index))

    def read(self):
        self.name_index = bytes_int(self.data)


class Constant_Fieldref_info(Constant_Base):
    class_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 9, 5)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nclass_index= {1} \r\nname_and_type_index= {2} \r\n'.format(self.tag, self.class_index,
                                                                                       self.name_and_type_index))

    def read(self):
        self.class_index = bytes_int(self.data[:2])
        self.name_and_type_index = bytes_int(self.data[2:])


class Constant_Methodref_info(Constant_Base):
    class_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 10, 5)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nclass_index= {1} \r\nname_and_type_index= {2} \r\n'.format(self.tag, self.class_index,
                                                                                       self.name_and_type_index))

    def read(self):
        self.class_index = bytes_int(self.data[:2])
        self.name_and_type_index = bytes_int(self.data[2:])


class Constant_InterfaceMethodref_info(Constant_Base):
    class_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 11, 5)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nclass_index= {1} \r\nname_and_type_index= {2} \r\n'.format(self.tag, self.class_index,
                                                                                       self.name_and_type_index))

    def read(self):
        self.class_index = bytes_int(self.data[:2])
        self.name_and_type_index = bytes_int(self.data[2:])


class Constant_String_info(Constant_Base):
    string_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 8, 3)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nstring_index= {1} \r\n'.format(self.tag, self.string_index))

    def read(self):
        self.name_index = bytes_int(self.data)


class Constant_Integer_info(Constant_Base):
    bytes = 0  # u4

    def __init__(self):
        Constant_Base.__init__(self, 3, 5)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nbytes= {1} \r\n'.format(self.tag, self.bytes))

    def read(self):
        self.bytes = bytes_int(self.data)


class Constant_Float_info(Constant_Base):
    bytes = 0  # u4

    def __init__(self):
        Constant_Base.__init__(self, 4, 5)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nbytes= {1} \r\n'.format(self.tag, self.bytes))

    def read(self):
        self.bytes = bytes_int(self.data)


class Constant_Long_info(Constant_Base):
    high_bytes = 0  # u4
    low_bytes = 0  # u4

    def __init__(self):
        Constant_Base.__init__(self, 5, 9)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nhigh_bytes= {1} \r\nlow_bytes= {1} \r\ndata= {2} \r\n'.format(self.tag, self.high_bytes,
                                                                                          bytes_int(self.data)))

    def read(self):
        self.high_bytes = self.data[:4]
        self.low_bytes = self.data[4:]


class Constant_Double_info(Constant_Base):
    high_bytes = 0  # u4
    low_bytes = 0  # u4

    def __init__(self):
        Constant_Base.__init__(self, 6, 9)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nhigh_bytes= {1} \r\nlow_bytes= {1} \r\ndata= {2} \r\n'.format(self.tag, self.high_bytes,
                                                                                          self.low_bytes,
                                                                                          bytes_int(self.data)))

    def read(self):
        self.high_bytes = self.data[:4]
        self.low_bytes = self.data[4:]


class Constant_NameAndType_info(Constant_Base):
    name_index = 0  # u2
    descriptor_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 12, 5)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nname_index= {1} \r\ndescriptor_index= {2} \r\n'.format(self.tag, self.name_index,
                                                                                   self.descriptor_index))

    def read(self):
        self.name_index = bytes_int(self.data[:2])
        self.descriptor_index = bytes_int(self.data[2:])


class Constant_Utf8_info:
    tag = 1
    length = 0
    bytes = bytes()

    def __init__(self, len):
        self.length = len
        self.bytes = bytes(self.length)

    def print(self):
        print('{0} {1}'.format(self.bytes_hex(bytes([self.tag])), self.bytes_hex(self.bytes)))
        print('tag= {0} \r\nlength= {1} \r\nbytes= {2} \r\n'.format(self.tag, self.length,
                                                                    str(self.bytes, 'utf-8')))

    def bytes_hex(self, s):
        lin = ['%02X' % i for i in s]
        return " ".join(lin)


class Constant_MethodHandle_info(Constant_Base):
    reference_kind = 0  # u2
    reference_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 15, 5)

    def print(self):
        print('tag= {0} \r\nreference_kind= {1} \r\nreference_index= {2} \r\n'.format(self.tag, self.reference_kind,
                                                                                      self.reference_index))

    def read(self):
        self.reference_kind = self.data[:2]
        self.reference_index = self.data[2:]


class Constant_MethodType_info(Constant_Base):
    descriptor_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 16, 3)

    def print(self):
        print('tag= {0} \r\ndescriptor_index= {1} \r\n'.format(self.tag, self.descriptor_index))

    def read(self):
        self.descriptor_index = bytes_int(self.data)


class Constant_InvokeDynamic_info(Constant_Base):
    bootstrap_method_attr_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 18, 5)

    def print(self):
        print('tag= {0} \r\nbootstrap_method_attr_index= {1} \r\nname_and_type_index= {2} \r\n'.format(self.tag,
                                                                                                       self.bootstrap_method_attr_index,
                                                                                                       self.name_and_type_index))

    def read(self):
        self.bootstrap_method_attr_index = self.data[:2]
        self.name_and_type_index = self.data[2:]


header_indice = [4, 2, 2]
flag_indice = [2, 2, 2, 2]

# len_map = {7: 2, 9: 4, 10: 4, 11: 4, 8: 2, 3: 4, 4: 4, 5: 8, 6: 8, 12: 4}
class_map = {7: Constant_Class_info,
             9: Constant_Fieldref_info,
             10: Constant_Methodref_info,
             11: Constant_InterfaceMethodref_info,
             8: Constant_String_info,
             3: Constant_Integer_info,
             4: Constant_Float_info,
             5: Constant_Long_info,
             6: Constant_Double_info,
             12: Constant_NameAndType_info,
             15: Constant_MethodHandle_info,
             16: Constant_MethodType_info,
             18: Constant_InvokeDynamic_info}


def read_class(file_path):
    binfile = open(file_path, 'rb')
    size = os.path.getsize(file_path)
    constant_index = 1

    # 读取固定文件头
    for i in header_indice:
        data = binfile.read(i)
        print_bytes_hex(data)

    print()

    # 常量池大小
    constant_size_data = binfile.read(2)
    print_bytes_hex(constant_size_data)
    constant_size = bytes_int(constant_size_data)

    print('constant_size = %d' % constant_size)

    print()

    # 读取各个常量
    while constant_index < constant_size:
        data = binfile.read(1)
        tag = bytes_int(data)
        if tag in class_map:
            class_model = class_map.get(tag)
            instance = class_model()
            instance.data = binfile.read(instance.offset())
            instance.read()
            print('# {0}   {1} -->'.format(constant_index, instance.__class__.__name__))
            instance.print()
        else:
            len_data = binfile.read(2)
            len = bytes_int(len_data)
            instance = Constant_Utf8_info(len)
            instance.bytes = binfile.read(instance.length)
            print('# {0}   {1} -->'.format(constant_index, instance.__class__.__name__))
            instance.print()
        constant_index += 1

    access_flag_data = binfile.read(2)
    print_bytes_hex(access_flag_data)
    access_flag = bytes_int(access_flag_data)

    this_class_data = binfile.read(2)
    print_bytes_hex(this_class_data)
    this_class = bytes_int(this_class_data)

    super_class_data = binfile.read(2)
    print_bytes_hex(super_class_data)
    super_class = bytes_int(super_class_data)

    binfile.close()


def print_bytes_hex(data):
    lin = ['%02X' % i for i in data]
    print(" ".join(lin))

