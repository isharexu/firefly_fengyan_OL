# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='LeaveDuiWu4305.proto',
  package='protoFile.zudui.LeaveDuiWu4305',
  serialized_pb='\n\x14LeaveDuiWu4305.proto\x12\x1eprotoFile.zudui.LeaveDuiWu4305\"-\n\x11LeaveDuiWuRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04\x64wId\x18\x02 \x02(\x05\"5\n\x12LeaveDuiWuResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08')




_LEAVEDUIWUREQUEST = descriptor.Descriptor(
  name='LeaveDuiWuRequest',
  full_name='protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dwId', full_name='protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuRequest.dwId', index=1,
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
  serialized_start=56,
  serialized_end=101,
)


_LEAVEDUIWURESPONSE = descriptor.Descriptor(
  name='LeaveDuiWuResponse',
  full_name='protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuResponse.result', index=1,
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
  serialized_start=103,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['LeaveDuiWuRequest'] = _LEAVEDUIWUREQUEST
DESCRIPTOR.message_types_by_name['LeaveDuiWuResponse'] = _LEAVEDUIWURESPONSE

class LeaveDuiWuRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEAVEDUIWUREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuRequest)

class LeaveDuiWuResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEAVEDUIWURESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.zudui.LeaveDuiWu4305.LeaveDuiWuResponse)

# @@protoc_insertion_point(module_scope)
