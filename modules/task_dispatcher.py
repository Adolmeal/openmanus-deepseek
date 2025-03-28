from deepseek_coder import generate_code
from openmanus import call_tool, train_model

def dispatch_task(task):
    # ...existing code...
    if task["type"] == "generate_code":
        result = generate_code(task["details"])
        return result, False
    elif task["type"] == "call_tool":
        result = call_tool(task["details"])
        return result, False
    elif task["type"] == "train_model":
        result = train_model(task["details"])
        return result, True  # 假设训练需要用户反馈
    else:
        return "无法识别的任务类型", False
