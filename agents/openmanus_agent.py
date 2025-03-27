from typing import List
from openmanus import TaskPlanner

class OpenManusAdapter:
    def __init__(self):
        self.planner = TaskPlanner()
    
    def decompose_task(self, user_input: str) -> List[str]:
        """将复杂任务拆解为可执行的子任务序列"""
        return self.planner.plan(user_input).subtasks
    
    def validate_subtask(self, subtask: str) -> bool:
        """验证子任务是否符合OpenManus规范"""
        return self.planner.validate(subtask)
