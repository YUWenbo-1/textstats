import pytest
from textstats import word_count, char_frequencies, longest_word

# 示例 fixture（小组两个人共用这个夹具）
@pytest.fixture
def sample_text():
    return "Hello, world! 123 test."

# word_count 普通测试
def test_word_count_empty():
    assert word_count("") == 0

def test_word_count_one_token():
    assert word_count("hello") == 1

# 作业要求：parametrize 参数化测试，至少3组
@pytest.mark.parametrize("text, expected", [
    ("", 0),
    ("one", 1),
    ("the end.", 2),
    ("Hi! 567 abc", 3),
])
def test_word_count_param(text, expected):
    assert word_count(text) == expected

# 使用 fixture 的测试1
def test_word_count_with_fixture(sample_text):
    assert word_count(sample_text) == 4

# 使用同一个 fixture 的测试2（满足：同一个fixture被两个不同测试用）
def test_char_freq_with_fixture(sample_text):
    res = char_frequencies(sample_text)
    assert res["h"] == 2

# longest_word 空字符串抛ValueError（作业硬性要求）
def test_longest_word_empty_raise():
    with pytest.raises(ValueError):
        longest_word("")