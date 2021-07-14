# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yacht/config/proto/environment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yacht.config.proto import reward_schema_pb2 as yacht_dot_config_dot_proto_dot_reward__schema__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yacht/config/proto/environment.proto',
  package='yacht.config.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n$yacht/config/proto/environment.proto\x12\x12yacht.config.proto\x1a&yacht/config/proto/reward_schema.proto\"\xfd\x01\n\x11\x45nvironmentConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0e\x62uy_commission\x18\x02 \x01(\x02\x12\x17\n\x0fsell_commission\x18\x03 \x01(\x02\x12\x1d\n\x15initial_cash_position\x18\x04 \x01(\x02\x12>\n\x0ereward_schemas\x18\x05 \x03(\x0b\x32&.yacht.config.proto.RewardSchemaConfig\x12\x16\n\x0ereward_scaling\x18\x06 \x01(\x02\x12\x15\n\raction_schema\x18\x07 \x01(\t\x12\x1b\n\x13max_units_per_asset\x18\x08 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[yacht_dot_config_dot_proto_dot_reward__schema__pb2.DESCRIPTOR,])




_ENVIRONMENTCONFIG = _descriptor.Descriptor(
  name='EnvironmentConfig',
  full_name='yacht.config.proto.EnvironmentConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yacht.config.proto.EnvironmentConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buy_commission', full_name='yacht.config.proto.EnvironmentConfig.buy_commission', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sell_commission', full_name='yacht.config.proto.EnvironmentConfig.sell_commission', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_cash_position', full_name='yacht.config.proto.EnvironmentConfig.initial_cash_position', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_schemas', full_name='yacht.config.proto.EnvironmentConfig.reward_schemas', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reward_scaling', full_name='yacht.config.proto.EnvironmentConfig.reward_scaling', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_schema', full_name='yacht.config.proto.EnvironmentConfig.action_schema', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_units_per_asset', full_name='yacht.config.proto.EnvironmentConfig.max_units_per_asset', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=354,
)

_ENVIRONMENTCONFIG.fields_by_name['reward_schemas'].message_type = yacht_dot_config_dot_proto_dot_reward__schema__pb2._REWARDSCHEMACONFIG
DESCRIPTOR.message_types_by_name['EnvironmentConfig'] = _ENVIRONMENTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnvironmentConfig = _reflection.GeneratedProtocolMessageType('EnvironmentConfig', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENTCONFIG,
  __module__ = 'yacht.config.proto.environment_pb2'
  # @@protoc_insertion_point(class_scope:yacht.config.proto.EnvironmentConfig)
  ))
_sym_db.RegisterMessage(EnvironmentConfig)


# @@protoc_insertion_point(module_scope)
