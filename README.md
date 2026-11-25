# python_handmake

手动写 Python 小程序的个人练习仓库，记录学习与实践过程中的代码。

## 环境准备

- Python 3.10+（本机基于 miniconda 的 Python 3.10.14）
- 项目使用虚拟环境 `.venv`，虚拟环境不入库

首次克隆本仓库后，创建并激活虚拟环境：

```bash
# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境（macOS / Linux）
source .venv/bin/activate

# 激活虚拟环境（Windows）
.venv\Scripts\activate
```

## 运行程序

```bash
# 方式一：直接使用虚拟环境解释器运行
.venv/bin/python hello.py

# 方式二：激活虚拟环境后运行
python hello.py
```

安装第三方库（先激活虚拟环境）：

```bash
pip install <库名>
```

## 代码风格与格式化

- 格式化工具：`autopep8`（已通过 `.vscode/settings.json` 配置为 Python 文件的默认格式化程序）
- 保存文件时自动格式化
- 手动格式化快捷键（macOS）：`Shift + Option + F`（整个文档）、`⌘K ⌘F`（选中代码）

## 目录结构

```
python_handmake/
├── .gitignore          # Git 忽略规则（虚拟环境、缓存等不入库）
├── .vscode/            # 编辑器配置（解释器路径、格式化程序）
├── hello.py            # 环境验证示例，可修改或删除
└── README.md           # 本文件
```
