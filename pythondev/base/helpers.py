from importlib import import_module


def get_class_instance(modulo, class_name):
    return getattr(import_module(modulo), class_name)
