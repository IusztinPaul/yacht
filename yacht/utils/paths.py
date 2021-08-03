import os


def build_config_path(project_root_dir: str, config_name: str) -> str:
    return os.path.join(project_root_dir, 'yacht', 'config', 'configs', config_name)


def build_last_checkpoint_path(storage_dir: str) -> str:
    return build_checkpoints_path(storage_dir, 'last_checkpoint.zip')


def build_best_checkpoint_path(storage_dir: str) -> str:
    return build_checkpoints_path(storage_dir, 'best_model.zip')


def build_best_checkpoint_dir(storage_dir: str) -> str:
    return build_checkpoints_path(storage_dir, '')


def build_checkpoints_path(storage_dir: str, file_name: str) -> str:
    checkpoint_dir = os.path.join(storage_dir, 'checkpoints')
    if not os.path.exists(checkpoint_dir):
        os.mkdir(checkpoint_dir)

    return os.path.join(checkpoint_dir, file_name)


def build_graphics_path(storage_dir: str, file_name: str) -> str:
    graphics_dir = os.path.join(storage_dir, 'graphics')
    if not os.path.exists(graphics_dir):
        os.mkdir(graphics_dir)

    return os.path.join(graphics_dir, file_name)


def build_cache_path(storage_dir: str) -> str:
    return os.path.join(storage_dir, '.cache.json')


def build_log_path(storage_dir: str) -> str:
    return os.path.join(storage_dir, 'log')
