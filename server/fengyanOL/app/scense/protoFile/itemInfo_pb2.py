# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/itemInfo.proto',
  package='protoFile',
  serialized_pb='\n\x18protoFile/itemInfo.proto\x12\tprotoFile\"\xf1\x04\n\tItemsInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nprefixNmae\x18\x02 \x01(\t\x12\x12\n\nsuffixName\x18\x03 \x01(\t\x12\x0f\n\x07isBound\x18\x04 \x01(\x05\x12\x11\n\textAttack\x18\x05 \x01(\x05\x12\x0e\n\x06\x65xtStr\x18\x06 \x01(\x05\x12\x0e\n\x06\x65xtVit\x18\x07 \x01(\x05\x12\x0e\n\x06\x65xtDex\x18\x08 \x01(\x05\x12\x0e\n\x06\x65xtWis\x18\t \x01(\x05\x12\x19\n\x11\x65xtPhysicalAttack\x18\n \x01(\x05\x12\x16\n\x0e\x65xtMagicAttack\x18\x0b \x01(\x05\x12\x1a\n\x12\x65xtPhysicalDefense\x18\x0c \x01(\x05\x12\x17\n\x0f\x65xtMagicDefense\x18\r \x01(\x05\x12\x17\n\x0f\x65xtHpAdditional\x18\x0e \x01(\x05\x12\x17\n\x0f\x65xtMpAdditional\x18\x0f \x01(\x05\x12\x18\n\x10\x65xtHitAdditional\x18\x10 \x01(\x05\x12\x19\n\x11\x65xtCritAdditional\x18\x11 \x01(\x05\x12\x1a\n\x12\x65xtBlockAdditional\x18\x12 \x01(\x05\x12\x1a\n\x12\x65xtDodgeAdditional\x18\x13 \x01(\x05\x12\x1a\n\x12\x65xtSpeedAdditional\x18\x14 \x01(\x05\x12\x16\n\x0e\x62uyingRateCoin\x18\x15 \x01(\x05\x12\x12\n\nextDefense\x18\x16 \x01(\x05\x12\r\n\x05stack\x18\x17 \x01(\x05\x12\x11\n\tstarLevel\x18\x18 \x01(\x05\x12\x12\n\ntemplateId\x18\x19 \x01(\x05\x12\"\n\x06xqInfo\x18\x1a \x01(\x0b\x32\x12.protoFile.XQ_Info\x12#\n\tsuiteInfo\x18\x1b \x01(\x0b\x32\x10.protoFile.Suite\"\x95\x01\n\x07XQ_Info\x12\x11\n\txqItemId1\x18\x01 \x01(\x05\x12\x0e\n\x06xqDes1\x18\x02 \x01(\t\x12\x11\n\txqItemId2\x18\x03 \x01(\x05\x12\x0e\n\x06xqDes2\x18\x04 \x01(\t\x12\x11\n\txqItemId3\x18\x05 \x01(\x05\x12\x0e\n\x06xqDes3\x18\x06 \x01(\t\x12\x11\n\txqItemId4\x18\x07 \x01(\x05\x12\x0e\n\x06xqDes4\x18\x08 \x01(\t\"e\n\x05Suite\x12\x11\n\tsuitename\x18\x01 \x01(\t\x12\x0e\n\x06nowcnt\x18\x02 \x01(\x05\x12\x0e\n\x06maxcnt\x18\x03 \x01(\x05\x12)\n\nsuiteeffct\x18\x04 \x03(\x0b\x32\x15.protoFile.SuiteEffec\"/\n\nSuiteEffec\x12\x11\n\teffectstr\x18\x01 \x01(\t\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08')




