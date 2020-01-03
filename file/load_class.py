# -*- coding: utf-8 -*-

import os
import sys

# class_file_path = sys.argv[1]
class_file_path = "Point.class"
# class_file_path = "ISortStrategy.class"
# class_file_path = "BubbleSort.class"


class Constant_Base:
    tag = bytes(1)     # u1
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


# 字段表
class Field_info():
    access_flags = 0  # u2
    name_index = 0  # u2
    descriptor_index = 0  # u2
    attributes_count = 0  # u2
    attributes = []

    head = bytes(8)
    content = bytes()

    def print(self):
        print('access_flags = {0}\r\nname_index = {1}\r\ndescriptor_index = {2}\r\nattributes_count = {3}\r\n'.format(
            self.access_flags, self.name_index, self.descriptor_index, self.attributes_count))

    def read(self):
        self.access_flags = bytes_hex(self.head[:2])
        self.name_index = bytes_int(self.head[2:4])
        self.descriptor_index = bytes_int(self.head[4:6])
        self.attributes_count = bytes_int(self.head[6:8])

# 方法表
class Method_info():
    access_flags = 0  # u2
    name_index = 0  # u2
    descriptor_index = 0  # u2
    attributes_count = 0  # u2
    attributes = []

    head = bytes(8)
    content = bytes()

    def print(self):
        print('access_flags = {0}\r\nname_index = {1}\r\ndescriptor_index = {2}\r\nattributes_count = {3}\r\n'.format(
            self.access_flags, self.name_index, self.descriptor_index, self.attributes_count))

    def read(self):
        self.access_flags = bytes_hex(self.head[:2])
        self.name_index = bytes_int(self.head[2:4])
        self.descriptor_index = bytes_int(self.head[4:6])
        self.attributes_count = bytes_int(self.head[6:8])

class Attribute_info():
    head = bytes(6)

    attribute_name_index = 0  # u2
    attribute_length = 0  # u4
    attribute_content = bytes()

    def read(self):
        self.attribute_name_index = bytes_int(self.head[:2])
        self.attribute_length = bytes_int(self.head[2:])
        self.attribute_content = bytes(self.attribute_length)

    def print(self):
        print('\tattribute_name_index = {0}\r\n\tattribute_length = {1}\r\n\tattribute_content = {2}\r\n'.format(
            self.attribute_name_index, self.attribute_length, bytes_hex(self.attribute_content)))


header_indice = [4, 2, 2]
flag_indice = [2, 2, 2, 2]

reference_map = {}
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
    class_file = open(file_path, 'rb')
    size = os.path.getsize(file_path)
    constant_index = 1

    # 读取固定文件头
    for i in header_indice:
        data = class_file.read(i)
        print(bytes_hex(data))

    print()

    # 常量池大小
    constant_size_data = class_file.read(2)
    print(bytes_hex(constant_size_data))
    constant_size = bytes_int(constant_size_data)

    print('constant_size = %d' % constant_size)

    print()

    # 读取各个常量
    while constant_index < constant_size:
        data = class_file.read(1)
        tag = bytes_int(data)
        if tag in class_map:
            class_model = class_map.get(tag)
            instance = class_model()
            instance.data = class_file.read(instance.offset())
            instance.read()
            print('# {0}   {1} -->'.format(constant_index, instance.__class__.__name__))
            instance.print()
        else:
            len_data = class_file.read(2)
            len = bytes_int(len_data)
            instance = Constant_Utf8_info(len)
            instance.bytes = class_file.read(instance.length)
            print('# {0}   {1} -->'.format(constant_index, instance.__class__.__name__))
            instance.print()
        constant_index += 1

    # 读取类的信息
    access_flag_data = class_file.read(2)
    print(bytes_hex(access_flag_data))
    print("access_flag:" + bytes_hex(access_flag_data))

    this_class_data = class_file.read(2)
    print(bytes_hex(this_class_data))
    this_class = bytes_int(this_class_data)
    print("this_class: %d" % this_class)

    super_class_data = class_file.read(2)
    print(bytes_hex(super_class_data))
    super_class = bytes_int(super_class_data)
    print("super_class: %d" % super_class)

    # 读取接口信息
    interface_count_data = class_file.read(2)
    print(bytes_hex(interface_count_data))
    interface_count = bytes_int(interface_count_data)
    print("interface_count: %d" % interface_count)

    interface_index = 0
    while interface_index < interface_count:
        interface_data = class_file.read(2)
        print(bytes_hex(interface_data))
        print("interface_index: %d " % bytes_int(interface_data))
        interface_index += 1

    # 字段
    field_count_data = class_file.read(2)
    print(bytes_hex(field_count_data))
    field_count = bytes_int(field_count_data)
    print("field_count: %d" % field_count)
    print()

    field_index = 0
    while field_index < field_count:
        field_info = Field_info()
        field_info.head = class_file.read(8)
        field_info.read()
        print("Field # {0}  {1} -->".format(field_index,field_info.__class__.__name__))
        field_info.print()
        attribute_index = 0
        while attribute_index < field_info.attributes_count:
            attribute_info = Attribute_info()
            attribute_info.head = class_file.read(6)
            attribute_info.read()
            attribute_info.attribute_content = class_file.read(attribute_info.attribute_length)
            print("\tAttr # {0} {1} -->".format(attribute_index, attribute_info.__class__.__name__))
            attribute_info.print()
            attribute_index += 1
        field_index += 1

    # 方法
    method_count_data = class_file.read(2)
    print(bytes_hex(method_count_data))
    method_count = bytes_int(method_count_data)
    print("method_count: %d" % method_count)
    print()

    method_index = 0
    while method_index < method_count:
        method_info = Method_info()
        method_info.head = class_file.read(8)
        method_info.read()
        print("Method # {0}  {1} -->".format(method_index, method_info.__class__.__name__))
        method_info.print()
        attribute_index = 0
        while attribute_index < method_info.attributes_count:
            attribute_info = Attribute_info()
            attribute_info.head = class_file.read(6)
            attribute_info.read()
            attribute_info.attribute_content = class_file.read(attribute_info.attribute_length)
            print("\tAttr # {0} {1} -->".format(attribute_index, attribute_info.__class__.__name__))
            attribute_info.print()
            attribute_index += 1
        method_index += 1

    # 属性
    attr_count_data = class_file.read(2)
    print(bytes_hex(attr_count_data))
    attr_count = bytes_int(attr_count_data)
    print("attr_count: %d" % attr_count)
    print()

    attribute_index = 0
    while attribute_index < attr_count:
        attribute_info = Attribute_info()
        attribute_info.head = class_file.read(6)
        attribute_info.read()
        attribute_info.attribute_content = class_file.read(attribute_info.attribute_length)
        print("\tAttr # {0} {1} -->".format(attribute_index, attribute_info.__class__.__name__))
        attribute_info.print()
        attribute_index += 1

    class_file.close()


def bytes_hex(data):
    lin = ['%02X' % i for i in data]
    return " ".join(lin)


def bytes_int(data):
    return int().from_bytes(data, byteorder='big', signed=True)


read_class(class_file_path)
