---
title: Encrypt File and Decrypt File
description: Encrypt or decrypt a whole document file with AES or Blowfish, or add or remove the password of an Excel workbook, in a PlaidCloud workflow step.
sidebar:
  order: 12
---

## Description

**Document: Encrypt File** encrypts one file in a Document account and writes the result to another file. **Document: Decrypt File** does the reverse. Both steps take the same settings. Use them to receive encrypted files from a partner, decrypt them before an import reads them, and encrypt an export before it leaves for another system.

## Files

| Setting | Required | What it does |
| --- | --- | --- |
| Source File | Yes | The file to encrypt or decrypt. |
| Target File | Yes | The file to write. It must be a different file from the source, so a re-run never works on its own output. |
| Delete the source file once the target file is written | No | Removes the source file after the target file is safely written. |

A source file that isn't there isn't an error: the step finishes with a warning that names the path and writes nothing, and the workflow continues. An empty source file writes an empty target file with a warning, except that encrypting an empty file with AES or Blowfish writes a real encrypted file. A Smartsheet Document account can't be used, because files can't be read back from it.

## Parameters

| Setting | What it does |
| --- | --- |
| Cipher | **AES-128 (16-byte key)**, **AES-192 (24-byte key)**, **AES-256 (32-byte key)**, **Blowfish (4 to 56-byte key)**, or **Excel Workbook Password**. |
| Mode | **CBC** (the default), **ECB**, or **GCM**. Blowfish takes CBC or ECB only. |
| Key | The encryption key. Required for AES and Blowfish. |
| Key and IV Encoding | How the key and IV are written: **Text (UTF-8)**, **Hexadecimal**, or **Base64**. |
| Fixed IV | The initialization vector. Leave it blank and encryption starts the file with a random IV, which decryption reads back from the start of the file. GCM encryption always uses a random IV, so leave it blank for GCM. |
| Workbook Password | The password to set on, or remove from, an Excel workbook. Required for **Excel Workbook Password**. |

CBC and ECB pad with PKCS7, and GCM adds a 16-byte authentication tag after the encrypted data. A GCM file can be up to 256 MB. A wrong key or IV stops the step with an error and leaves no partial file behind.

## Keep Keys in Workflow Variables

The **Key**, **Fixed IV** and **Workbook Password** fields are password fields: their values are hidden in the form. Put the secret in a [workflow variable](/guides/workflows/manage-workflow-variables/) and enter the variable in the field, such as `{aes_key}`, so the key is set in one place and isn't typed into each step. The step reads the variable's value when it runs.

## Related

- [Document Steps](/reference/workflow-steps/document/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
