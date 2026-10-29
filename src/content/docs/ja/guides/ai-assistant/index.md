---
title: AIアシスタント
description: PlaidCloud組み込みのAIアシスタントを使って、質問したり、式を生成したり、プロジェクトを自然な言葉で操作したりできます。
sidebar:
  label: AIアシスタント
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/ai-assistant/index.md
---

PlaidCloud AIアシスタントは、アプリ内のチャット機能です。データについて質問したり、ワークフローの式を生成したり、自然な言葉で操作を実行したりできます。外部のAIクライアントをテナントに接続する方法を扱う[AIエージェント（MCP）](/ja/integrations/ai-coding-agents/)とは別の機能です。

内部のしくみ（どのモデルが回答するか、検索によって回答がどのように裏付けられるか、何がアクセスを制御するか）については、[AIとLLMのアーキテクチャ](/ja/integrations/ai-architecture/)をお読みください。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 700 210" role="img" aria-label="自然な言葉でAIアシスタントに質問します。プロジェクトのスコープ内で、アシスタントはプロジェクトのデータとメタデータを検索して回答の根拠とし、回答を返します。会話は保存され、それぞれが開始されたプロジェクトに紐づきます。ただし、会話がプロジェクトに属する前の古い会話は、すべてのプロジェクトの履歴に表示されます。" style="width:100%;max-width:700px;height:auto;">
  <defs><marker id="ai-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="78" width="140" height="46" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="84" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">あなたの質問</text>
  <text x="84" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">自然言語</text>
  <path d="M154 101 L190 101" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="192" y="44" width="184" height="150" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" stroke-dasharray="6 4" />
  <text x="204" y="38" font-size="12" font-weight="700" fill="var(--sl-color-accent)">プロジェクトのスコープ</text>
  <rect x="214" y="66" width="140" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="284" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">AIアシスタント</text>
  <rect x="214" y="140" width="140" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="284" y="158" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">プロジェクトのデータとメタデータ</text>
  <text x="284" y="172" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">テーブル · ワークフロー · ディメンション</text>
  <path d="M284 140 L284 120" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ai-arrow)" />
  <text x="360" y="134" font-size="9" fill="var(--sl-color-gray-3)">検索</text>
  <path d="M376 92 L520 92" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#ai-arrow)" />
  <rect x="522" y="66" width="150" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="597" y="90" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">根拠のある回答</text>
  <text x="597" y="107" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">データを引用</text>
  <text x="284" y="205" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">会話は保存されます</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">自然な言葉で質問すると、アシスタントはプロジェクトのスコープ内でデータとメタデータを検索し、回答の根拠にします。会話は保存され、それぞれが開始されたプロジェクトに紐づきます。会話がプロジェクトに属する前の古い会話は、すべてのプロジェクトの履歴に（プロジェクトなし）と表示されます。しくみの詳細は、<a href="/ja/integrations/ai-architecture/">AIとLLMのアーキテクチャ</a>を参照してください。</figcaption>
</figure>

AIによる支援は、一部のワークフローステップにも直接組み込まれています。たとえば、平易な言葉による説明から[SQL抽出ステップのクエリを生成](/ja/guides/ai-assistant/generate-sql-extract/)できます。
