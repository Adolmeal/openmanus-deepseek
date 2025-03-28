def parse_user_input(user_input):
    # ...existing code...
    # 示例：根据输入生成任务字典
    if "训练模型" in user_input:
        return {"type": "train_model", "details": user_input}
    elif "生成代码" in user_input:
        return {"type": "generate_code", "details": user_input}
    elif "调用工具" in user_input:
        return {"type": "call_tool", "details": user_input}
    else:
        return {"type": "unknown", "details": user_input}
