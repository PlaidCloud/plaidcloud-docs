---
title: Aplicativos Panel
description: Crie e implante aplicativos de dados interativos HoloViz Panel no PlaidCloud — como aplicativos estáticos no navegador ou como aplicativos do lado do servidor criados a partir de um repositório git.
sidebar:
  label: Aplicativos Panel
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Os aplicativos Panel permitem publicar aplicativos interativos [HoloViz Panel](https://panel.holoviz.org/) — entradas parametrizadas, gráficos ao vivo e tabelas de dados incorporadas — diretamente do PlaidCloud. Você os gerencia na tela **Meus aplicativos Panel**, que lista todos os aplicativos junto com o tempo de execução, o status de compilação e a URL de cada um.

Há dois tempos de execução, mostrados na coluna **Tempo de execução**:

- **WASM** — um aplicativo estático que é executado inteiramente no navegador (Pyodide). Você publica um arquivo HTML pré-compilado de uma conta de documentos. Não há processo de servidor nem nada para escalar; ele é servido imediatamente.
- **Servidor** — um aplicativo criado a partir de um repositório git e executado no servidor. Ao publicar, o PlaidCloud compila seu repositório em um contêiner que fica ocioso com zero réplicas, desperta na primeira solicitação à URL dele, atende (inclusive com atualizações ao vivo) e volta a zero quando fica ocioso. Essa é a escolha certa para aplicativos que precisam de um ambiente Python, computação no servidor ou bibliotecas que não podem ser executadas no navegador.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Os dois tempos de execução do aplicativo Panel. Um aplicativo WASM é um arquivo HTML pré-compilado servido diretamente ao navegador, sem servidor. Um aplicativo de servidor é criado a partir de um repositório git em um contêiner que fica ocioso com zero réplicas, desperta na primeira solicitação em cerca de quinze segundos, atende e volta a zero quando fica ocioso." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">arquivo HTML pré-compilado</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">navegador · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">servido imediatamente</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Servidor</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">repo git</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">compilar contêiner</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">ocioso · 0 réplicas</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nada em execução</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1ª solic.</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">atendendo</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">desperta em ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">volta a 0 quando fica ocioso</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Dois tempos de execução: um aplicativo <strong>WASM</strong> é um arquivo HTML pré-compilado servido diretamente ao navegador; um aplicativo de <strong>Servidor</strong> é criado a partir do git, fica ocioso em zero, desperta na primeira solicitação (~15 s), atende e volta a zero.</figcaption>
</figure>

## Escolhendo um tempo de execução

| | WASM | Servidor |
|---|---|---|
| Origem | Um arquivo HTML publicado | Um repositório git (conexão, branch, ponto de entrada) |
| Executa | No navegador | No servidor, com escala para zero |
| Ideal para | Painéis leves e autossuficientes | Aplicativos que precisam de computação no servidor ou de bibliotecas Python completas |
| Inicialização a frio | Nenhuma | A primeira solicitação inicia o aplicativo (~15 segundos) |

## Próximas etapas

- [Implante um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) — o caminho completo do repositório até um aplicativo servido, usando uma conexão gerenciada sem credenciais.
- [Panel Studio](/pt-br/guides/panel-apps/studio/) — crie, edite, pré-visualize e publique um aplicativo no PlaidCloud, sem repositório para configurar.
- [Crie aplicativos Panel com o Weave](/pt-br/guides/panel-apps/build-with-weave/) — descreva o aplicativo e aprove a alteração exata que o Weave propõe.
- [Criando um aplicativo Panel](/pt-br/guides/panel-apps/creating/) — publique um aplicativo de servidor a partir do git ou um aplicativo WASM a partir de um arquivo.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — crie aplicativos com a aparência do PlaidCloud, em modo claro e escuro, com filtros, números de destaque, uma grade de dados paginada no servidor, gráficos, formulários, botões de execução, configurações salvas e impressão.
- [A Data API para aplicativos Panel](/pt-br/guides/panel-apps/data-api/) — filtre, pagine, conte e agregue tabelas no servidor.
- [Alertas e resumos](/pt-br/guides/panel-apps/alerts-and-digests/) — receba uma notificação push, e-mail, Slack ou mensagem do Teams quando um número ultrapassar um limite, ou um resumo agendado.
- [A galeria de aplicativos](/pt-br/guides/panel-apps/gallery/) — liste um aplicativo como modelo e crie novos aplicativos a partir dos listados.
- [Identidade visual do projeto e projetos de aplicativos](/pt-br/guides/panel-apps/branding/) — defina cores e um logotipo para os aplicativos de um projeto e atribua aplicativos a projetos.
- [Usando um aplicativo Panel](/pt-br/guides/panel-apps/using/) — status de compilação, abertura do aplicativo, edição e remoção.
- [Crie um agente de IA dentro de um aplicativo Panel](/pt-br/get-started/tutorials/panel-ai-agent/) — um tutorial: dê a um agente de IA a API REST como ferramentas, restrito às permissões do próprio visualizador.
