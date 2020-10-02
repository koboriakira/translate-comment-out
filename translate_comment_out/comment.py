import re
from typing import List, Tuple
from googletrans import Translator as GoogleTranslator


google_translator = GoogleTranslator()


def is_comment_out(line: str) -> bool:
    return re.match(r'^\s*//.*$', line) is not None


def get_comment(idx: int, lines: List[str]) -> Tuple[str, List[int]]:
    comment_list: List[str] = []
    idx_list: List[int] = []
    for sub_idx in list(map(lambda i: i + idx, range(len(lines) - idx))):
        line: str = lines[sub_idx]
        if is_comment_out(line):
            is_first_line: bool = (idx == sub_idx)
            comment: str = _extract_comment_from_line(line, is_first_line)
            comment_list.append(comment)
            idx_list.append(sub_idx)
        else:
            break
    return " ".join(comment_list), idx_list


def _extract_comment_from_line(line: str, is_first_line: bool) -> str:
    if is_first_line:
        return line.replace('\n', '')
    else:
        return re.sub(r'^\s*/+\s*', '', line).replace('\n', '')


def translate_comment(comment: str, dest: str) -> str:
    spaces, *text = tuple(comment.split('//'))
    if text is not str:
        text: str = " ".join(text)
    translated_text: str = google_translator.translate(text, dest=dest).text
    return "//".join([spaces, translated_text])
