# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yacht/config/proto/train.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yacht/config/proto/train.proto',
  package='yacht.config.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1eyacht/config/proto/train.proto\x12\x12yacht.config.proto\"\x91\x03\n\x0bTrainConfig\x12\x14\n\x0ctrainer_name\x18\x01 \x01(\t\x12\x10\n\x08\x65pisodes\x18\x02 \x01(\x05\x12\x15\n\rlearning_rate\x18\x03 \x01(\x02\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\x12\x1a\n\x12\x63ollecting_n_steps\x18\x05 \x01(\x05\x12\x10\n\x08n_epochs\x18\x06 \x01(\x05\x12\r\n\x05gamma\x18\x07 \x01(\x02\x12\x12\n\ngae_lambda\x18\x08 \x01(\x02\x12\x12\n\nclip_range\x18\t \x01(\x02\x12\x1b\n\x13\x65ntropy_coefficient\x18\n \x01(\x02\x12\x16\n\x0evf_coefficient\x18\x0b \x01(\x02\x12\x15\n\rmax_grad_norm\x18\x0c \x01(\x02\x12\x15\n\rk_fold_splits\x18\r \x01(\x05\x12\x1a\n\x12k_fold_purge_ratio\x18\x0e \x01(\x02\x12\x1c\n\x14k_fold_embargo_ratio\x18\x0f \x01(\x02\x12\x16\n\x0e\x65val_frequency\x18\x10 \x01(\x05\x12\x15\n\rlog_frequency\x18\x11 \x01(\x05\x62\x06proto3')
)




_TRAINCONFIG = _descriptor.Descriptor(
  name='TrainConfig',
  full_name='yacht.config.proto.TrainConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer_name', full_name='yacht.config.proto.TrainConfig.trainer_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='episodes', full_name='yacht.config.proto.TrainConfig.episodes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='yacht.config.proto.TrainConfig.learning_rate', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='yacht.config.proto.TrainConfig.batch_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collecting_n_steps', full_name='yacht.config.proto.TrainConfig.collecting_n_steps', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_epochs', full_name='yacht.config.proto.TrainConfig.n_epochs', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gamma', full_name='yacht.config.proto.TrainConfig.gamma', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gae_lambda', full_name='yacht.config.proto.TrainConfig.gae_lambda', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clip_range', full_name='yacht.config.proto.TrainConfig.clip_range', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entropy_coefficient', full_name='yacht.config.proto.TrainConfig.entropy_coefficient', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vf_coefficient', full_name='yacht.config.proto.TrainConfig.vf_coefficient', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_grad_norm', full_name='yacht.config.proto.TrainConfig.max_grad_norm', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k_fold_splits', full_name='yacht.config.proto.TrainConfig.k_fold_splits', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k_fold_purge_ratio', full_name='yacht.config.proto.TrainConfig.k_fold_purge_ratio', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k_fold_embargo_ratio', full_name='yacht.config.proto.TrainConfig.k_fold_embargo_ratio', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eval_frequency', full_name='yacht.config.proto.TrainConfig.eval_frequency', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_frequency', full_name='yacht.config.proto.TrainConfig.log_frequency', index=16,
      number=17, type=5, cpp_type=1, label=1,
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
  serialized_start=55,
  serialized_end=456,
)

DESCRIPTOR.message_types_by_name['TrainConfig'] = _TRAINCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainConfig = _reflection.GeneratedProtocolMessageType('TrainConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRAINCONFIG,
  __module__ = 'yacht.config.proto.train_pb2'
  # @@protoc_insertion_point(class_scope:yacht.config.proto.TrainConfig)
  ))
_sym_db.RegisterMessage(TrainConfig)


# @@protoc_insertion_point(module_scope)