_ITEMSINFO = descriptor.Descriptor(
  name='ItemsInfo',
  full_name='protoFile.ItemsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.ItemsInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='prefixNmae', full_name='protoFile.ItemsInfo.prefixNmae', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suffixName', full_name='protoFile.ItemsInfo.suffixName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isBound', full_name='protoFile.ItemsInfo.isBound', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extAttack', full_name='protoFile.ItemsInfo.extAttack', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extStr', full_name='protoFile.ItemsInfo.extStr', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extVit', full_name='protoFile.ItemsInfo.extVit', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extDex', full_name='protoFile.ItemsInfo.extDex', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extWis', full_name='protoFile.ItemsInfo.extWis', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extPhysicalAttack', full_name='protoFile.ItemsInfo.extPhysicalAttack', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extMagicAttack', full_name='protoFile.ItemsInfo.extMagicAttack', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extPhysicalDefense', full_name='protoFile.ItemsInfo.extPhysicalDefense', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extMagicDefense', full_name='protoFile.ItemsInfo.extMagicDefense', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extHpAdditional', full_name='protoFile.ItemsInfo.extHpAdditional', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extMpAdditional', full_name='protoFile.ItemsInfo.extMpAdditional', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extHitAdditional', full_name='protoFile.ItemsInfo.extHitAdditional', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extCritAdditional', full_name='protoFile.ItemsInfo.extCritAdditional', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extBlockAdditional', full_name='protoFile.ItemsInfo.extBlockAdditional', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extDodgeAdditional', full_name='protoFile.ItemsInfo.extDodgeAdditional', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extSpeedAdditional', full_name='protoFile.ItemsInfo.extSpeedAdditional', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buyingRateCoin', full_name='protoFile.ItemsInfo.buyingRateCoin', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extDefense', full_name='protoFile.ItemsInfo.extDefense', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stack', full_name='protoFile.ItemsInfo.stack', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='starLevel', full_name='protoFile.ItemsInfo.starLevel', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='templateId', full_name='protoFile.ItemsInfo.templateId', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqInfo', full_name='protoFile.ItemsInfo.xqInfo', index=25,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suiteInfo', full_name='protoFile.ItemsInfo.suiteInfo', index=26,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=40,
  serialized_end=665,
)


_XQ_INFO = descriptor.Descriptor(
  name='XQ_Info',
  full_name='protoFile.XQ_Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='xqItemId1', full_name='protoFile.XQ_Info.xqItemId1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqDes1', full_name='protoFile.XQ_Info.xqDes1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqItemId2', full_name='protoFile.XQ_Info.xqItemId2', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqDes2', full_name='protoFile.XQ_Info.xqDes2', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqItemId3', full_name='protoFile.XQ_Info.xqItemId3', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqDes3', full_name='protoFile.XQ_Info.xqDes3', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqItemId4', full_name='protoFile.XQ_Info.xqItemId4', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='xqDes4', full_name='protoFile.XQ_Info.xqDes4', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=668,
  serialized_end=817,
)


_SUITE = descriptor.Descriptor(
  name='Suite',
  full_name='protoFile.Suite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='suitename', full_name='protoFile.Suite.suitename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nowcnt', full_name='protoFile.Suite.nowcnt', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxcnt', full_name='protoFile.Suite.maxcnt', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suiteeffct', full_name='protoFile.Suite.suiteeffct', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=819,
  serialized_end=920,
)


_SUITEEFFEC = descriptor.Descriptor(
  name='SuiteEffec',
  full_name='protoFile.SuiteEffec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='effectstr', full_name='protoFile.SuiteEffec.effectstr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enable', full_name='protoFile.SuiteEffec.enable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=922,
  serialized_end=969,
)

_ITEMSINFO.fields_by_name['xqInfo'].message_type = _XQ_INFO
_ITEMSINFO.fields_by_name['suiteInfo'].message_type = _SUITE
_SUITE.fields_by_name['suiteeffct'].message_type = _SUITEEFFEC
DESCRIPTOR.message_types_by_name['ItemsInfo'] = _ITEMSINFO
DESCRIPTOR.message_types_by_name['XQ_Info'] = _XQ_INFO
DESCRIPTOR.message_types_by_name['Suite'] = _SUITE
DESCRIPTOR.message_types_by_name['SuiteEffec'] = _SUITEEFFEC

class ItemsInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMSINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.ItemsInfo)

class XQ_Info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XQ_INFO
  
  # @@protoc_insertion_point(class_scope:protoFile.XQ_Info)

class Suite(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUITE
  
  # @@protoc_insertion_point(class_scope:protoFile.Suite)

class SuiteEffec(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUITEEFFEC
  
  # @@protoc_insertion_point(class_scope:protoFile.SuiteEffec)

# @@protoc_insertion_point(module_scope)