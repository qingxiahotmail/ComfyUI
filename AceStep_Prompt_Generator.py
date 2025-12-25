import tkinter as tk
from tkinter import ttk, scrolledtext
from music_style_templates import music_style_templates
import pyperclip
from pypinyin import pinyin, Style

class AceStepPromptGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("AceStep 提示词生成器")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 设置主题
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # 主框架
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        title_label = ttk.Label(main_frame, text="AceStep 音乐提示词生成器", font=(".SF NS Text", 16, "bold"))
        title_label.pack(pady=10)
        
        # 风格选择区域
        style_frame = ttk.LabelFrame(main_frame, text="音乐风格选择", padding="10")
        style_frame.pack(fill=tk.X, pady=10)
        
        # 风格选择下拉菜单
        ttk.Label(style_frame, text="选择音乐风格:").pack(anchor=tk.W)
        self.style_var = tk.StringVar()
        self.style_combobox = ttk.Combobox(style_frame, textvariable=self.style_var, state="readonly", width=50)
        
        # 填充风格选项
        style_options = [(template["name"], key) for key, template in music_style_templates.items()]
        self.style_combobox['values'] = [opt[0] for opt in style_options]
        self.style_combobox.set(style_options[0][0])  # 默认选择第一个
        self.style_combobox.pack(fill=tk.X, pady=5)
        
        # 风格描述
        self.style_desc = scrolledtext.ScrolledText(style_frame, height=3, wrap=tk.WORD)
        self.style_desc.pack(fill=tk.X, pady=5)
        self.style_desc.insert(tk.END, music_style_templates[style_options[0][1]]["description"])
        self.style_desc.config(state=tk.DISABLED)
        
        # 绑定风格选择事件
        self.style_combobox.bind("<<ComboboxSelected>>", self.on_style_change)
        
        # 歌词输入区域
        lyrics_frame = ttk.LabelFrame(main_frame, text="歌词输入", padding="10")
        lyrics_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 主歌输入区域
        verse_section = ttk.Frame(lyrics_frame)
        verse_section.pack(fill=tk.BOTH, expand=True, pady=5)
        
        verse_header = ttk.Frame(verse_section)
        verse_header.pack(fill=tk.X)
        ttk.Label(verse_header, text="主歌 (Verse):").pack(side=tk.LEFT)
        
        # 主歌语言选择
        ttk.Label(verse_header, text="语言:").pack(side=tk.LEFT, padx=10)
        self.verse_lang_var = tk.StringVar()
        self.verse_lang_combobox = ttk.Combobox(verse_section, textvariable=self.verse_lang_var, state="readonly", width=10)
        self.verse_lang_combobox['values'] = ["中文[zh]", "日语[ja]", "韩语[ko]", "英语[en]", "西班牙语[es]", "法语[fr]", "德语[de]", "俄语[ru]"]
        self.verse_lang_combobox.set("中文[zh]")
        self.verse_lang_combobox.pack(side=tk.LEFT, padx=5)
        
        self.verse_text = scrolledtext.ScrolledText(verse_section, height=6, wrap=tk.WORD)
        self.verse_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 副歌输入区域
        chorus_section = ttk.Frame(lyrics_frame)
        chorus_section.pack(fill=tk.BOTH, expand=True, pady=5)
        
        chorus_header = ttk.Frame(chorus_section)
        chorus_header.pack(fill=tk.X)
        ttk.Label(chorus_header, text="副歌 (Chorus):").pack(side=tk.LEFT)
        
        # 副歌语言选择
        ttk.Label(chorus_header, text="语言:").pack(side=tk.LEFT, padx=10)
        self.chorus_lang_var = tk.StringVar()
        self.chorus_lang_combobox = ttk.Combobox(chorus_section, textvariable=self.chorus_lang_var, state="readonly", width=10)
        self.chorus_lang_combobox['values'] = ["中文[zh]", "日语[ja]", "韩语[ko]", "英语[en]", "西班牙语[es]", "法语[fr]", "德语[de]", "俄语[ru]"]
        self.chorus_lang_combobox.set("中文[zh]")
        self.chorus_lang_combobox.pack(side=tk.LEFT, padx=5)
        
        self.chorus_text = scrolledtext.ScrolledText(chorus_section, height=6, wrap=tk.WORD)
        self.chorus_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 生成按钮
        generate_button = ttk.Button(main_frame, text="生成 ComfyUI 提示词", command=self.generate_prompt)
        generate_button.pack(pady=10)
        
        # 输出区域
        output_frame = ttk.LabelFrame(main_frame, text="生成的提示词", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=10, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # 复制按钮
        copy_button = ttk.Button(output_frame, text="复制到剪贴板", command=self.copy_to_clipboard)
        copy_button.pack(pady=5)
        
        # 状态标签
        self.status_var = tk.StringVar()
        self.status_var.set("准备就绪")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, font=(".SF NS Text", 10))
        status_label.pack(pady=5)
    
    def on_style_change(self, event):
        """当风格选择改变时更新描述"""
        selected_name = self.style_var.get()
        
        # 查找对应的风格键
        selected_key = None
        for key, template in music_style_templates.items():
            if template["name"] == selected_name:
                selected_key = key
                break
        
        if selected_key:
            self.style_desc.config(state=tk.NORMAL)
            self.style_desc.delete(1.0, tk.END)
            self.style_desc.insert(tk.END, music_style_templates[selected_key]["description"])
            self.style_desc.config(state=tk.DISABLED)
    
    def convert_chinese_to_pinyin(self, text):
        """将中文文本转换为带声调的拼音"""
        result = []
        for word in text.split('\n'):
            if word.strip():
                pinyin_list = pinyin(word, style=Style.TONE3)
                # 将二维列表转换为带声调的拼音字符串
                pinyin_str = ''.join([item[0] for item in pinyin_list])
                result.append(pinyin_str)
            else:
                result.append('')
        return '\n'.join(result)
    
    def generate_prompt(self):
        """生成ComfyUI提示词"""
        selected_name = self.style_var.get()
        
        # 查找对应的风格键
        selected_key = None
        for key, template in music_style_templates.items():
            if template["name"] == selected_name:
                selected_key = key
                break
        
        if not selected_key:
            self.status_var.set("错误：未找到选中的风格")
            return
        
        # 获取歌词
        verse = self.verse_text.get(1.0, tk.END).strip()
        chorus = self.chorus_text.get(1.0, tk.END).strip()
        
        # 生成歌词格式
        lyrics_formatted = ""
        
        # 处理主歌
        if verse:
            lyrics_formatted += "[verse]\n\n"
            # 获取主歌语言代码
            verse_lang = self.verse_lang_var.get()
            lang_code = verse_lang[verse_lang.find('['):verse_lang.find(']')+1]  # 提取 [zh] 格式
            
            # 如果是中文，转换为带声调的拼音
            processed_verse = verse
            if lang_code == '[zh]':
                processed_verse = self.convert_chinese_to_pinyin(verse)
            
            # 为每一行添加语言代码
            for line in processed_verse.split('\n'):
                if line.strip():
                    lyrics_formatted += f"{lang_code}{line.strip()}\n"
            lyrics_formatted += "\n"
        
        # 处理副歌
        if chorus:
            lyrics_formatted += "[chorus]\n\n"
            # 获取副歌语言代码
            chorus_lang = self.chorus_lang_var.get()
            lang_code = chorus_lang[chorus_lang.find('['):chorus_lang.find(']')+1]  # 提取 [zh] 格式
            
            # 如果是中文，转换为带声调的拼音
            processed_chorus = chorus
            if lang_code == '[zh]':
                processed_chorus = self.convert_chinese_to_pinyin(chorus)
            
            # 为每一行添加语言代码
            for line in processed_chorus.split('\n'):
                if line.strip():
                    lyrics_formatted += f"{lang_code}{line.strip()}\n"
            lyrics_formatted += "\n"
        
        # 生成完整提示词
        prompt = music_style_templates[selected_key]["prompt"]
        
        # 组合最终输出
        final_output = f"""{prompt}\n\n{lyrics_formatted}"""
        
        # 显示输出
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, final_output)
        
        self.status_var.set("提示词生成完成！")
    
    def copy_to_clipboard(self):
        """复制输出到剪贴板"""
        output = self.output_text.get(1.0, tk.END).strip()
        if output:
            pyperclip.copy(output)
            self.status_var.set("已复制到剪贴板！")
        else:
            self.status_var.set("没有可复制的内容")

def main():
    """Main function to be called by entry point"""
    root = tk.Tk()
    app = AceStepPromptGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()