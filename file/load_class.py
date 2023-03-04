# -*- coding: utf-8 -*-

import os
import sys
import struct


class Constant_Base:
    tag = 0
    length = 0
    head = bytes(1)
    data = bytes()
    constant_map = {}

    def __init__(self, tag, length):
        self.tag = tag
        self.length = length
        self.data = bytes(self.offset())

    def len(self):
        return self.length

    def offset(self):
        return self.length - 1

    def space(self):
        return 1

    def print(self):
        print('{0} {1}'.format(bytes_hex(bytes([self.tag])), bytes_hex(self.data)))

    def to_string(self):
        return 'Base'


# UTF-8编码的字符串
class Constant_Utf8_info:
    tag = 1
    length = 0
    head = bytes()
    len_byte = bytes()
    bytes = bytes()

    def __init__(self, len):
        self.length = len
        self.bytes = bytes(self.length)

    def print(self):
        print('{0} {1} {2}'.format(self.bytes_hex(bytes([self.tag])), self.bytes_hex(self.len_byte),
                                   self.bytes_hex(self.bytes)))
        print('{0} \t\ttag= {1}'.format(self.bytes_hex(self.head), self.tag))
        print('{0} \tlength= {1}'.format(self.bytes_hex(self.len_byte), self.length))
        print('str= {0}'.format(self.to_string()))
        print()

    def space(self):
        return 1

    def to_string(self):
        return str(self.bytes, 'utf-8')

    def bytes_hex(self, s):
        lin = ['%02X' % i for i in s]
        return " ".join(lin)


# 字符串类型字面量
class Constant_String_info(Constant_Base):
    string_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 8, 3)

    def print(self):
        Constant_Base.print(self)
        print('tag= {0} \r\nstring_index= {1} \r\n'.format(self.tag, self.string_index))

    def read(self):
        self.name_index = bytes_int(self.data)

    def to_string(self):
        return Constant_Base.constant_map[self.string_index].to_string()


# 整型字面量
class Constant_Integer_info(Constant_Base):
    bytes = bytes()  # u4
    value = 0

    def __init__(self):
        Constant_Base.__init__(self, 3, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\t\t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tvalue= {1}'.format(bytes_hex(self.bytes), self.value))

    def read(self):
        self.bytes = self.data
        self.value = bytes_int(self.bytes)

    def to_string(self):
        return str(self.value)


# 浮点型字面量
class Constant_Float_info(Constant_Base):
    bytes = bytes()  # u4
    value = 0

    def __init__(self):
        Constant_Base.__init__(self, 4, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\t\t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tvalue= {1}'.format(bytes_hex(self.data), self.value))

    def read(self):
        self.bytes = self.data
        self.value = round(struct.unpack('!f', bytes.fromhex(bytes_hex(self.bytes)))[0], 6)

    def to_string(self):
        return str(self.value)


# 长整型字面量
class Constant_Long_info(Constant_Base):
    high_bytes = bytes()  # u4
    low_bytes = bytes()  # u4
    value = 0

    def __init__(self):
        Constant_Base.__init__(self, 5, 9)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\t\t\t\t\t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tvalue= {1}'.format(bytes_hex(self.data), self.value))

    def read(self):
        self.high_bytes = self.data[:4]
        self.low_bytes = self.data[4:]
        self.value = bytes_int(self.data)

    def space(self):
        return 2

    def to_string(self):
        return str(self.value)


# 双精度浮点型字面量
class Constant_Double_info(Constant_Base):
    high_bytes = bytes()  # u4
    low_bytes = bytes()  # u4
    value = 0

    def __init__(self):
        Constant_Base.__init__(self, 6, 9)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\t\t\t\t\t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tvalue= {1}'.format(bytes_hex(self.data), self.value))

    def read(self):
        self.high_bytes = self.data[:4]
        self.low_bytes = self.data[4:]
        self.value = round(struct.unpack('!f', bytes.fromhex(bytes_hex(self.data)))[0], 6)

    def space(self):
        return 2

    def to_string(self):
        return str(self.value)


# 类或接口的符号引用
class Constant_Class_info(Constant_Base):
    name_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 7, 3)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tname_index= {1}'.format(bytes_hex(self.data), self.name_index))
        print()

    def read(self):
        self.name_index = bytes_int(self.data)

    def to_string(self):
        return Constant_Base.constant_map[self.name_index].to_string()


# 字段的符号引用
class Constant_Fieldref_info(Constant_Base):
    class_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 9, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tclass_index= {1}'.format(bytes_hex(self.data[:2]), self.class_index))
        print('{0} \tname_and_type_index= {1}'.format(bytes_hex(self.data[2:]),
                                                      self.name_and_type_index))
        print()

    def read(self):
        self.class_index = bytes_int(self.data[:2])
        self.name_and_type_index = bytes_int(self.data[2:])

    def to_string(self):
        return Constant_Base.constant_map[self.class_index].to_string() + "\r\n" + Constant_Base.constant_map[
            self.name_and_type_index].to_string()


# 类中方法的符号引用
class Constant_Methodref_info(Constant_Base):
    class_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 10, 5)

    def ref(self):
        ref_class = Constant_Class_info()

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tclass_index= {1}'.format(bytes_hex(self.data[:2]), self.class_index))
        print('{0} \tname_and_type_index= {1}'.format(bytes_hex(self.data[2:]),
                                                      self.name_and_type_index))
        print()

    def read(self):
        self.class_index = bytes_int(self.data[:2])
        self.name_and_type_index = bytes_int(self.data[2:])

    def to_string(self):
        return Constant_Base.constant_map[self.class_index].to_string() + "\r\n" + Constant_Base.constant_map[
            self.name_and_type_index].to_string()


