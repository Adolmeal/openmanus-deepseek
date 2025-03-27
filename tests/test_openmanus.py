import pytest
from agents.openmanus_agent import OpenManusAdapter

@pytest.fixture
def openmanus():
    return OpenManusAdapter()

def test_task_decomposition(openmanus):
    complex_task = "完成一个包含热分析和结构分析的耦合仿真"
    subtasks = openmanus.decompose_task(complex_task)
    assert len(subtasks) >= 2
    assert "热分析" in subtasks[0]
    assert "结构分析" in subtasks[1]

def test_subtask_validation(openmanus):
    valid_subtask = "进行网格独立性验证"
    invalid_subtask = "非标准操作指令"
    assert openmanus.validate_subtask(valid_subtask) is True
    assert openmanus.validate_subtask(invalid_subtask) is False
