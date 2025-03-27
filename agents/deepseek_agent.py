from transformers import AutoModelForCausalLM, AutoTokenizer
from openmanus.agents import BaseAgent

class DeepSeekAgent(BaseAgent):
    def __init__(self, model_path="models/DeepSeek-V3"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            device_map="auto",
            torch_dtype=torch.bfloat16  # 节省显存[citation:4][citation:10]
        )
    
    def generate(self, prompt: str, max_tokens=2048):
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