# 接口中方法的符号引用
class Constant_InterfaceMethodref_info(Constant_Base):
    class_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 11, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tclass_index= {1}'.format(bytes_hex(self.data[:2]), self.class_index))
        print('{0} \tname_and_type_index= {1}'.format(bytes_hex(self.data[2:]),
                                                      self.name_and_type_index))
        print()

    def read(self):
        self.class_index = bytes_int(self.data[:2])
        self.name_and_type_index = bytes_int(self.data[2:])

    def to_string(self):
        return Constant_Base.constant_map[self.class_index].to_string() + "\r\n" + Constant_Base.constant_map[
            self.name_and_type_index].to_string()


# 字段或方法的部分符号引用
class Constant_NameAndType_info(Constant_Base):
    name_index = 0  # u2
    descriptor_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 12, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tname_index= {1}'.format(bytes_hex(self.data[:2]), self.name_index))
        print('{0} \tdescriptor_index= {1}'.format(bytes_hex(self.data[2:]),
                                                   self.descriptor_index))
        print()

    def read(self):
        self.name_index = bytes_int(self.data[:2])
        self.descriptor_index = bytes_int(self.data[2:])

    def to_string(self):
        return Constant_Base.constant_map[self.name_index].to_string() + ";" + Constant_Base.constant_map[
            self.descriptor_index].to_string()


# 表示方法句柄
class Constant_MethodHandle_info(Constant_Base):
    reference_kind = 0  # u2
    reference_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 15, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \treference_kind= {1}'.format(bytes_hex(self.data[:2]), self.reference_kind))
        print('{0} \treference_index= {1}'.format(bytes_hex(self.data[2:]),
                                                  self.reference_index))
        print()

    def read(self):
        self.reference_kind = self.data[:2]
        self.reference_index = self.data[2:]

    def to_string(self):
        return Constant_Base.constant_map[self.reference_kind].to_string() + ";" + Constant_Base.constant_map[
            self.reference_index].to_string()


# 标识方法类型
class Constant_MethodType_info(Constant_Base):
    descriptor_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 16, 3)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tdescriptor_index= {1}'.format(bytes_hex(self.data), self.descriptor_index))
        print()

    def read(self):
        self.descriptor_index = bytes_int(self.data)

    def to_string(self):
        return Constant_Base.constant_map[self.descriptor_index].to_string()


