# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/pet/TrainingPet2304.proto',
  package='protoFile.pet.TrainingPet2304',
  serialized_pb='\n#protoFile/pet/TrainingPet2304.proto\x12\x1dprotoFile.pet.TrainingPet2304\"E\n\x12TrainingPetRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05petId\x18\x02 \x02(\x05\x12\x14\n\x0ctrainingType\x18\x03 \x02(\x05\"s\n\x13TrainingPetResponse\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12;\n\ttrainInfo\x18\x03 \x01(\x0b\x32(.protoFile.pet.TrainingPet2304.TrainInfo\"\xb1\x01\n\tTrainInfo\x12\x13\n\x0b\x62\x61seLiLiang\x18\x01 \x01(\x05\x12\x15\n\rchangeLiLiang\x18\x02 \x01(\x05\x12\x11\n\tbaseZhiLi\x18\x03 \x01(\x05\x12\x13\n\x0b\x63hangeZhiLi\x18\x04 \x01(\x05\x12\x11\n\tbaseNaiLi\x18\x05 \x01(\x05\x12\x13\n\x0b\x63hangeNaiLi\x18\x06 \x01(\x05\x12\x12\n\nbaseMinJie\x18\x07 \x01(\x05\x12\x14\n\x0c\x63hangeMinJie\x18\x08 \x01(\x05')




_TRAININGPETREQUEST = descriptor.Descriptor(
  name='TrainingPetRequest',
  full_name='protoFile.pet.TrainingPet2304.TrainingPetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.pet.TrainingPet2304.TrainingPetRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='petId', full_name='protoFile.pet.TrainingPet2304.TrainingPetRequest.petId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trainingType', full_name='protoFile.pet.TrainingPet2304.TrainingPetRequest.trainingType', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=70,
  serialized_end=139,
)


_TRAININGPETRESPONSE = descriptor.Descriptor(
  name='TrainingPetResponse',
  full_name='protoFile.pet.TrainingPet2304.TrainingPetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.pet.TrainingPet2304.TrainingPetResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.pet.TrainingPet2304.TrainingPetResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trainInfo', full_name='protoFile.pet.TrainingPet2304.TrainingPetResponse.trainInfo', index=2,
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
  serialized_start=141,
  serialized_end=256,
)


_TRAININFO = descriptor.Descriptor(
  name='TrainInfo',
  full_name='protoFile.pet.TrainingPet2304.TrainInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='baseLiLiang', full_name='protoFile.pet.TrainingPet2304.TrainInfo.baseLiLiang', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changeLiLiang', full_name='protoFile.pet.TrainingPet2304.TrainInfo.changeLiLiang', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseZhiLi', full_name='protoFile.pet.TrainingPet2304.TrainInfo.baseZhiLi', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changeZhiLi', full_name='protoFile.pet.TrainingPet2304.TrainInfo.changeZhiLi', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseNaiLi', full_name='protoFile.pet.TrainingPet2304.TrainInfo.baseNaiLi', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changeNaiLi', full_name='protoFile.pet.TrainingPet2304.TrainInfo.changeNaiLi', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseMinJie', full_name='protoFile.pet.TrainingPet2304.TrainInfo.baseMinJie', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='changeMinJie', full_name='protoFile.pet.TrainingPet2304.TrainInfo.changeMinJie', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=259,
  serialized_end=436,
)

_TRAININGPETRESPONSE.fields_by_name['trainInfo'].message_type = _TRAININFO
DESCRIPTOR.message_types_by_name['TrainingPetRequest'] = _TRAININGPETREQUEST
DESCRIPTOR.message_types_by_name['TrainingPetResponse'] = _TRAININGPETRESPONSE
DESCRIPTOR.message_types_by_name['TrainInfo'] = _TRAININFO

class TrainingPetRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAININGPETREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.TrainingPet2304.TrainingPetRequest)

class TrainingPetResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAININGPETRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.TrainingPet2304.TrainingPetResponse)

class TrainInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRAININFO
  
  # @@protoc_insertion_point(class_scope:protoFile.pet.TrainingPet2304.TrainInfo)

# @@protoc_insertion_point(module_scope)
