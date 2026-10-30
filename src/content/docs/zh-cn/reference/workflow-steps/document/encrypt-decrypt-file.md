---
title: Encrypt File and Decrypt File 步骤
description: 在 PlaidCloud 工作流步骤中，使用 AES 或 Blowfish 加密或解密整个文档文件，或为 Excel 工作簿添加或移除密码。
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## 说明

**文档：加密文件**加密文档账户中的一个文件，并将结果写入另一个文件。**文档：解密文件**则执行相反的操作。两个步骤的设置相同。可用于接收合作伙伴发来的加密文件、在导入读取之前解密，以及在导出发往其他系统之前加密。

## 文件

| 设置 | 是否必填 | 作用 |
| --- | --- | --- |
| 源文件 | 是 | 要加密或解密的文件。 |
| 目标文件 | 是 | 要写入的文件。必须与源文件不同，以免重新运行时处理自己的输出。 |
| 目标文件写入后删除源文件 | 否 | 在目标文件安全写入后移除源文件。 |

源文件不存在不算错误：步骤会以指明该路径的警告结束，不写入任何内容，工作流继续运行。空的源文件会写出空的目标文件并给出警告；但使用 AES 或 Blowfish 加密空文件时，会写出真正的加密文件。不能使用 Smartsheet 文档账户，因为无法从中回读文件。

## 参数

| 设置 | 作用 |
| --- | --- |
| 算法 | 在加密组中：**AES-128（16 字节密钥）**、**AES-192（24 字节密钥）**、**AES-256（32 字节密钥）**、**Blowfish（4 至 56 字节密钥）** 或 **Excel 工作簿密码**。 |
| 模式 | **CBC**（默认）、**ECB** 或 **GCM**。Blowfish 仅支持 CBC 或 ECB。 |
| 密钥变量 | 保存加密密钥的工作流变量或项目变量，例如 `{aes_key}`。AES 和 Blowfish 必填。 |
| 密钥和 IV 的编码 | 密钥和 IV 的书写方式：**文本 (UTF-8)**、**十六进制**或 **Base64**。 |
| 固定 IV | 初始化向量。留空时，加密会在文件开头写入随机 IV，解密时从文件开头读回。GCM 加密始终使用随机 IV，因此 GCM 请留空。 |
| 工作簿密码变量 | 保存要为 Excel 工作簿设置或移除的密码的工作流变量或项目变量，例如 `{xlsx_password}`。**Excel 工作簿密码**必填。 |

CBC 和 ECB 使用 PKCS7 填充，GCM 会在加密数据之后添加 16 字节的认证标签。GCM 文件最大可达 256 MB。密钥或 IV 错误会使步骤报错停止，且不会留下部分写入的文件。

## 密钥存放在变量中

**密钥变量**和**工作簿密码变量**只接受变量引用，例如 `{aes_key}`，而不接受密钥或密码本身：在其中填入其他内容的步骤将无法保存。请将机密放入[工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)或项目变量中，这样只需在一处设置，并且永远不会出现在步骤、步骤版本、步骤副本或 AI 助手读回的内容中。步骤在运行时读取变量的值。**固定 IV** 是密码字段，因此其值在表单中会被隐藏。

在此规则出台之前保存了明文密钥或密码的步骤，其密钥或密码已自动移入新的项目变量（仅架构师可见），现在引用该变量。

## 相关内容

- [文档步骤](/zh-cn/reference/workflow-steps/document/)
- [管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)
