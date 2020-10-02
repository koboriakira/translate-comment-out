from typing import List
from translate_comment_out.config import get_environment
from translate_comment_out.comment import is_comment_out, get_comment, translate_comment


def translate(filepath: str, dest: str = 'ja') -> str:
    if invalid_goolge_application_credentials():
        raise Exception('Set environment \'GOOGLE_APPLICATION_CREDENTIALS\'')

    source_text: List[str] = []
    with open(file=filepath) as f:
        skip_idx: List[int] = []
        lines: List[str] = f.readlines()
        for idx, line in enumerate(lines):
            if idx in skip_idx:
                continue
            if is_comment_out(line):
                comment, idx_list = get_comment(idx, lines)
                skip_idx.extend(idx_list)
                translated_comment = translate_comment(comment, dest)
                source_text.append(f'{translated_comment}\n')
            else:
                source_text.append(line)
    return "".join(source_text)


def invalid_goolge_application_credentials():
    return get_environment('GOOGLE_APPLICATION_CREDENTIALS') is None
