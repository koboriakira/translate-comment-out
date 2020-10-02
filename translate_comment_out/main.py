from translate_comment_out.translator import translate
from translate_comment_out.config import get_argument


def cli():
    filepath: str = get_argument('filepath')
    dest: str = get_argument('dest')
    translated_source = translate(filepath=filepath, dest=dest)
    print(translated_source)
