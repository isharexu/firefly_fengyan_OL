# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import app.scense.protoFile.itemInfo_pb2
import app.scense.protoFile.PlayerProperty_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/playerInfo/GetOtherRoleInfo221.proto',
  package='protoFile.playerInfo.GetOtherRoleInfo221',
  serialized_pb='\n.protoFile/playerInfo/GetOtherRoleInfo221.proto\x12(protoFile.playerInfo.GetOtherRoleInfo221\x1a\x18protoFile/itemInfo.proto\x1a\x1eprotoFile/PlayerProperty.proto\"5\n\x17GetOtherRoleInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06roleId\x18\x02 \x02(\x05\"\x85\x01\n\x18GetOtherRoleInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12H\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32:.protoFile.playerInfo.GetOtherRoleInfo221.ResponseInfoData\"\x9c\x01\n\x10ResponseInfoData\x12\x34\n\rotherRoleInfo\x18\x01 \x02(\x0b\x32\x1d.protoFile.PlayerPropertyInfo\x12R\n\rotherRoleItem\x18\x02 \x03(\x0b\x32;.protoFile.playerInfo.GetOtherRoleInfo221.OtherRoleItemInfo\"M\n\x11OtherRoleItemInfo\x12&\n\x08itemInfo\x18\x01 \x01(\x0b\x32\x14.protoFile.ItemsInfo\x12\x10\n\x08position\x18\x02 \x01(\x05')




_GETOTHERROLEINFOREQUEST = descriptor.Descriptor(
  name='GetOtherRoleInfoRequest',
  full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roleId', full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoRequest.roleId', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=150,
  serialized_end=203,
)


_GETOTHERROLEINFORESPONSE = descriptor.Descriptor(
  name='GetOtherRoleInfoResponse',
  full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoResponse.data', index=2,
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
  serialized_start=206,
  serialized_end=339,
)


_RESPONSEINFODATA = descriptor.Descriptor(
  name='ResponseInfoData',
  full_name='protoFile.playerInfo.GetOtherRoleInfo221.ResponseInfoData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='otherRoleInfo', full_name='protoFile.playerInfo.GetOtherRoleInfo221.ResponseInfoData.otherRoleInfo', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='otherRoleItem', full_name='protoFile.playerInfo.GetOtherRoleInfo221.ResponseInfoData.otherRoleItem', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=342,
  serialized_end=498,
)


_OTHERROLEITEMINFO = descriptor.Descriptor(
  name='OtherRoleItemInfo',
  full_name='protoFile.playerInfo.GetOtherRoleInfo221.OtherRoleItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemInfo', full_name='protoFile.playerInfo.GetOtherRoleInfo221.OtherRoleItemInfo.itemInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='position', full_name='protoFile.playerInfo.GetOtherRoleInfo221.OtherRoleItemInfo.position', index=1,
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
  serialized_start=500,
  serialized_end=577,
)

_GETOTHERROLEINFORESPONSE.fields_by_name['data'].message_type = _RESPONSEINFODATA
_RESPONSEINFODATA.fields_by_name['otherRoleInfo'].message_type = app.scense.protoFile.PlayerProperty_pb2._PLAYERPROPERTYINFO
_RESPONSEINFODATA.fields_by_name['otherRoleItem'].message_type = _OTHERROLEITEMINFO
_OTHERROLEITEMINFO.fields_by_name['itemInfo'].message_type = app.scense.protoFile.itemInfo_pb2._ITEMSINFO
DESCRIPTOR.message_types_by_name['GetOtherRoleInfoRequest'] = _GETOTHERROLEINFOREQUEST
DESCRIPTOR.message_types_by_name['GetOtherRoleInfoResponse'] = _GETOTHERROLEINFORESPONSE
DESCRIPTOR.message_types_by_name['ResponseInfoData'] = _RESPONSEINFODATA
DESCRIPTOR.message_types_by_name['OtherRoleItemInfo'] = _OTHERROLEITEMINFO

class GetOtherRoleInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETOTHERROLEINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoRequest)

class GetOtherRoleInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETOTHERROLEINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.playerInfo.GetOtherRoleInfo221.GetOtherRoleInfoResponse)

class ResponseInfoData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEINFODATA
  
  # @@protoc_insertion_point(class_scope:protoFile.playerInfo.GetOtherRoleInfo221.ResponseInfoData)

class OtherRoleItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OTHERROLEITEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.playerInfo.GetOtherRoleInfo221.OtherRoleItemInfo)

# @@protoc_insertion_point(module_scope)
