---
title: Fix File Extension 步骤
description: 在 PlaidCloud 工作流步骤中，通过检测文件的实际类型并使用正确的扩展名重命名，来更正文件扩展名。
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

读取文件的实际内容，当内容与其扩展名不符时，将其重命名为该类型通常使用的扩展名，例如保存为 `.dat` 的 PDF 会变为 `.pdf`。当源系统交付的文件扩展名有误或缺失时，此步骤很有用。

## 输入

- **输入文件或目录** — 文档账户中的一个文件，或其中每个文件都会被检查的文件夹。文件就地重命名，因此没有输出位置。

## 工作方式

步骤根据内容识别每个文件的类型，仅当文件当前名称缺少扩展名、使用占位扩展名（`.dat`、`.tmp` 或 `.bin`），或者指向步骤能识别的另一种类型时，才会重命名该文件。

它能识别的类型包括：PDF；JPEG、PNG、GIF、TIFF、BMP、WebP 和 HEIC 图像；Excel（`.xlsx`、`.xls`）、Word（`.docx`、`.doc`）和 PowerPoint（`.pptx`）文档；ZIP 和 GZip 归档；以及 CSV、JSON、HTML、XML 和纯文本。

在以下情况下，文件保留其名称：

- 扩展名已与内容相符 — `.jpg` 和 `.jpeg` 都适用于 JPEG，`.tif` 和 `.tiff` 适用于 TIFF；
- 扩展名是步骤无法识别的，例如 `.sql`、`.log` 或 `.ai`，因为仅凭内容无法将 SQL 脚本与其他文本区分开，也无法将 Illustrator 文件与 PDF 区分开；
- 文件内容为纯文本，且使用 `.csv`、`.tsv` 或 `.json` 等文本扩展名；
- 文件内容为某种文本格式，却使用另一种文本格式的扩展名 — 例如 `.html` 文件中的 XML、`.json` 文件中的 CSV — 因为仅凭内容无法可靠地区分它们。只有 `.txt` 文件，或没有扩展名或使用占位扩展名的文件，才会被重命名为某种文本格式；
- 文件是以 Office 文档命名的 ZIP 文件，因为 `.xlsx`、`.docx` 和 `.pptx` 文件本质上是 ZIP 文件；
- 无法确定其类型，例如空文件。

归档按其自身内容判断：不会打开或重命名其中的成员。名称以 `.` 开头的文件会被跳过。

## 示例

| 文件 | 内容 | 结果 |
|---|---|---|
| `invoice.dat` | PDF | 重命名为 `invoice.pdf` |
| `photo.png` | JPEG | 重命名为 `photo.jpg` |
| `export.txt` | CSV | 重命名为 `export.csv` |
| `readme` | 纯文本 | 重命名为 `readme.txt` |
| `query.sql` | 纯文本 | 不变 |
| `budget.xlsx` | ZIP | 不变 |

## 备注

- 如果输入路径不存在或其中没有文件，步骤会以指明该路径的警告结束，不处理任何内容，工作流继续运行。

## 相关内容

- [Concatenate Files 步骤](/zh-cn/reference/workflow-steps/document/concatenate-files/)
- [文档指南](/zh-cn/guides/documents/)
