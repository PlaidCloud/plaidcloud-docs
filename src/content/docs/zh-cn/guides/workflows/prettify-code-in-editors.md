---
title: 在编辑器中美化（格式化）代码
description: 使用“美化”按钮或 Shift+Alt+F，在 PlaidCloud 工作流步骤编辑器中自动格式化 SQL、JSON 和表达式代码。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## 在编辑器中美化代码

多个工作流步骤编辑器使用代码编辑器：SQL 步骤（Frame Extract SQL、远程执行 SQL、Remote Direct SQL、Remote Export SQL 和导入 SQL）、LLM 步骤的 **Result schema**（JSON），以及流程区域中随处可用的表达式编辑器。

这些编辑器都有一个**美化**按钮，可就地重新格式化代码，对其进行缩进并统一排版，使其更易于阅读和审查。光标位于编辑器中时，也可以按 **Shift+Alt+F**（macOS 上为 **Shift+Option+F**）。

## 格式化的内容

- **SQL**：重新排版为易读的多行布局：每个子句一行，`CASE` / `WHEN` 对齐，嵌套函数拆分展开。项目变量以及 `{variable}`、`{{ ... }}` 和 `{% ... %}` 等模板标记会被原样保留。
- **JSON**：以两个空格重新缩进（例如 LLM 步骤的 Result schema）。
- **表达式**：PlaidCloud 表达式按标准 Python 格式化：运算符和逗号周围的间距保持一致，较长的表达式会换行。

## 须知

- 美化绝不会改变代码的行为，只会改变其排版方式。SQL 关键字和标识符保持原有的大小写。
- 如果代码无法解析（存在语法错误），美化会保持代码不变并显示简短提示，因此不会丢失您的工作。
- 格式化作为单个操作应用，按 **Ctrl+Z**（macOS 上为 **Cmd+Z**）即可撤消。
