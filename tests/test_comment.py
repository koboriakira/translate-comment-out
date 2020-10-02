from typing import List
from translate_comment_out import comment


def test_is_comment_out():
    line = '     //  This is a comment.'
    assert comment.is_comment_out(line)


def test_is_comment_out_false():
    line = 'const test = "This is not a comment"'
    assert not comment.is_comment_out(line)


def test_is_url_comment_out():
    line = '    // https://github.com/webpack/webpack-dev-server/issues/887'
    assert comment.is_url_comment_out(line)
    line = '    // http://github.com/webpack/webpack-dev-server/issues/887'
    assert comment.is_url_comment_out(line)


def test_is_url_comment_out_false():
    line = '    // websites from potentially accessing local content through DNS rebinding:'
    assert not comment.is_url_comment_out(line)


def test_get_comment():
    # setup
    idx = 0
    lines: List[str] = []
    lines.append('// This is a first comment.\n')
    lines.append('// This is a second comment.\n')
    lines.append('const test = "This is not a comment"\n')

    # execute
    actual, skip_idx = comment.get_comment(idx=idx, lines=lines)

    # verify
    expect = '// This is a first comment. This is a second comment.'
    assert skip_idx == [0, 1]
    assert actual == expect


def test_extract_comment_from_line() -> str:
    line = '// This is a first comment.\n'
    actual = comment._extract_comment_from_line(line=line, is_first_line=False)
    expect = 'This is a first comment.'
    assert actual == expect