# 表示一个动态方法调用点
class Constant_InvokeDynamic_info(Constant_Base):
    bootstrap_method_attr_index = 0  # u2
    name_and_type_index = 0  # u2

    def __init__(self):
        Constant_Base.__init__(self, 18, 5)

    def print(self):
        Constant_Base.print(self)
        print('{0} \t\ttag= {1}'.format(bytes_hex(Constant_Base.head), self.tag))
        print('{0} \tbootstrap_method_attr_index= {1}'.format(bytes_hex(self.data[:2]),
                                                              self.bootstrap_method_attr_index))
        print('{0} \tname_and_type_index= {1}'.format(bytes_hex(self.data[2:]),
                                                      self.name_and_type_index))
        print()

    def read(self):
        self.bootstrap_method_attr_index = self.data[:2]
        self.name_and_type_index = self.data[2:]

    def to_string(self):
        return Constant_Base.constant_map[self.bootstrap_method_attr_index].to_string() + ";" + \
               Constant_Base.constant_map[
                   self.name_and_type_index].to_string()


class Table_base:
    length = 0
    head = bytes()
    data = bytes()

    def head_len(self):
        return 0

    def print(self):
        print('{0} {1}'.format(bytes_hex(self.head), bytes_hex(self.data)))


# 字段表
class Field_info(Table_base):
    bytes_access_flags = bytes(2)
    bytes_name_index = bytes(2)
    bytes_descriptor_index = bytes(2)
    bytes_attributes_count = bytes(2)
    attributes_info = bytes()

    access_flags = 0
    name_index = 0
    descriptor_index = 0
    attributes_count = 0
    attributes = []

    def head_len(self):
        return 8

    def read(self):
        self.bytes_access_flags = self.head[:2]
        self.bytes_name_index = self.head[2:4]
        self.bytes_descriptor_index = self.head[4:6]
        self.bytes_attributes_count = self.head[6:8]
        self.access_flags = bytes_int(self.bytes_access_flags)
        self.name_index = bytes_int(self.bytes_name_index)
        self.descriptor_index = bytes_int(self.bytes_descriptor_index)
        self.attributes_count = bytes_int(self.bytes_attributes_count)

    def print(self):
        print("{0}".format(bytes_hex(self.head)))
        print("{0} \taccess_flags= {1}".format(bytes_hex(self.bytes_access_flags), self.access_flags))
        print("{0} \tname_index= {1}".format(bytes_hex(self.bytes_name_index), self.name_index))
        print("{0} \tdescriptor_index= {1}".format(bytes_hex(self.bytes_descriptor_index), self.descriptor_index))
        print("{0} \tattributes_count= {1}".format(bytes_hex(self.bytes_attributes_count), self.attributes_count))

    def to_string(self):
        return str(access_flags_string(self.access_flags, 2)) + "\r\n" + Constant_Base.constant_map[
            self.name_index].to_string() + "\r\n" + Constant_Base.constant_map[self.descriptor_index].to_string()


# 方法表
class Method_info(Table_base):
    bytes_access_flags = bytes(2)
    bytes_name_index = bytes(2)
    bytes_descriptor_index = bytes(2)
    bytes_attributes_count = bytes(2)
    attributes_info = bytes()

    access_flags = 0
    name_index = 0
    descriptor_index = 0
    attributes_count = 0
    attributes = []

    def head_len(self):
        return 8

    def read(self):
        self.bytes_access_flags = self.head[:2]
        self.bytes_name_index = self.head[2:4]
        self.bytes_descriptor_index = self.head[4:6]
        self.bytes_attributes_count = self.head[6:8]
        self.access_flags = bytes_int(self.bytes_access_flags)
        self.name_index = bytes_int(self.bytes_name_index)
        self.descriptor_index = bytes_int(self.bytes_descriptor_index)
        self.attributes_count = bytes_int(self.bytes_attributes_count)

    def print(self):
        print("{0}".format(bytes_hex(self.head)))
        print("{0} \taccess_flags= {1}".format(bytes_hex(self.bytes_access_flags), self.access_flags))
        print("{0} \tname_index= {1}".format(bytes_hex(self.bytes_name_index), self.name_index))
        print("{0} \tdescriptor_index= {1}".format(bytes_hex(self.bytes_descriptor_index), self.descriptor_index))
        print("{0} \tattributes_count= {1}".format(bytes_hex(self.bytes_attributes_count), self.attributes_count))

    def to_string(self):
        return str(access_flags_string(self.access_flags, 3)) + "\r\n" + Constant_Base.constant_map[
            self.name_index].to_string() + "\r\n" + Constant_Base.constant_map[self.descriptor_index].to_string()


