# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/skill/getAllSkills.proto',
  package='protoFile.skill.getAllSkills',
  serialized_pb='\n\"protoFile/skill/getAllSkills.proto\x12\x1cprotoFile.skill.getAllSkills\"!\n\x13getAllSkillsRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"q\n\x14getAllSkillsResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x38\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32*.protoFile.skill.getAllSkills.ResponseData\"o\n\x0cResponseData\x12\x12\n\nskillLevel\x18\x01 \x01(\x05\x12:\n\tskillInfo\x18\x02 \x01(\x0b\x32\'.protoFile.skill.getAllSkills.SkillData\x12\x0f\n\x07\x65\x66\x66\x65\x63ts\x18\x03 \x03(\t\"\x8c\x03\n\tSkillData\x12\x11\n\tgroupType\x18\x01 \x01(\x05\x12\x1e\n\x16professionStageRequire\x18\x02 \x01(\x05\x12\x18\n\x10removeEffectRate\x18\x03 \x01(\t\x12\x11\n\taddEffect\x18\x04 \x01(\t\x12\x0f\n\x07useRate\x18\x05 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\r\n\x05level\x18\x07 \x01(\x05\x12\x0c\n\x04type\x18\x08 \x01(\x05\x12\x0e\n\x06weapon\x18\t \x01(\x05\x12\x14\n\x0clevelRequire\x18\n \x01(\x05\x12\x16\n\x0e\x61\x64\x64\x45\x66\x66\x65\x63tNames\x18\x0b \x03(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x0f\n\x07useCoin\x18\r \x01(\x05\x12\x17\n\x0fskillProfession\x18\x0e \x01(\x05\x12\x14\n\x0cremoveEffect\x18\x0f \x01(\t\x12\x15\n\raddEffectRate\x18\x10 \x01(\t\x12\r\n\x05useMp\x18\x11 \x01(\x05\x12\x10\n\x08maxLevel\x18\x12 \x01(\x05\x12\n\n\x02id\x18\x13 \x01(\x05\x12\x0c\n\x04icon\x18\x14 \x01(\t')




_GETALLSKILLSREQUEST = descriptor.Descriptor(
  name='getAllSkillsRequest',
  full_name='protoFile.skill.getAllSkills.getAllSkillsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.skill.getAllSkills.getAllSkillsRequest.id', index=0,
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
  serialized_start=68,
  serialized_end=101,
)


_GETALLSKILLSRESPONSE = descriptor.Descriptor(
  name='getAllSkillsResponse',
  full_name='protoFile.skill.getAllSkills.getAllSkillsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.skill.getAllSkills.getAllSkillsResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.skill.getAllSkills.getAllSkillsResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.skill.getAllSkills.getAllSkillsResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=103,
  serialized_end=216,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='protoFile.skill.getAllSkills.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='skillLevel', full_name='protoFile.skill.getAllSkills.ResponseData.skillLevel', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='skillInfo', full_name='protoFile.skill.getAllSkills.ResponseData.skillInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='effects', full_name='protoFile.skill.getAllSkills.ResponseData.effects', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=218,
  serialized_end=329,
)


_SKILLDATA = descriptor.Descriptor(
  name='SkillData',
  full_name='protoFile.skill.getAllSkills.SkillData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='groupType', full_name='protoFile.skill.getAllSkills.SkillData.groupType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='professionStageRequire', full_name='protoFile.skill.getAllSkills.SkillData.professionStageRequire', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='removeEffectRate', full_name='protoFile.skill.getAllSkills.SkillData.removeEffectRate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='addEffect', full_name='protoFile.skill.getAllSkills.SkillData.addEffect', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='useRate', full_name='protoFile.skill.getAllSkills.SkillData.useRate', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='protoFile.skill.getAllSkills.SkillData.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='protoFile.skill.getAllSkills.SkillData.level', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.skill.getAllSkills.SkillData.type', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weapon', full_name='protoFile.skill.getAllSkills.SkillData.weapon', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='levelRequire', full_name='protoFile.skill.getAllSkills.SkillData.levelRequire', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='addEffectNames', full_name='protoFile.skill.getAllSkills.SkillData.addEffectNames', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='protoFile.skill.getAllSkills.SkillData.name', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='useCoin', full_name='protoFile.skill.getAllSkills.SkillData.useCoin', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='skillProfession', full_name='protoFile.skill.getAllSkills.SkillData.skillProfession', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='removeEffect', full_name='protoFile.skill.getAllSkills.SkillData.removeEffect', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='addEffectRate', full_name='protoFile.skill.getAllSkills.SkillData.addEffectRate', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='useMp', full_name='protoFile.skill.getAllSkills.SkillData.useMp', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxLevel', full_name='protoFile.skill.getAllSkills.SkillData.maxLevel', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.skill.getAllSkills.SkillData.id', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon', full_name='protoFile.skill.getAllSkills.SkillData.icon', index=19,
      number=20, type=9, cpp_type=9, label=1,
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
  serialized_start=332,
  serialized_end=728,
)

_GETALLSKILLSRESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
_RESPONSEDATA.fields_by_name['skillInfo'].message_type = _SKILLDATA
DESCRIPTOR.message_types_by_name['getAllSkillsRequest'] = _GETALLSKILLSREQUEST
DESCRIPTOR.message_types_by_name['getAllSkillsResponse'] = _GETALLSKILLSRESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['SkillData'] = _SKILLDATA

class getAllSkillsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETALLSKILLSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.skill.getAllSkills.getAllSkillsRequest)

class getAllSkillsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETALLSKILLSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.skill.getAllSkills.getAllSkillsResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.skill.getAllSkills.ResponseData)

class SkillData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SKILLDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.skill.getAllSkills.SkillData)

# @@protoc_insertion_point(module_scope)
