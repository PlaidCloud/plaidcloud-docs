---
title: Workflow Loop 步骤
description: 在 PlaidCloud 工作流步骤中创建循环，遍历一组值，并对集合中的每一项重复执行步骤。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## 说明

针对数据集的每一行运行一次目标工作流，并在每次迭代之前将该行的列值设置为项目变量。当带参数的流程需要使用不同输入多次运行时，请使用它，例如“为此表中的每个业务单元运行月度结账”或“为列出的每个季度加载此报表”。

每次循环迭代看到的变量，就如同手动设置的一样，因此被调用的工作流可以使用标准的 `\{variable_name}` 语法，在表达式、筛选器、文件路径和表名称中引用它们。循环默认按顺序执行；迭代不会并行运行。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="对包含 Q1、Q2 和 Q3 行的数据集执行 Workflow Loop。每一行的列值成为项目变量，然后运行目标工作流——每行一次，按顺序执行，不并行。" style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">数据集</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">第 1 轮</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">第 2 轮</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">第 3 轮</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">按顺序——每次一轮，不并行</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">每一行的列成为项目变量，然后运行目标工作流——每行一轮，按顺序执行。如需隔离的并行扇出，请改用<a href="/zh-cn/guides/workflows/create-a-macro/">宏</a>。</figcaption>
</figure>



## 要停止的工作流


首先，从**项目**下拉菜单中选择包含每次循环要运行的工作流的项目。



接着，从**工作流**下拉菜单中选择要运行的具体工作流。

## 迭代失败时

默认情况下，循环会在第一个工作流失败的迭代处停止，且该步骤失败。在**错误处理**下，选择**失败的迭代后继续**，即使某次迭代失败，也会运行每一次迭代。每次失败以及每次迭代的结果都会保存在**循环运行状态**中，步骤结束时会给出一条警告，说明有多少次迭代失败。取消选择后，循环会在第一次失败时停止。

## 示例

示例即将推出
