---
title: 配賦の割り当て
description: コスト分割、活動基準原価計算、ITチャージバック、ドライバーベースの分配に向けて、PlaidCloudの配賦モデルを設定します。
sidebar:
  label: 概要
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/index.md
---

配賦は、ドライバーデータとルールを使って、ある行のセット（「ソース」）の値を別の行のセット（「ターゲット」）に分配します。PlaidCloudは、移転価格、ITチャージバックなどのコスト分配の課題に向けて、ルールベースのタグ付け、配賦分割、ディメンション駆動の配賦、再帰的な配賦をサポートしています。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="配賦は、ドライバーデータに比例してソースのコストプールをターゲットに分配します。1,000ドルのソースプールが使用量や人員数などのドライバーを経由し、ターゲットA、B、Cに50、30、20パーセントの割合で分割されます。再帰モデルでは、ターゲットが再び入力されて次のパスに進むことができます。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="al-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="98" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="89" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ソースプール</text>
  <text x="89" y="140" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">$1,000</text>
  <path d="M164 128 L244 128" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#al-arrow)" />
  <rect x="246" y="98" width="142" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="317" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ドライバー／基準</text>
  <text x="317" y="140" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">使用量 · 人員数…</text>
  <path d="M388 118 C450 100 452 62 496 62" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 128 L496 132" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 138 C450 156 452 202 496 202" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <text x="444" y="78" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">50%</text>
  <text x="450" y="126" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">30%</text>
  <text x="444" y="188" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">20%</text>
  <rect x="498" y="40" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="66" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ターゲットA — $500</text>
  <rect x="498" y="110" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="136" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ターゲットB — $300</text>
  <rect x="498" y="180" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="206" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ターゲットC — $200</text>
  <path d="M582 224 C582 250 90 250 89 160" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#al-arrow)" />
  <text x="330" y="248" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">再帰：ターゲットが次のパスに入力されます</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">ソースプールの値は、ドライバーデータに比例してターゲットに分割されます。再帰モデルでは、数値が収束するまで結果を再び入力して、パスを繰り返します。</figcaption>
</figure>
