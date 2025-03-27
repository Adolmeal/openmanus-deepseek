import torch
import torch.nn as nn
import torch.optim as optim
from openmanus import OpenManusModel
from deepseek import DeepSeekModel

class FusionModel(nn.Module):
    def __init__(self):
        super(FusionModel, self).__init__()
        self.openmanus = OpenManusModel()
        self.deepseek = DeepSeekModel()
        self.fc = nn.Linear(100, 1)  # 假设最终输出维度为1

    def forward(self, x):
        x1 = self.openmanus(x)
        x2 = self.deepseek(x)
        x = torch.cat((x1, x2), dim=1)
        return self.fc(x)

# 示例数据
inputs = torch.randn(100, 10)
targets = torch.randn(100, 1)

# 初始化模型、损失函数和优化器
model = FusionModel()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练循环
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

# 保存模型
torch.save(model.state_dict(), 'fusion_model.pth')
