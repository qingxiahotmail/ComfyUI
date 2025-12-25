# AceStep 音乐提示词生成器

A powerful GUI tool for generating AceStep text-to-music prompts with multi-language support and Chinese-to-Pinyin conversion.

## 🎯 功能特点

- 🎵 **10+ 音乐风格模板**：内置10种常见音乐风格，覆盖多种场景
- 🌐 **多语言支持**：支持中文、日语、韩语、英语、西班牙语、法语、德语、俄语
- 🔄 **中文自动转拼音**：输入中文，自动转换为ACE-Step模型所需的带声调拼音
- ✍️ **歌词输入**：支持主歌(Verse)和副歌(Chorus)分栏输入
- 📋 **一键生成**：自动组合风格提示词和歌词，生成符合ACE-Step格式的提示词
- 📎 **一键复制**：生成的提示词可直接复制到剪贴板
- 🎨 **友好界面**：直观的图形用户界面，易于操作
- 📦 **易于安装**：支持pip安装和命令行运行

## 🎼 支持的音乐风格

1. **合成波** - 复古未来主义风格，80年代电子音乐元素
2. **低保真** - 温暖、放松的节奏，常用于背景音乐
3. **原声** - 以原声乐器为主，自然、纯净的声音
4. **电子音乐** - 现代电子舞曲，适合派对和运动
5. **古典音乐** - 优雅、庄重的古典音乐风格
6. **爵士乐** - 即兴、摇摆的爵士乐风格
7. **摇滚** - 充满力量和激情的摇滚音乐
8. **流行音乐** - catchy、商业化的流行音乐
9. **氛围音乐** - 舒缓、沉浸式的氛围音乐
10. **乡村音乐** - 讲述故事的乡村音乐风格

## 📋 系统要求

- Python 3.8 或更高版本
- tkinter 库（通常随Python一起安装）
- pyperclip 库（用于剪贴板功能）
- pypinyin 库（用于中文转拼音功能）

## 🚀 安装和运行

### 方法一：使用 pip 安装（推荐）

```bash
# 安装最新版本
pip install acestep-prompt-generator

# 运行程序
acestep-generator
```

### 方法二：从 GitHub 克隆

```bash
# 克隆仓库
git clone https://github.com/yourusername/acestep-prompt-generator.git
cd acestep-prompt-generator

# 安装依赖
pip install -r requirements.txt

# 运行程序
python AceStep_Prompt_Generator.py
```

### 方法三：使用 Windows 启动脚本

1. 下载最新发布的 zip 文件
2. 解压到本地目录
3. 双击 `start_generator.bat` 运行

## 📖 使用说明

1. **选择音乐风格**：从下拉菜单中选择你想要的音乐风格
2. **选择语言**：为歌词选择对应的语言（中文会自动转拼音）
3. **输入歌词**：
   - 在"主歌 (Verse)"框中输入歌曲的主歌部分
   - 在"副歌 (Chorus)"框中输入歌曲的副歌部分
4. **生成提示词**：点击"生成 ComfyUI 提示词"按钮
5. **复制使用**：生成的提示词会显示在下方，点击"复制到剪贴板"即可复制到ComfyUI中使用

## 🎤 输入输出示例

### 输入

```
# 主歌
我走过深夜的街道
冷风吹乱思念的漂亮外套
你的微笑像星光很闪耀
照亮了我孤独的每分每秒

# 副歌
你是风吹过我手心
温暖的感觉像春天的雨滴
你是风包围着我的身体
深厚的爱情永远不会褪去
```

### 输出

```
lo-fi, jazz, chill hop, warm, cozy, with gentle piano & smooth bass. Soft drum beats, subtle vinyl crackle, warm reverb. Relaxed, nostalgic mood at 95 BPM. Soulful male vocals, heartfelt emotion, intimate recording.

[verse]

[zh]wo3zou3guo4shen1ye4de5jie1dao4
[zh]leng3feng1chui1luan4si1nian4de5piao4liang4wai4tao4
[zh]ni3de5wei1xiao4xiang4xing1guang1hen3xuan4yao4
[zh]zhao4liang4le5wo3gu1du2de5mei3fen1mei3miao3

[chorus]

[zh]ni3shi4feng1chui1guo4wo3shou3xin1
[zh]nuan3nuan3de5gan3jue2xiang4chun1tian1de5yu3di3
[zh]ni3shi4feng1bao4wei2zhe5wo3de5shen1ti3
[zh]shen1hou4de5ai4qing2yong3yuan3bu4hui4tui4qu4
```

## 📁 文件结构

```
acestep-prompt-generator/
├── AceStep_Prompt_Generator.py  # 主程序文件
├── music_style_templates.py     # 音乐风格模板库
├── output/
│   └── audio/                   # 音乐案例文件
├── AceStep_Prompt_Generator_README.md  # 说明文档
├── setup.py                     # 安装配置文件
├── requirements.txt             # 依赖列表
├── .gitignore                   # Git忽略文件
├── start_generator.bat          # Windows启动脚本
└── start_generator_with_pinyin.bat  # 带拼音功能的启动脚本
```

## 🎨 自定义风格模板

你可以编辑 `music_style_templates.py` 文件，添加自己的音乐风格模板：

```python
"your_style_key": {
    "name": "风格显示名称",
    "description": "风格描述",
    "prompt": "完整的风格提示词"
}
```

## 🔧 开发说明

### 安装开发依赖

```bash
pip install -r requirements.txt
```

### 运行测试

```bash
# 目前暂无单元测试，可直接运行程序进行功能测试
python AceStep_Prompt_Generator.py
```

### 构建和发布

```bash
# 构建包
python setup.py sdist bdist_wheel

# 上传到PyPI
python -m twine upload dist/*
```

## 📝 注意事项

1. 歌词输入是可选的，你可以只使用风格提示词生成纯音乐
2. 生成的提示词可以直接在ComfyUI的Text-to-Song AceStep节点中使用
3. 你可以根据需要修改生成的提示词，添加或删除元素
4. 中文歌词会自动转换为带声调的拼音，其他语言保持原样
5. 支持的语言代码：中文[zh]、日语[ja]、韩语[ko]、英语[en]、西班牙语[es]、法语[fr]、德语[de]、俄语[ru]

## 📄 许可证

本项目采用 **MIT License**，可自由使用和修改。

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建你的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📧 联系方式

如果您有任何问题或建议，欢迎通过以下方式联系：

- GitHub Issues: [https://github.com/yourusername/acestep-prompt-generator/issues](https://github.com/yourusername/acestep-prompt-generator/issues)
- Email: your.email@example.com

## 📱 相关项目

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的节点式AI图像和视频生成工具
- [ACE-Step](https://github.com/ACE-Step/ACE-Step) - 文本到音乐生成模型

---

**祝您创作愉快！🎵**

Made with ❤️ for music creators everywhere