from setuptools import setup, find_packages

setup(
    name="acestep-prompt-generator",
    version="1.0.0",
    description="A GUI tool for generating AceStep text-to-music prompts with multi-language support",
    long_description=open("AceStep_Prompt_Generator_README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/acestep-prompt-generator",
    packages=find_packages(),
    install_requires=[
        "pypinyin>=0.55.0",
        "pyperclip>=1.8.2",
        "tkinter"  # tkinter is part of Python standard library
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Sound/Audio :: Music Synthesis",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities"
    ],
    keywords="acestep music prompt generator text-to-music",
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "acestep-generator=AceStep_Prompt_Generator:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["music_style_templates.py"],
    },
)
