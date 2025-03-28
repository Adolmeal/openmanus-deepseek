from deepseek_coder import DeepSeekCoder  # 更新为 DeepSeek-Coder 的模块
import openmanus  # 假设 OpenManus 提供功能模块

class NLPProcessor:
    def __init__(self):
        self.deepseek_model = DeepSeekCoder.load_model()  # 使用 DeepSeek-Coder 的加载方法

    def process_input(self, user_input: str):
        """
        解析用户输入并调用相应的 OpenManus 功能。
        """
        # 使用 DeepSeek-Coder 模型解析自然语言
        command = self.deepseek_model.parse(user_input)
        
        # 根据解析结果调用 OpenManus 的功能
        if command == "create_document":
            return openmanus.create_document()
        elif command == "analyze_text":
            return openmanus.analyze_text(user_input)
        else:
            return "无法识别的指令"
