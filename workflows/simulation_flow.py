from agents import DeepSeekAgent, TaskPlanner

def run_simulation(task: str):
    # 任务拆解
    planner = TaskPlanner()
    subtasks = planner.breakdown(task)  # 调用OpenManus多智能体拆解
    
    # 调用DeepSeek生成代码
    ds_agent = DeepSeekAgent()
    code_snippets = []
    for subtask in subtasks:
        code = ds_agent.generate(f"生成ANSYS APDL脚本：{subtask}")
        code_snippets.append(auto_correct(code))  # 自动纠错[citation:3]
    
    return integrate_codes(code_snippets)  # 整合为完整工作流
