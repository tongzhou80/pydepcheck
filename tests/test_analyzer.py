from pydepcheck import analyze_loop_dependences

def test_valid_code():
    source_code = """
for i in range(10):
    a[i] = a[i-1] + 1
"""
    result = analyze_loop_dependences(source_code)
    assert result.analyzable is True
    assert result.fail_reason is None
    assert isinstance(result.dependences, list)

def test_invalid_code():
    source_code = """
for i in range(10)
    a[i] = a[i-1] + 1
"""  # Missing colon
    result = analyze_loop_dependences(source_code)
    assert result.analyzable is False
    assert result.fail_reason == 'AST parsing failed'
    assert result.dependences == []

def test_empty_code():
    source_code = ""
    result = analyze_loop_dependences(source_code)
    assert result.analyzable is True
    assert result.fail_reason is None
    assert result.dependences == []