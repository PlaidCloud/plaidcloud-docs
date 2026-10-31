---
title: Panel 应用
description: 在 PlaidCloud 中构建并部署交互式 HoloViz Panel 数据应用，可以是静态的浏览器内应用，也可以是基于 git 存储库构建的服务器端应用。
sidebar:
  label: Panel 应用
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

借助 Panel 应用，您可以直接从 PlaidCloud 发布交互式 [HoloViz Panel](https://panel.holoviz.org/) 应用，其中包括参数化输入、实时图表和嵌入式数据表。您在**我的 Panel 应用**屏幕中管理它们，该屏幕列出每个应用及其运行时、构建状态和 URL。

从 [Panel Studio](/zh-cn/guides/panel-apps/studio/) 开始：选择 **新建 Studio 应用**，即可在 PlaidCloud 中从空白应用、表、视图或图库构建应用，无需设置存储库。对于定制需求，可使用下面的某个运行时发布，其显示在**运行时**列中：

- **WASM**：完全在浏览器（Pyodide）中运行的静态应用。您从文档账户发布预先构建的 HTML 文件。没有服务器进程，也无需扩缩容；它会立即提供服务。
- **服务器**：基于 git 存储库构建并在服务器端运行的应用。发布时，PlaidCloud 会将您的存储库构建为容器，该容器空闲时保持零副本，在对其 URL 的第一次请求时唤醒，提供服务（包括实时更新），并在空闲时缩减为零。对于需要 Python 运行时、服务器端计算或无法在浏览器中运行的库的应用，这是正确的选择。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="两种 Panel 应用运行时。WASM 应用是直接提供给浏览器的预构建 HTML 文件，没有服务器。服务器应用基于 git 存储库构建为容器，空闲时保持零副本，在第一次请求时约十五秒内唤醒，提供服务，并在空闲时缩减为零。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">预构建的 HTML 文件</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">浏览器 · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">立即提供服务</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">服务器</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">git 存储库</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">构建容器</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">空闲 · 0 个副本</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">无任何运行</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">首次请求</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">提供服务</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">唤醒约 15 秒</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">空闲时缩减为 0</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">两种运行时：<strong>WASM</strong> 应用是直接提供给浏览器的预构建 HTML 文件；<strong>服务器</strong>应用基于 git 构建，空闲时保持零副本，在第一次请求（约 15 秒）时唤醒，提供服务，并缩减为零。</figcaption>
</figure>

## 选择运行时

| | WASM | 服务器 |
|---|---|---|
| 来源 | 已发布的 HTML 文件 | git 存储库（连接、分支、入口点） |
| 运行位置 | 在浏览器中 | 服务器端，缩减到零 |
| 最适合 | 轻量、自包含的仪表板 | 需要服务器计算或完整 Python 库的应用 |
| 冷启动 | 无 | 第一次请求会启动应用（约 15 秒） |

## 后续步骤

- [Panel Studio](/zh-cn/guides/panel-apps/studio/)：在 PlaidCloud 中创建、编辑、预览和发布应用，无需设置存储库。
- [从 PlaidCloud Git 部署 Panel 应用](/zh-cn/guides/panel-apps/deploy-from-git/)：从存储库到已提供服务的应用的完整路径，使用无需凭据的托管连接。
- [使用 Weave 构建 Panel 应用](/zh-cn/guides/panel-apps/build-with-weave/)：描述应用，并批准 Weave 提出的具体更改。
- [创建 Panel 应用](/zh-cn/guides/panel-apps/creating/)：从空白应用、表或图库开始创建 Studio 应用，或者从 git 发布服务器应用，从文件发布 WASM 应用。
- [Panel 应用工具包](/zh-cn/guides/panel-apps/app-kit/)：构建外观与 PlaidCloud 一致、支持浅色和深色主题的应用，包含筛选器、关键数字、服务器分页数据网格、图表、表单、运行按钮、已保存设置和打印。
- [Panel 应用的数据 API](/zh-cn/guides/panel-apps/data-api/)：在服务器上筛选、分页、计数和聚合表。
- [告警和摘要](/zh-cn/guides/panel-apps/alerts-and-digests/)：当某个数字越过限值时，或按计划，获取推送通知、电子邮件、Slack 或 Teams 消息，或定期摘要。
- [应用图库](/zh-cn/guides/panel-apps/gallery/)：将应用作为模板列出，并基于已列出的应用创建新应用。
- [项目品牌和应用项目](/zh-cn/guides/panel-apps/branding/)：为项目的应用设置颜色和徽标，并将应用分配到项目。
- [使用 Panel 应用](/zh-cn/guides/panel-apps/using/)：构建状态、打开应用、编辑和删除。
- [在 Panel 应用中构建 AI 代理](/zh-cn/get-started/tutorials/panel-ai-agent/)：教程：为 AI 代理提供 REST API 作为其工具，并限定在查看者自己的权限范围内。
