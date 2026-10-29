---
title: Aplicações Panel
description: Crie e implemente aplicações de dados interativas HoloViz Panel no PlaidCloud — como aplicações estáticas executadas no navegador ou como aplicações do lado do servidor compiladas a partir de um repositório git.
sidebar:
  label: Aplicações Panel
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

As aplicações Panel permitem-lhe publicar aplicações interativas [HoloViz Panel](https://panel.holoviz.org/) — entradas parametrizadas, gráficos em direto e tabelas de dados incorporadas — diretamente a partir do PlaidCloud. Gere-as no ecrã **As minhas aplicações Panel**, que lista todas as aplicações com o respetivo tempo de execução, estado de compilação e URL.

Existem dois tempos de execução, apresentados na coluna **Tempo de execução**:

- **WASM** — uma aplicação estática que é executada inteiramente no navegador (Pyodide). Publica um ficheiro HTML pré-compilado a partir de uma conta de documentos. Não há processo de servidor nem nada a escalar; é disponibilizada imediatamente.
- **Servidor** — uma aplicação compilada a partir de um repositório git e executada no servidor. Ao publicar, o PlaidCloud compila o seu repositório num contentor que fica inativo com zero réplicas, acorda no primeiro pedido ao seu URL, disponibiliza a aplicação (incluindo atualizações em direto) e volta a zero quando está inativo. É a escolha certa para aplicações que precisam de um ambiente de execução Python, de computação no servidor ou de bibliotecas que não podem ser executadas no navegador.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Os dois tempos de execução das aplicações Panel. Uma aplicação WASM é um ficheiro HTML pré-compilado disponibilizado diretamente ao navegador, sem servidor. Uma aplicação de servidor é compilada a partir de um repositório git num contentor que fica inativo com zero réplicas, acorda no primeiro pedido em cerca de quinze segundos, disponibiliza a aplicação e volta a zero quando está inativo." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ficheiro HTML pré-compilado</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">navegador · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">disponibilizada de imediato</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Servidor</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">repo git</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">compilar contentor</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">inativo · 0 réplicas</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nada em execução</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1.º pedido</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">a disponibilizar</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">acorda em ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">volta a 0 quando está inativo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Dois tempos de execução: uma aplicação <strong>WASM</strong> é um ficheiro HTML pré-compilado disponibilizado diretamente ao navegador; uma aplicação de <strong>servidor</strong> é compilada a partir do git, fica inativa a zero, acorda no primeiro pedido (~15 s), disponibiliza a aplicação e volta a zero.</figcaption>
</figure>

## Escolher um tempo de execução

| | WASM | Servidor |
|---|---|---|
| Origem | Um ficheiro HTML publicado | Um repositório git (ligação, ramo, ponto de entrada) |
| Executa | No navegador | No servidor, com escala a zero |
| Ideal para | Painéis de controlo leves e autónomos | Aplicações que precisam de computação no servidor ou de bibliotecas Python completas |
| Arranque a frio | Nenhum | O primeiro pedido arranca a aplicação (~15 segundos) |

## Passos seguintes

- [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) — o percurso completo desde o repositório até uma aplicação disponibilizada, com uma ligação gerida sem credenciais.
- [Panel Studio](/pt-pt/guides/panel-apps/studio/) — crie, edite, pré-visualize e publique uma aplicação no PlaidCloud, sem repositório para configurar.
- [Criar aplicações Panel com o Weave](/pt-pt/guides/panel-apps/build-with-weave/) — descreva a aplicação e aprove a alteração exata que o Weave propõe.
- [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/) — publique uma aplicação de servidor a partir do git, ou uma aplicação WASM a partir de um ficheiro.
- [O Panel App Kit](/pt-pt/guides/panel-apps/app-kit/) — crie aplicações com o aspeto do PlaidCloud, nos modos claro e escuro, com filtros, números de destaque, uma grelha de dados paginada no servidor, gráficos, formulários, botões de execução, definições guardadas e impressão.
- [A Data API para aplicações Panel](/pt-pt/guides/panel-apps/data-api/) — filtre, pagine, conte e agregue tabelas no servidor.
- [Alertas e resumos](/pt-pt/guides/panel-apps/alerts-and-digests/) — receba uma notificação push, uma mensagem de correio eletrónico, Slack ou Teams quando um número ultrapassa um limite, ou um resumo agendado.
- [A galeria de aplicações](/pt-pt/guides/panel-apps/gallery/) — liste uma aplicação como modelo e crie novas aplicações a partir das listadas.
- [Identidade visual do projeto e projetos das aplicações](/pt-pt/guides/panel-apps/branding/) — defina cores e um logótipo para as aplicações de um projeto e atribua aplicações a projetos.
- [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) — estado da compilação, abertura da aplicação, edição e remoção.
- [Criar um agente de IA dentro de uma aplicação Panel](/pt-pt/get-started/tutorials/panel-ai-agent/) — um tutorial: dê a um agente de IA a API REST como ferramentas, limitadas às permissões do próprio visualizador.