# 属性表
class Attribute_info(Table_base):
    bytes_attribute_name_index = bytes(2)
    bytes_attribute_length = bytes(4)

    attribute_name_index = 0
    attribute_length = 0

    def head_len(self):
        return 6

    def read(self):
        self.bytes_attribute_name_index = self.head[:2]
        self.bytes_attribute_length = self.head[2:]
        self.attribute_name_index = bytes_int(self.bytes_attribute_name_index)
        self.attribute_length = bytes_int(self.bytes_attribute_length)

    def print(self):
        # print("{0} {1}".format(bytes_hex(self.head),bytes_hex(self.data)))
        print("{0}".format(self.class_name()))

    def class_name(self):
        return Constant_Base.constant_map[self.attribute_name_index].to_string()


class Attribute_Constant_Value(Attribute_info):
    bytes_constant_value_index = bytes(2)
    constant_value_index = 0

    def read(self):
        self.bytes_constant_value_index = self.data
        self.constant_value_index = bytes_int(self.bytes_constant_value_index)

    def print(self):
        print("{0} {1}".format(bytes_hex(self.head),bytes_hex(self.data)))
        print("{0} \t\t\tattribute_name_index= {1}".format(bytes_hex(self.bytes_attribute_name_index), self.attribute_name_index))
        print("{0} \tattribute_length= {1}".format(bytes_hex(self.bytes_attribute_length), self.attribute_length))
        print("{0} \t\t\tconstant_value_index= {1}".format(bytes_hex(self.bytes_constant_value_index), self.constant_value_index))
        print("{0}".format(Constant_Base.constant_map[self.constant_value_index].to_string()))


class Attribute_Code(Attribute_info):
    bytes_max_stack = bytes(2)
    bytes_max_locals = bytes(2)
    bytes_code_length = bytes(4)
    bytes_code = bytes()
    bytes_exception_table_length = bytes(2)
    bytes_exception_table = bytes()
    bytes_attributes_count = bytes(2)
    bytes_attributes_info = bytes()

    max_stack = 0
    max_locals = 0
    code_length = 0
    exception_table_length = 0
    attributes_count = 0

    def read(self):
        self.bytes_max_stack = self.data[:2]
        self.bytes_max_locals = self.data[2:4]
        self.bytes_code_length = self.data[4:8]

        self.max_stack = bytes_int(self.bytes_max_stack)
        self.max_locals = bytes_int(self.bytes_max_locals)
        self.code_length = bytes_int(self.bytes_code_length)

        code_end_index = 8+self.code_length
        self.bytes_code = self.data[8:code_end_index]

        self.bytes_exception_table_length = self.data[code_end_index:code_end_index+2]
        self.exception_table_length = bytes_int(self.bytes_exception_table_length)

        exception_end_index = code_end_index+2+8*self.exception_table_length
        self.bytes_exception_table = self.data[code_end_index+2:exception_end_index]

        self.bytes_attributes_count = self.data[exception_end_index:exception_end_index+2]
        self.attributes_count = bytes_int(self.bytes_attributes_count)

    def print(self):
        print("{0} {1}".format(bytes_hex(self.head),bytes_hex(self.data)))
        print("{0} \t\t\tattribute_name_index= {1}".format(bytes_hex(self.bytes_attribute_name_index), self.attribute_name_index))
        print("{0} \tattribute_length= {1}".format(bytes_hex(self.bytes_attribute_length), self.attribute_length))
        print("{0} \t\t\tmax_stack= {1}".format(bytes_hex(self.bytes_max_stack), self.max_stack))
        print("{0} \t\t\tmax_locals= {1}".format(bytes_hex(self.bytes_max_locals), self.max_locals))
        print("{0} \tcode_length= {1}".format(bytes_hex(self.bytes_code_length), self.code_length))
        print("code: \t\t\t{0}".format(bytes_hex(self.bytes_code)))
        print("{0} \t\t\texception_table_length= {1}".format(bytes_hex(self.bytes_exception_table_length), self.exception_table_length))
        print("{0} \t\t\tattributes_count= {1}".format(bytes_hex(self.bytes_attributes_count), self.attributes_count))


