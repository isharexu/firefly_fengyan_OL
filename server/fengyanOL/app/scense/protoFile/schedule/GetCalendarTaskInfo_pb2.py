# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/schedule/GetCalendarTaskInfo.proto',
  package='protoFile.schedule.GetCalendarTaskInfo',
  serialized_pb='\n,protoFile/schedule/GetCalendarTaskInfo.proto\x12&protoFile.schedule.GetCalendarTaskInfo\",\n\x1eGetCalendarTaskListInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"\x86\x01\n\x1bGetCalendarTaskInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x46\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x38.protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo\"\xfc\x01\n\x10\x43\x61lendarTaskInfo\x12\x18\n\x10totalLivenessNum\x18\x01 \x01(\x05\x12\x44\n\nunfinished\x18\x02 \x03(\x0b\x32\x30.protoFile.schedule.GetCalendarTaskInfo.Schedule\x12\x42\n\x08\x66inished\x18\x03 \x03(\x0b\x32\x30.protoFile.schedule.GetCalendarTaskInfo.Schedule\x12\x44\n\rscheduleBound\x18\x04 \x03(\x0b\x32-.protoFile.schedule.GetCalendarTaskInfo.Bound\"Z\n\x08Schedule\x12\x12\n\nscheduleId\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0b\n\x03now\x18\x03 \x01(\x05\x12\r\n\x05total\x18\x04 \x01(\x05\x12\x10\n\x08\x61\x63tivity\x18\x05 \x01(\x05\"\'\n\x05\x42ound\x12\x0c\n\x04step\x18\x01 \x01(\x05\x12\x10\n\x08received\x18\x02 \x01(\x05')




_GETCALENDARTASKLISTINFOREQUEST = descriptor.Descriptor(
  name='GetCalendarTaskListInfoRequest',
  full_name='protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskListInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskListInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=88,
  serialized_end=132,
)


_GETCALENDARTASKINFORESPONSE = descriptor.Descriptor(
  name='GetCalendarTaskInfoResponse',
  full_name='protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskInfoResponse.data', index=2,
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
  serialized_start=135,
  serialized_end=269,
)


_CALENDARTASKINFO = descriptor.Descriptor(
  name='CalendarTaskInfo',
  full_name='protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='totalLivenessNum', full_name='protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo.totalLivenessNum', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='unfinished', full_name='protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo.unfinished', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='finished', full_name='protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo.finished', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scheduleBound', full_name='protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo.scheduleBound', index=3,
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
  serialized_start=272,
  serialized_end=524,
)


_SCHEDULE = descriptor.Descriptor(
  name='Schedule',
  full_name='protoFile.schedule.GetCalendarTaskInfo.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='scheduleId', full_name='protoFile.schedule.GetCalendarTaskInfo.Schedule.scheduleId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='desc', full_name='protoFile.schedule.GetCalendarTaskInfo.Schedule.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='now', full_name='protoFile.schedule.GetCalendarTaskInfo.Schedule.now', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='total', full_name='protoFile.schedule.GetCalendarTaskInfo.Schedule.total', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='activity', full_name='protoFile.schedule.GetCalendarTaskInfo.Schedule.activity', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=526,
  serialized_end=616,
)


_BOUND = descriptor.Descriptor(
  name='Bound',
  full_name='protoFile.schedule.GetCalendarTaskInfo.Bound',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='step', full_name='protoFile.schedule.GetCalendarTaskInfo.Bound.step', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='received', full_name='protoFile.schedule.GetCalendarTaskInfo.Bound.received', index=1,
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
  serialized_start=618,
  serialized_end=657,
)

_GETCALENDARTASKINFORESPONSE.fields_by_name['data'].message_type = _CALENDARTASKINFO
_CALENDARTASKINFO.fields_by_name['unfinished'].message_type = _SCHEDULE
_CALENDARTASKINFO.fields_by_name['finished'].message_type = _SCHEDULE
_CALENDARTASKINFO.fields_by_name['scheduleBound'].message_type = _BOUND
DESCRIPTOR.message_types_by_name['GetCalendarTaskListInfoRequest'] = _GETCALENDARTASKLISTINFOREQUEST
DESCRIPTOR.message_types_by_name['GetCalendarTaskInfoResponse'] = _GETCALENDARTASKINFORESPONSE
DESCRIPTOR.message_types_by_name['CalendarTaskInfo'] = _CALENDARTASKINFO
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
DESCRIPTOR.message_types_by_name['Bound'] = _BOUND

class GetCalendarTaskListInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCALENDARTASKLISTINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskListInfoRequest)

class GetCalendarTaskInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCALENDARTASKINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.schedule.GetCalendarTaskInfo.GetCalendarTaskInfoResponse)

class CalendarTaskInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CALENDARTASKINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.schedule.GetCalendarTaskInfo.CalendarTaskInfo)

class Schedule(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SCHEDULE
  
  # @@protoc_insertion_point(class_scope:protoFile.schedule.GetCalendarTaskInfo.Schedule)

class Bound(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BOUND
  
  # @@protoc_insertion_point(class_scope:protoFile.schedule.GetCalendarTaskInfo.Bound)

# @@protoc_insertion_point(module_scope)
