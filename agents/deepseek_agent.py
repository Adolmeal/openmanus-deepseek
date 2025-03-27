import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Optional

class DeepSeekWrapper:
    def __init__(self, model_path: str = "models/DeepSeek-V3", quantize: bool = True):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            torch_dtype=torch.bfloat16 if quantize else torch.float32,
            load_in_4bit=quantize
        )
        
    def generate_ansys_script(self, task: str, max_length: int = 2048) -> str:
        prompt = f"""基于以下需求生成ANSYS APDL脚本：
        {task}
        要求：
        1. 使用!注释说明关键步骤
        2. 包含错误处理机制
        3. 输出格式为纯代码"""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_length,
            temperature=0.7,
            top_p=0.9
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
