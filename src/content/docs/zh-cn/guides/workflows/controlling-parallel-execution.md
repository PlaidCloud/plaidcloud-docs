---
title: 控制并行执行
description: 控制 PlaidCloud 工作流中的并行步骤执行，通过同时运行相互独立的步骤来优化性能。
sidebar:
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/controlling-parallel-execution.md
---

PlaidCloud 中的工作流可以作为串行步骤和并行操作的组合来执行。要将一组步骤设置为并行运行，请将这些步骤放在工作流层次结构中的一个分组内。右键单击该分组文件夹，然后选择**并行执行**选项。这样，分组内的所有步骤会同时触发并并行执行。分组内的所有步骤完成后，工作流中该分组之后的下一个步骤或分组才会激活。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="前一个步骤连接到标有“并行执行”的分组。分组内的三个转换步骤同时触发并一起运行。下一个步骤会等待，直到分组内的每个步骤都已完成。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pe-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="6" y="86" width="110" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="61" y="112" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">前一步骤</text>
  <rect x="170" y="26" width="320" height="160" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="182" y="20" font-size="12" font-weight="700" fill="var(--sl-color-accent)">并行执行</text>
  <circle cx="170" cy="108" r="6" fill="var(--sl-color-accent)" />
  <circle cx="490" cy="108" r="6" fill="var(--sl-color-accent)" />
  <rect x="210" y="42" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="63" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">转换 1</text>
  <rect x="210" y="91" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="112" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">转换 2</text>
  <rect x="210" y="140" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="161" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">转换 3</text>
  <path d="M116 108 L164 108" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 C192 108 194 59 206 59" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 L206 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 C192 108 194 157 206 157" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 59 C468 59 470 108 484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 108 L484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 157 C468 157 470 108 484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M496 108 L560 108" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pe-arrow)" />
  <rect x="562" y="86" width="112" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="618" y="105" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">下一步骤</text>
  <text x="618" y="119" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">等待全部完成</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">将相互独立的步骤分组并启用<strong>并行执行</strong>，它们会同时触发并一起运行。只有全部完成后，下一个步骤才会激活。</figcaption>
</figure>