class Attribute_Exceptions(Attribute_info):
    bytes_number_of_exceptions = bytes(2)
    bytes_exception_index_table = bytes()

    number_of_exceptions = 0
    exception_index_table = []

    def read(self):
        self.bytes_number_of_exceptions = self.data[:2]
        self.bytes_exception_index_table = self.data[2:]
        self.number_of_exceptions = bytes_int(self.bytes_number_of_exceptions)

        index = 0
        while index < self.number_of_exceptions:
            exception_index = bytes_int(self.bytes_exception_index_table[index*2:(index+1)*2])
            self.exception_index_table.append(exception_index)
            index = index+1

    def print(self):
        print("{0} {1}".format(bytes_hex(self.head),bytes_hex(self.data)))
        print("{0} \t\t\tattribute_name_index= {1}".format(bytes_hex(self.bytes_attribute_name_index), self.attribute_name_index))
        print("{0} \tattribute_length= {1}".format(bytes_hex(self.bytes_attribute_length), self.attribute_length))
        print("{0} \t\t\tnumber_of_exceptions= {1}".format(bytes_hex(self.bytes_number_of_exceptions), self.number_of_exceptions))
        for index in self.exception_index_table:
            print("exception: \t\t{0}".format(Constant_Base.constant_map[index].to_string()))


class Attribute_SourceFile(Attribute_info):
    bytes_sourcefile_index = bytes(2)
    sourcefile_index = 0

    def read(self):
        self.bytes_sourcefile_index = self.data
        self.sourcefile_index = bytes_int(self.bytes_sourcefile_index)

    def print(self):
        print("{0} {1}".format(bytes_hex(self.head),bytes_hex(self.data)))
        print("{0} \t\t\tattribute_name_index= {1}".format(bytes_hex(self.bytes_attribute_name_index), self.attribute_name_index))
        print("{0} \tattribute_length= {1}".format(bytes_hex(self.bytes_attribute_length), self.attribute_length))
        print("{0} \t\t\tsourcefile_index= {1}".format(bytes_hex(self.bytes_sourcefile_index), self.sourcefile_index))
        print("{0}".format(Constant_Base.constant_map[self.sourcefile_index].to_string()))


def print_bytes_hex(data):
    lin = ['%02X' % i for i in data]
    print(" ".join(lin))


def bytes_int(data):
    return int().from_bytes(data, byteorder='big', signed=True)


def bytes_hex(s):
    lin = ['%02X' % i for i in s]
    return " ".join(lin)


def access_flags_string(flags,select):
    flags_map = {}
    if select == 1:
        flags_map = access_class_map
    elif select == 2:
        flags_map = access_field_map
    elif select == 3:
        flags_map = access_method_map

    flags_str = []
    for k, v in flags_map.items():
        result = k & flags
        if result != 0:
            flags_str.append(v)
    return flags_str


# 魔数4字节，次版本号2字节，主版本号2字节
header_indice = [4, 2, 2]
# 访问标志、类索引、父类索引、接口索引数量
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

attribute_class_map = {
    "ConstantValue": Attribute_Constant_Value,
    "Code": Attribute_Code,
    "SourceFile": Attribute_SourceFile,
    "Exceptions": Attribute_Exceptions
}

