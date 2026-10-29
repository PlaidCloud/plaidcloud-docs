---
title: Convert Document Encoding 步骤
description: 在 PlaidCloud 工作流步骤中在字符集之间转换文档文件编码，以解决编码兼容性问题。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## 说明



将文本文件从一种字符编码重新编码为另一种。当源文件以旧版编码（Windows-1252、ISO-8859-1）到达，而下游工具需要 UTF-8，或反过来时很有用。

当源文件不是 UTF-8 时，会根据文件内容推断其编码。非常短或高度重复的文件提供的信息过少，可能被误读，因此对这类文件请检查转换后的输出。

默认情况下，目标编码无法容纳的字符会使步骤失败。选择**将目标编码无法表示的字符替换为 ?**，则会改为在其位置写入 `?`（与 Java 写入器的做法相同），步骤即可完成。

请在步骤配置中选择目标编码。若需特定编码的快捷方式，请参阅 [UTF-8](/zh-cn/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)、[UTF-16](/zh-cn/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) 和 [ASCII](/zh-cn/reference/workflow-steps/document/convert-document-encoding-to-ascii/) 变体。


## 示例


创建源输入，选择输入文件，并在该位置中浏览找到文件。选择所需的输出位置，并浏览选择文件的所需位置。保存并运行。
