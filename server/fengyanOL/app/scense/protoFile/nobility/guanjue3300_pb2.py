# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/nobility/guanjue3300.proto',
  package='protoFile.nobility.guanjue3300',
  serialized_pb='\n$protoFile/nobility/guanjue3300.proto\x12\x1eprotoFile.nobility.guanjue3300\"4\n\x15GetGuanJueInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x63urpage\x18\x02 \x01(\x05\"t\n\x16GetGuanJueInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x39\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32+.protoFile.nobility.guanjue3300.GuanJueInfo\"\xc6\x02\n\x0bGuanJueInfo\x12\x15\n\rcurrentJuewei\x18\x01 \x01(\t\x12\x0f\n\x07weiwang\x18\x02 \x01(\x05\x12\x14\n\x0c\x63urrentJinbi\x18\x03 \x01(\x05\x12\x14\n\x0c\x63urrentDouqi\x18\x04 \x01(\x05\x12\r\n\x05\x61\x64\x64\x64q\x18\x05 \x03(\t\x12\x12\n\nnextJuewei\x18\x06 \x01(\t\x12\x13\n\x0bnextWeiwang\x18\x07 \x01(\x05\x12\x11\n\tnextJinbi\x18\x08 \x01(\x05\x12\x11\n\tnextDouqi\x18\t \x01(\x05\x12\r\n\x05\x61\x64\x64xj\x18\n \x03(\t\x12\r\n\x05\x66time\x18\x0b \x03(\t\x12\x10\n\x08\x66\x63ontext\x18\x0c \x03(\t\x12\x0f\n\x07\x63urpage\x18\r \x01(\x05\x12\x11\n\ttotalpage\x18\x0e \x01(\x05\x12\x0c\n\x04isjw\x18\x0f \x01(\x08\x12\x14\n\x0chasGetSalary\x18\x10 \x01(\x08\x12\r\n\x05level\x18\x11 \x01(\x05')




_GETGUANJUEINFOREQUEST = descriptor.Descriptor(
  name='GetGuanJueInfoRequest',
  full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curpage', full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoRequest.curpage', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=72,
  serialized_end=124,
)


_GETGUANJUEINFORESPONSE = descriptor.Descriptor(
  name='GetGuanJueInfoResponse',
  full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.nobility.guanjue3300.GetGuanJueInfoResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=126,
  serialized_end=242,
)


_GUANJUEINFO = descriptor.Descriptor(
  name='GuanJueInfo',
  full_name='protoFile.nobility.guanjue3300.GuanJueInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='currentJuewei', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.currentJuewei', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weiwang', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.weiwang', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='currentJinbi', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.currentJinbi', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='currentDouqi', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.currentDouqi', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='adddq', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.adddq', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nextJuewei', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.nextJuewei', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nextWeiwang', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.nextWeiwang', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nextJinbi', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.nextJinbi', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nextDouqi', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.nextDouqi', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='addxj', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.addxj', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ftime', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.ftime', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fcontext', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.fcontext', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curpage', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.curpage', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='totalpage', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.totalpage', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isjw', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.isjw', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hasGetSalary', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.hasGetSalary', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protoFile.nobility.guanjue3300.GuanJueInfo.level', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=245,
  serialized_end=571,
)

_GETGUANJUEINFORESPONSE.fields_by_name['data'].message_type = _GUANJUEINFO
DESCRIPTOR.message_types_by_name['GetGuanJueInfoRequest'] = _GETGUANJUEINFOREQUEST
DESCRIPTOR.message_types_by_name['GetGuanJueInfoResponse'] = _GETGUANJUEINFORESPONSE
DESCRIPTOR.message_types_by_name['GuanJueInfo'] = _GUANJUEINFO

class GetGuanJueInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETGUANJUEINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.nobility.guanjue3300.GetGuanJueInfoRequest)

class GetGuanJueInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETGUANJUEINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.nobility.guanjue3300.GetGuanJueInfoResponse)

class GuanJueInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUANJUEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.nobility.guanjue3300.GuanJueInfo)

# @@protoc_insertion_point(module_scope)