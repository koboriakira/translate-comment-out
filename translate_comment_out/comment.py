import re
from typing import List, Tuple
from googletrans import Translator as GoogleTranslator


google_translator = GoogleTranslator()
CHARACTER_SIZE_PER_LINE = 40


def is_comment_out(line: str) -> bool:
    return re.match(r'^\s*//.*$', line) is not None


def is_url_comment_out(line: str) -> bool:
    return re.match(r'^\s*//\s*https?://.*', line) is not None


def get_comment(idx: int, lines: List[str]) -> Tuple[str, List[int]]:
    comment_list: List[str] = []
    idx_list: List[int] = []
    for sub_idx in list(map(lambda i: i + idx, range(len(lines) - idx))):
        line: str = lines[sub_idx]
        if is_url_comment_out(line):
            break
        elif is_comment_out(line):
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
    translated_text_list = _break_line(translated_text)
    return "\n".join(
        list(map(lambda t: f'{spaces}// {t}', translated_text_list)))


def _break_line(text: str) -> List[str]:
    return [text[i: i + CHARACTER_SIZE_PER_LINE]
            for i in range(0, len(text), CHARACTER_SIZE_PER_LINE)]
