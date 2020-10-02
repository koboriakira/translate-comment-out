import os
from typing import Optional, Dict, Any
import argparse


def get_environment(key: str) -> Optional[str]:
    return os.getenv(key=key)


def get_argument(key: str) -> Optional[Dict[str, Any]]:
    return vars_args[key] if key in vars_args else None


parser = argparse.ArgumentParser()
parser.add_argument(
    'filepath',
    type=str,)
parser.add_argument(
    '-d', '--dest',
    help='destination language ex.) ja',
    type=str,
    default='ja')
vars_args = vars(parser.parse_args())
