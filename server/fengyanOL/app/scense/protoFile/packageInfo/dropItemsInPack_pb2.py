# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/packageInfo/dropItemsInPack.proto',
  package='protoFile.packageInfo.GetShangJiaoInfo3304',
  serialized_pb='\n+protoFile/packageInfo/dropItemsInPack.proto\x12*protoFile.packageInfo.GetShangJiaoInfo3304\"\\\n\x16\x64ropItemsInPackRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08position\x18\x02 \x02(\x05\x12\x13\n\x0bpackageType\x18\x03 \x02(\x05\x12\x0f\n\x07\x63urPage\x18\x04 \x02(\x05\"H\n\x17\x64ropItemsInPackResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x05')




_DROPITEMSINPACKREQUEST = descriptor.Descriptor(
  name='dropItemsInPackRequest',
  full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='position', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackRequest.position', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='packageType', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackRequest.packageType', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curPage', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackRequest.curPage', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=91,
  serialized_end=183,
)


_DROPITEMSINPACKRESPONSE = descriptor.Descriptor(
  name='dropItemsInPackResponse',
  full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackResponse.data', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=185,
  serialized_end=257,
)

DESCRIPTOR.message_types_by_name['dropItemsInPackRequest'] = _DROPITEMSINPACKREQUEST
DESCRIPTOR.message_types_by_name['dropItemsInPackResponse'] = _DROPITEMSINPACKRESPONSE

class dropItemsInPackRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DROPITEMSINPACKREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackRequest)

class dropItemsInPackResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DROPITEMSINPACKRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.packageInfo.GetShangJiaoInfo3304.dropItemsInPackResponse)

# @@protoc_insertion_point(module_scope)