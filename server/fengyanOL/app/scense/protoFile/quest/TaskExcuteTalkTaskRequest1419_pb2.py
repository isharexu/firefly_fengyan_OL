# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/TaskExcuteTalkTaskRequest1419.proto',
  package='protoFile.quest.TaskExcuteTalkTaskRequest1419',
  serialized_pb='\n3protoFile/quest/TaskExcuteTalkTaskRequest1419.proto\x12-protoFile.quest.TaskExcuteTalkTaskRequest1419\"H\n\x19TaskExcuteTalkTaskRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07task_id\x18\x02 \x02(\x05\x12\x0e\n\x06npc_id\x18\x03 \x01(\x05\"=\n\x1aTaskExcuteTalkTaskResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_TASKEXCUTETALKTASKREQUEST = descriptor.Descriptor(
  name='TaskExcuteTalkTaskRequest',
  full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_id', full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskRequest.task_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_id', full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskRequest.npc_id', index=2,
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
  serialized_start=102,
  serialized_end=174,
)


_TASKEXCUTETALKTASKRESPONSE = descriptor.Descriptor(
  name='TaskExcuteTalkTaskResponse',
  full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=176,
  serialized_end=237,
)

DESCRIPTOR.message_types_by_name['TaskExcuteTalkTaskRequest'] = _TASKEXCUTETALKTASKREQUEST
DESCRIPTOR.message_types_by_name['TaskExcuteTalkTaskResponse'] = _TASKEXCUTETALKTASKRESPONSE

class TaskExcuteTalkTaskRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKEXCUTETALKTASKREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskRequest)

class TaskExcuteTalkTaskResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKEXCUTETALKTASKRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskExcuteTalkTaskRequest1419.TaskExcuteTalkTaskResponse)

# @@protoc_insertion_point(module_scope)