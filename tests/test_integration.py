import pytest
from workflows.simulation_flow import SimulationWorkflow

@pytest.fixture
def workflow():
    return SimulationWorkflow()

def test_full_workflow(workflow):
    user_request = "生成圆柱绕流仿真脚本，Re=2e5"
    result = workflow.execute_workflow(user_request)
    
    assert result["status"] == "success"
    assert len(result["subtasks"]) >= 1
    assert "FLDATA" in result["combined_script"]
    assert "SOLVE" in result["combined_script"]
