---
title: Convert Document Encoding
description: Convert document file encoding between character sets in a PlaidCloud workflow step to resolve encoding compatibility issues.
sidebar:
  order: 3
---

## Description



Re-encodes a text file from one character encoding to another. Useful when source files arrive in legacy encodings (Windows-1252, ISO-8859-1) but downstream tools need UTF-8, or vice-versa.

When the source file isn't UTF-8, its encoding is worked out from the file's content. A very short or highly repetitive file gives too little to go on and can be read wrongly, so check the converted output of a file like that.

A character the target encoding can't hold fails the step by default. Select **Replace characters the target encoding cannot hold with ?** to write a `?` in its place instead, as a Java writer does, and the step finishes.

A compressed file is expanded first, and each file in it is converted. For a folder, each file is written into the destination under its own name. Tick **Keep Subfolders** to write a file from a subfolder into the matching subfolder of the destination instead; the contents of a compressed file then go into the subfolder the compressed file was in. If two files would be written to the same place, the step fails before writing the second, rather than letting it replace the first, and says whether ticking **Keep Subfolders** would keep them apart.

Choose the target encoding from the step configuration. For specific encoding shortcuts, see the [UTF-8](/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/reference/workflow-steps/document/convert-document-encoding-to-utf-16/), and [ASCII](/reference/workflow-steps/document/convert-document-encoding-to-ascii/) variants.


## Examples


Create a source input, select the input file and browse for the file within that location. Select the desired output location, and browse to selected the desired location for the file. Save and run.