access_class_map = {
    0x0001: "ACC_PUBLIC",       # 0000 0000 0000 0001
    0x0010: "ACC_FINAL",        # 0000 0000 0001 0000
    0x0020: "ACC_SUPER",        # 0000 0000 0010 0000
    0x0200: "ACC_INTERFACE",    # 0000 0010 0000 0000
    0x0400: "ACC_ABSTRACT",     # 0000 0100 0000 0000
    0x1000: "ACC_SYNTHETIC",    # 0001 0000 0000 0000
    0x2000: "ACC_ANNOTATION",   # 0010 0000 0000 0000
    0x4000: "ACC_ENUM",         # 0100 0000 0000 0000
}

access_field_map = {
    0x0001: "ACC_PUBLIC",       # 0000 0000 0000 0001
    0x0002: "ACC_PRIVATE",      # 0000 0000 0000 0010
    0x0004: "ACC_PROTECT",      # 0000 0000 0000 0100
    0x0008: "ACC_STATIC",       # 0000 0000 0000 1000
    0x0010: "ACC_FINAL",        # 0000 0000 0001 0000
    0x0040: "ACC_VOLATILE",     # 0000 0000 0100 0000
    0x0080: "ACC_TRANSIENT",    # 0000 0000 1000 0000
    0x1000: "ACC_SYNTHETIC",    # 0001 0000 0000 0000
    0x4000: "ACC_ENUM",         # 0100 0000 0000 0000
}

access_method_map = {
    0x0001: "ACC_PUBLIC",       # 0000 0000 0000 0001
    0x0002: "ACC_PRIVATE",      # 0000 0000 0000 0010
    0x0004: "ACC_PROTECT",      # 0000 0000 0000 0100
    0x0008: "ACC_STATIC",       # 0000 0000 0000 1000
    0x0010: "ACC_FINAL",        # 0000 0000 0001 0000
    0x0020: "ACC_SYNCHRONIZED", # 0000 0000 0010 0000
    0x0040: "ACC_BRIDGE",       # 0000 0000 0100 0000
    0x0080: "ACC_VARARGS",      # 0000 0000 1000 0000
    0x0100: "ACC_NATIVE",       # 0000 0001 0000 0000
    0x0400: "ACC_ABSTRACT",     # 0000 0100 0000 0000
    0x0800: "ACC_STRICT",       # 0000 1000 0000 0000
    0x1000: "ACC_SYNTHETIC",    # 0001 0000 0000 0000
}

