---
title: Fix File Extensionステップ
description: PlaidCloudのワークフローステップで、実際のファイルタイプを検出し、適切な拡張子に名前を変更して、ファイル拡張子を修正します。
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

ファイルの実際の内容を読み取り、拡張子と矛盾する場合は、その種類で通常使われる拡張子に名前を変更します。たとえば、`.dat` として保存されたPDFは `.pdf` になります。ソースシステムが誤った拡張子、または拡張子なしでファイルを渡してくる場合に便利です。

## 入力

- **入力ファイルまたはディレクトリ** — ドキュメントアカウント内のファイル、または含まれる各ファイルをチェックするフォルダーです。ファイルはその場で名前が変更されるため、出力先はありません。

## 動作

このステップは、各ファイルの種類を内容から判別し、現在の名前に拡張子がない場合、プレースホルダーの拡張子（`.dat`、`.tmp`、`.bin`）である場合、またはステップが認識する別の種類を示している場合にのみ、名前を変更します。

認識する種類は、PDF、画像（JPEG、PNG、GIF、TIFF、BMP、WebP、HEIC）、Excel（`.xlsx`、`.xls`）、Word（`.docx`、`.doc`）、PowerPoint（`.pptx`）のドキュメント、ZIPおよびGZipアーカイブ、そしてCSV、JSON、HTML、XML、プレーンテキストです。

次の場合、ファイルの名前は変更されません。

- 拡張子がすでに内容に適合している場合。`.jpg` と `.jpeg` はどちらもJPEGに、`.tif` と `.tiff` はどちらもTIFFに適合します。
- 拡張子がステップに認識されないもの（`.sql`、`.log`、`.ai` など）の場合。内容だけでは、SQLスクリプトとその他のテキスト、IllustratorファイルとPDFを区別できないためです。
- `.csv`、`.tsv`、`.json` などのテキスト拡張子の下に、プレーンテキストが入っている場合。
- ある形式のテキストが、別の形式の拡張子で保存されている場合（`.html` ファイル内のXML、`.json` ファイル内のCSVなど）。内容からは確実に区別できないためです。テキスト形式への名前変更の対象となるのは、`.txt` のファイル、または拡張子がない、もしくはプレースホルダーの拡張子であるファイルのみです。
- Officeドキュメントの名前が付いたZIPファイルの場合。`.xlsx`、`.docx`、`.pptx` ファイルは、内部がZIPファイルであるためです。
- 空のファイルなど、種類を判別できない場合。

アーカイブは、それ自体の内容で判断されます。中のメンバーは開かれず、名前も変更されません。名前が `.` で始まるファイルはスキップされます。

## 例

| ファイル | 内容 | 結果 |
|---|---|---|
| `invoice.dat` | PDF | `invoice.pdf` に名前を変更 |
| `photo.png` | JPEG | `photo.jpg` に名前を変更 |
| `export.txt` | CSV | `export.csv` に名前を変更 |
| `readme` | プレーンテキスト | `readme.txt` に名前を変更 |
| `query.sql` | プレーンテキスト | 変更なし |
| `budget.xlsx` | ZIP | 変更なし |

## 注記

- 入力パスが存在しない場合、またはファイルがない場合、ステップはそのパスを示す警告とともに終了して何も処理せず、ワークフローは続行されます。

## 関連項目

- [Concatenate Filesステップ](/ja/reference/workflow-steps/document/concatenate-files/)
- [ドキュメントガイド](/ja/guides/documents/)
