# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yacht/config/proto/meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yacht/config/proto/meta.proto',
  package='yacht.config.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dyacht/config/proto/meta.proto\x12\x12yacht.config.proto\"\x97\x01\n\nMetaConfig\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x1f\n\x17metrics_to_save_best_on\x18\x02 \x03(\t\x12\x1f\n\x17metrics_to_load_best_on\x18\x03 \x03(\t\x12\x1b\n\x13log_frequency_steps\x18\x04 \x01(\x05\x12\x1a\n\x12\x65xperiment_tracker\x18\x05 \x01(\tb\x06proto3')
)




_METACONFIG = _descriptor.Descriptor(
  name='MetaConfig',
  full_name='yacht.config.proto.MetaConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='yacht.config.proto.MetaConfig.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics_to_save_best_on', full_name='yacht.config.proto.MetaConfig.metrics_to_save_best_on', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics_to_load_best_on', full_name='yacht.config.proto.MetaConfig.metrics_to_load_best_on', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_frequency_steps', full_name='yacht.config.proto.MetaConfig.log_frequency_steps', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_tracker', full_name='yacht.config.proto.MetaConfig.experiment_tracker', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=54,
  serialized_end=205,
)

DESCRIPTOR.message_types_by_name['MetaConfig'] = _METACONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetaConfig = _reflection.GeneratedProtocolMessageType('MetaConfig', (_message.Message,), dict(
  DESCRIPTOR = _METACONFIG,
  __module__ = 'yacht.config.proto.meta_pb2'
  # @@protoc_insertion_point(class_scope:yacht.config.proto.MetaConfig)
  ))
_sym_db.RegisterMessage(MetaConfig)


# @@protoc_insertion_point(module_scope)