def read_class(file_path):
    binfile = open(file_path, 'rb')
    size = os.path.getsize(file_path)
    constant_index = 1

    # 读取固定文件头，魔数与版本号
    for i in header_indice:
        head = binfile.read(i)
        print_bytes_hex(head)

    print()

    # 常量池大小
    constant_size_data = binfile.read(2)
    print_bytes_hex(constant_size_data)
    constant_size = bytes_int(constant_size_data)

    print('constant_size = %d' % constant_size)

    print()

    # 读取各个常量
    while constant_index < constant_size:
        head = binfile.read(1)
        tag = bytes_int(head)

        if tag in class_map:
            class_model = class_map.get(tag)
            instance_field = class_model()
            instance_field.head = head
            instance_field.data = binfile.read(instance_field.offset())
            instance_field.read()
            # print('# {0}   {1} -->'.format(constant_index, instance.__class__.__name__))
            # instance.print()
            Constant_Base.constant_map[constant_index] = instance_field
            constant_index += instance_field.space()
        elif tag == 1:
            len_byte = binfile.read(2)
            len = bytes_int(len_byte)
            instance_field = Constant_Utf8_info(len)
            instance_field.head = head
            instance_field.len_byte = len_byte
            instance_field.bytes = binfile.read(instance_field.length)
            # print('# {0}   {1} -->'.format(constant_index, instance.__class__.__name__))
            # instance.print()
            Constant_Base.constant_map[constant_index] = instance_field
            constant_index += instance_field.space()

    for index, instance_field in Constant_Base.constant_map.items():
        print('# {0}   {1} -->'.format(index, instance_field.__class__.__name__))
        instance_field.print()
        print(instance_field.to_string())
        print()
        print("-" * 36)

    # 读取类的访问标志
    access_flag_data = binfile.read(2)
    print_bytes_hex(access_flag_data)
    access_flag = bytes_int(access_flag_data)
    print(access_flags_string(access_flag,1))
    print("-" * 36)

    # 读取类索引
    this_class_data = binfile.read(2)
    print_bytes_hex(this_class_data)
    index_this_class = bytes_int(this_class_data)
    print(Constant_Base.constant_map[index_this_class].to_string())
    print("-" * 36)

    # 读取父类索引
    super_class_data = binfile.read(2)
    print_bytes_hex(super_class_data)
    index_super_class = bytes_int(super_class_data)
    print(Constant_Base.constant_map[index_super_class].to_string())
    print("-" * 36)

    # 读取接口数量及接口索引
    interfaces_count_data = binfile.read(2)
    print_bytes_hex(interfaces_count_data)
    interfaces_count = bytes_int(interfaces_count_data)
    print('interfaces count = {0}\r\n'.format(interfaces_count))
    interfaces_index = 0
    while interfaces_index < interfaces_count:
        interface_index_data = binfile.read(2)
        print_bytes_hex(interface_index_data)
        index_interface = bytes_int(interface_index_data)
        print(Constant_Base.constant_map[index_interface].to_string())
        interfaces_index = interfaces_index+1
    print("-" * 36)

    # 读取字段表
    fields_count_data = binfile.read(2)
    print_bytes_hex(fields_count_data)
    fields_count = bytes_int(fields_count_data)
    print('fields count = {0}\r\n'.format(fields_count))

    read_field(fields_count, binfile)
    print("-" * 36)

    # 读取方法表
    method_count_data = binfile.read(2)
    print_bytes_hex(method_count_data)
    methods_count = bytes_int(method_count_data)
    print('methods count = {0}\r\n'.format(methods_count))

    read_method(methods_count, binfile)
    print("-" * 36)

    # 读取属性表
    attribute_count_data = binfile.read(2)
    print_bytes_hex(attribute_count_data)
    attributes_count = bytes_int(attribute_count_data)
    print('attributes count = {0}\r\n'.format(attributes_count))

    read_attribute(attributes_count, binfile)
    print("-" * 36)

    binfile.close()


def read_field(count, binfile):
    fields_index = 0
    while fields_index < count:
        print("# {0} Field info".format(fields_index))
        instance_field = Field_info()
        instance_field.head = binfile.read(instance_field.head_len())
        instance_field.read()
        instance_field.print()
        print(instance_field.to_string())
        read_attribute(instance_field.attributes_count, binfile)
        print()
        fields_index = fields_index+1


def read_method(count, binfile):
    methods_index = 0
    while methods_index < count:
        print("# {0} Method info".format(methods_index))
        instance_method = Method_info()
        instance_method.head = binfile.read(instance_method.head_len())
        instance_method.read()
        instance_method.print()
        print(instance_method.to_string())
        read_attribute(instance_method.attributes_count, binfile)
        print()
        methods_index = methods_index+1


def read_attribute(count, binfile):
    print("\r\nAttribute List\r\n")
    index = 0
    while index < count:
        instance_attr = Attribute_info()
        instance_attr.head = binfile.read(instance_attr.head_len())
        instance_attr.read()
        instance_attr.data = binfile.read(instance_attr.attribute_length)
        # instance_attr.print()
        class_model = attribute_class_map[instance_attr.class_name()]
        instance_attr_s = class_model()
        # print(type(instance_attr_s))
        instance_attr_s.__dict__.update(instance_attr.__dict__)
        instance_attr.print()
        instance_attr_s.read()
        instance_attr_s.print()
        print()
        index = index+1


read_class(
    'E:\studying\StudioProjects\TechBasis\out\production\TechBasis\com\\xter\\algorithm\other\BinarySeachI.class')
# classfile = sys.argv[1]
# print("源文件路径为:" + classfile)
# read_class(classfile)
