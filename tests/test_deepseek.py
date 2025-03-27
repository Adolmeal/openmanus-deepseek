import pytest
from agents.deepseek_agent import DeepSeekWrapper

@pytest.fixture
def deepseek():
    return DeepSeekWrapper()

def test_deepseek_init(deepseek):
    assert deepseek.model is not None
    assert deepseek.tokenizer is not None

def test_code_generation(deepseek):
    test_prompt = "生成简单的网格划分脚本"
    code = deepseek.generate_ansys_script(test_prompt)
    assert "/PREP7" in code
    assert "ET," in code
    assert "ESIZE" in code

def test_error_handling(deepseek):
    invalid_prompt = ""
    with pytest.raises(Exception):
        deepseek.generate_ansys_script(invalid_prompt)
