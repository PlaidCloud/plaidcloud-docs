---
title: Export to XML
description: Export data as XML files from a PlaidCloud workflow step for structured data interchange and system integration purposes.
sidebar:
  order: 11
---

## Description

Writes a PlaidCloud project table to a document account as an XML file. Use when downstream systems require XML input — common with older enterprise integrations, government filings, or specific industry data exchange formats.

The XML structure mirrors the table: one element per row, child elements for each column. For more control over the structure, use a templated approach via [Document Text Substitution](/reference/workflow-steps/document/document-text-substitution/) on a template file.

## If the File Exists

Under **If the File Exists**, **A File That Exists** (`if_exists`) decides what happens when the file is already there. **Overwrite it** (`overwrite`, default) replaces a file that is already there; **Fail the step, writing nothing** (`fail`) stops the step, writing nothing, when a file it would write already exists.
