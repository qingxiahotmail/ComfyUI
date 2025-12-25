# 零基础ComfyUI教程：视频制作与图像生成

## 一、环境准备

### 1. 当前环境分析

根据安装报告，您的系统情况：
- **操作系统**：Windows
- **显卡**：NVIDIA Quadro P2200（支持CUDA 12.8）
- **Python版本**：3.13.3（存在兼容性问题）
- **ComfyUI状态**：已安装但启动后立即停止

### 2. 解决Python兼容性问题

ComfyUI目前与Python 3.13存在兼容性问题，推荐使用以下两种解决方案：

#### 方案一：使用Python 3.12虚拟环境

1. 下载并安装Python 3.12：
   - 访问 [Python官网](https://www.python.org/downloads/release/python-3120/)
   - 选择"Windows Installer (64-bit)"
   - 安装时务必勾选"Add Python 3.12 to PATH"

2. 创建虚拟环境：
   ```powershell
   # 打开命令提示符或PowerShell
   python3.12 -m venv comfyui_env
   comfyui_env\Scripts\activate
   ```

3. 安装依赖：
   ```powershell
   # 进入ComfyUI目录
   cd d:\ComfyUI
   
   # 安装基础依赖
   pip install -r requirements.txt
   
   # 安装PyTorch（支持CUDA 12.4）
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```

#### 方案二：使用Windows便携式版本（推荐）

1. 下载便携式版本：
   - 访问 [ComfyUI GitHub发布页](https://github.com/comfyanonymous/ComfyUI/releases/latest)
   - 下载 `ComfyUI_windows_portable_nvidia.7z`（适用于NVIDIA显卡）

2. 解压并运行：
   - 使用7-Zip或Windows资源管理器解压
   - 直接运行解压目录中的 `run_nvidia_gpu.bat`

3. 复制模型文件：
   - 将现有模型从 `d:\ComfyUI\models` 复制到便携式版本的 `models` 目录

## 二、启动ComfyUI

### 1. 使用Python 3.12虚拟环境启动

```powershell
# 激活虚拟环境
comfyui_env\Scripts\activate

# 进入ComfyUI目录
cd d:\ComfyUI

# 启动ComfyUI
python main.py
```

### 2. 验证启动成功

启动后，命令行窗口会显示：
```
Starting server
To see the GUI go to: http://127.0.0.1:8080
```

打开浏览器访问 `http://127.0.0.1:8080`，即可看到ComfyUI的Web界面。

## 三、图像生成基础教程

### 1. 了解ComfyUI界面

- **左侧面板**：节点库，包含各种功能节点
- **中间画布**：用于连接节点，构建工作流
- **右侧面板**：节点参数设置
- **底部面板**：工作流执行状态和输出

### 2. 基础图像生成工作流

#### 步骤1：添加基础节点

1. 从左侧节点库拖拽以下节点到画布：
   - `Load Checkpoint`（加载模型）
   - `CLIP Text Encode`（文本编码，添加两个）
   - `KSampler`（采样器）
   - `VAEDecode`（VAE解码）
   - `Save Image`（保存图像）

#### 步骤2：连接节点

按照以下顺序连接节点：
1. `Load Checkpoint`的`clip`输出 → 连接到两个`CLIP Text Encode`的`clip`输入
2. `Load Checkpoint`的`model`输出 → 连接到`KSampler`的`model`输入
3. `Load Checkpoint`的`vae`输出 → 连接到`VAEDecode`的`vae`输入
4. 第一个`CLIP Text Encode`的`conditioning`输出 → 连接到`KSampler`的`positive`输入
5. 第二个`CLIP Text Encode`的`conditioning`输出 → 连接到`KSampler`的`negative`输入
6. `KSampler`的`samples`输出 → 连接到`VAEDecode`的`samples`输入
7. `VAEDecode`的`images`输出 → 连接到`Save Image`的`images`输入

#### 步骤3：设置参数

1. **Load Checkpoint**：
   - 点击`ckpt_name`下拉菜单，选择`ace_step_v1_3.5b.safetensors`（或其他已安装的模型）

2. **第一个CLIP Text Encode**（正向提示词）：
   - 在`text`框中输入：`a beautiful cat sitting on a sunny windowsill, detailed fur, soft lighting, high resolution`

3. **第二个CLIP Text Encode**（反向提示词）：
   - 在`text`框中输入：`ugly, blurry, low quality, deformed, extra limbs`

4. **KSampler**：
   - `seed`：点击随机按钮生成一个随机数
   - `steps`：设置为20
   - `cfg`：设置为7.0
   - `sampler_name`：选择`euler`
   - `scheduler`：选择`normal`
   - `width`：设置为512
   - `height`：设置为512

#### 步骤4：生成图像

1. 点击画布上方的`Queue Prompt`按钮
2. 等待生成完成（进度条在底部）
3. 生成的图像会显示在底部面板，同时保存到`ComfyUI/output`目录

### 3. 图像生成案例：生成风景照

**正向提示词**：
```
a stunning mountain landscape at sunrise, snow-capped peaks, crystal clear lake, colorful sky, dramatic lighting, 8k resolution, realistic, professional photography
```

**反向提示词**：
```
flat, cartoon, low quality, blurry, overexposed, underexposed, distorted perspective
```

**参数设置**：
- 尺寸：1024×768
- 步数：30
- 采样器：dpmpp_2m_sde

## 四、视频制作基础教程

### 1. 准备视频生成模型

从目录结构看，您已经安装了Wan视频模型：
- `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`
- `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors`
- 相关LoRA模型

### 2. 基础视频生成工作流

#### 步骤1：添加视频生成节点

1. 从左侧节点库拖拽以下节点：
   - `Load Checkpoint`（加载图像模型）
   - `Load Diffusion Model`（加载视频扩散模型）
   - `Load LoRA`（加载视频LoRA）
   - `CLIP Text Encode`（文本编码，两个）
   - `KSampler (Euler)`（采样器）
   - `VAEDecode`（VAE解码）
   - `Save Video`（保存视频）

#### 步骤2：连接节点

1. `Load Checkpoint`的`clip` → 连接到两个`CLIP Text Encode`的`clip`
2. `Load Checkpoint`的`model` → 连接到`Load LoRA`的`model`
3. `Load Diffusion Model`的`model` → 连接到`Load LoRA`的`diffusion_model`
4. `Load LoRA`的`model` → 连接到`KSampler`的`model`
5. `Load LoRA`的`diffusion_model` → 连接到`KSampler`的`diffusion_model`
6. `CLIP Text Encode`的`conditioning` → 连接到`KSampler`的`positive`和`negative`
7. `KSampler`的`samples` → 连接到`VAEDecode`的`samples`
8. `VAEDecode`的`images` → 连接到`Save Video`的`images`

#### 步骤3：设置视频参数

1. **Load Diffusion Model**：
   - 选择`wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors`

2. **Load LoRA**：
   - 选择`wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`
   - `strength_model`：0.8
   - `strength_diffusion_model`：0.8

3. **KSampler**：
   - `steps`：20
   - `cfg`：7.0
   - `width`：512
   - `height`：512
   - `batch_size`：8（生成8帧）

4. **Save Video**：
   - `fps`：8（每秒8帧）

#### 步骤4：生成视频

1. 点击`Queue Prompt`按钮
2. 等待生成完成
3. 视频会保存到`ComfyUI/output`目录

### 3. 视频生成案例：生成猫咪动画

**正向提示词**：
```
a cute cat playing with a ball, smooth animation, realistic fur, soft lighting, high frame rate
```

**反向提示词**：
```
jerky animation, low quality, blurry, distorted, static image
```

**参数设置**：
- 尺寸：768×512
- 帧数：16
- FPS：12
- 采样器：euler_ancestral

## 五、进阶技巧

### 1. 使用ControlNet控制图像生成

1. 下载ControlNet模型（如canny、depth）并放入`models/controlnet`目录
2. 添加`ControlNetApply`节点和相应的预处理节点（如`Canny`）
3. 连接图像输入到预处理节点，预处理结果连接到ControlNetApply
4. ControlNetApply的输出连接到KSampler的`control`输入

### 2. 使用LoRA调整风格

1. 下载LoRA模型并放入`models/loras`目录
2. 添加`Load LoRA`节点
3. 设置适当的`strength`值（通常0.5-1.0）
4. 连接到KSampler的模型输入

### 3. 批量生成

1. 使用`BatchPromptSchedule`节点创建多个提示词
2. 设置不同的seed值
3. 一次生成多张图像

## 六、常见问题解决

### 1. 启动后无法访问Web界面

- 检查防火墙设置，允许Python访问网络
- 尝试使用`python main.py --listen 0.0.0.0`启动
- 检查端口是否被占用，使用`python main.py --port 8189`更换端口

### 2. 生成速度慢

- 确保使用GPU模式启动（`run_nvidia_gpu.bat`）
- 降低图像尺寸或帧数
- 减少采样步数

### 3. 生成结果质量差

- 尝试使用不同的模型
- 优化提示词，添加更多细节描述
- 调整CFG值（通常5-10）
- 增加采样步数

## 七、资源推荐

### 1. 模型下载网站

- [Hugging Face](https://huggingface.co/models)
- [Civitai](https://civitai.com/)
- [ModelScope](https://www.modelscope.cn/models)

### 2. 学习资源

- ComfyUI官方文档：[GitHub Wiki](https://github.com/comfyanonymous/ComfyUI/wiki)
- B站教程：搜索"ComfyUI教程"，有大量中文视频
- 社区论坛：[ComfyUI Discord](https://discord.gg/comfyui)

## 八、下一步建议

1. 从简单的图像生成开始，熟悉基本节点和工作流
2. 尝试不同的模型和提示词，观察效果差异
3. 逐步学习ControlNet、LoRA等进阶功能
4. 尝试视频生成，从短片段开始
5. 加入ComfyUI社区，学习他人的工作流

祝您使用ComfyUI创作愉快！
