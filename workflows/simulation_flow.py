from agents import DeepSeekWrapper, OpenManusAdapter
from typing import Dict
import re

class SimulationWorkflow:
    def __init__(self):
        self.ds_agent = DeepSeekWrapper()
        self.om_adapter = OpenManusAdapter()
        
    def _error_correction(self, code: str) -> str:
        """自动纠错机制"""
        # 常见错误模式匹配
        error_patterns = {
            r"ET,\d+,SOLID\b": "ET,1,SOLID185",  # 修正元素类型
            r"MP,EX,\d+,2e11": "MP,EX,1,2e11",    # 修正材料编号
            r"ESIZE,\d+\.\d+": "ESIZE,0.5"        # 标准化网格尺寸
        }
        
        for pattern, replacement in error_patterns.items():
            code = re.sub(pattern, replacement, code)
        return code
    
    def execute_workflow(self, user_request: str) -> Dict:
        """端到端执行流程"""
        # 任务拆解
        subtasks = self.om_adapter.decompose_task(user_request)
        
        # 代码生成与纠错
        generated_scripts = []
        for idx, subtask in enumerate(subtasks, 1):
            raw_code = self.ds_agent.generate_ansys_script(subtask)
            corrected_code = self._error_correction(raw_code)
            generated_scripts.append({
                "subtask_id": idx,
                "original_code": raw_code,
                "corrected_code": corrected_code
            })
        
        # 结果整合
        return {
            "status": "success",
            "subtasks": generated_scripts,
            "combined_script": "\n".join([s["corrected_code"] for s in generated_scripts])
        }
