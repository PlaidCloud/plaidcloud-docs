---
title: Alterar o idioma
description: Apresente o PlaidCloud em English (US), English (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 ou 简体中文, e faça com que a escolha o acompanhe noutros dispositivos.
sidebar:
  label: Alterar o idioma
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/change-your-language.md
---

A interface do PlaidCloud está disponível em onze idiomas:

| Idioma | Entrada do menu |
|---|---|
| Inglês (EUA) | English (US) |
| Inglês (Reino Unido) | English (UK) |
| Alemão | Deutsch |
| Espanhol | Español |
| Francês | Français |
| Português (Portugal) | Português (Portugal) |
| Português (Brasil) | Português (Brasil) |
| Polaco | Polski |
| Japonês | 日本語 |
| Coreano | 한국어 |
| Chinês (simplificado) | 简体中文 |

Todos começam em English (US). Nada muda até escolher um idioma.

## Alterar o idioma

1. No cabeçalho superior, clique no botão **Idioma**, junto ao botão **Aspeto**. O respetivo menu apresenta cada idioma com o seu próprio nome, pelo que é possível encontrar o pretendido seja qual for o idioma apresentado.
2. Escolha um idioma.
3. Uma mensagem confirma que o PlaidCloud será recarregado nesse idioma. As alterações não guardadas perdem-se, pelo que convém guardar primeiro o trabalho. Clique em **Recarregar** para continuar ou cancele para ficar como está.

O PlaidCloud guarda a escolha no perfil e recarrega no novo idioma. Para voltar atrás, escolha **English (US)** da mesma forma.

## Onde a escolha se aplica

- **Outros dispositivos e navegadores.** A escolha acompanha-o. Ao iniciar sessão na mesma área de trabalho noutro dispositivo ou navegador, aplica-se a partir do carregamento de página seguinte.
- **Por área de trabalho.** A escolha pertence ao perfil numa área de trabalho. Quem utiliza várias áreas de trabalho tem de definir o idioma em cada uma.

## Números e datas

Os números e as datas são apresentados no formato do idioma escolhido. Em alemão, por exemplo, mil duzentos e trinta e quatro e meio é apresentado como `1.234,5`. Em polaco, 1234567.89 é apresentado como `1 234 567,89` e 12 de outubro de 2026 como `12.10.2026`. Em japonês e em chinês, essa data surge como `2026/10/12` e, em coreano, como `26. 10. 12.`. English (UK) utiliza a ortografia e os formatos britânicos.

Só a apresentação muda. Os valores guardados, exportados ou enviados para integrações mantêm o formato habitual.

## Escrever em japonês, coreano e chinês

Os métodos de introdução de japonês, coreano e chinês funcionam em campos numéricos e noutros campos que limitam o que se pode escrever. Os algarismos de largura total são convertidos à medida que se escreve, pelo que `１２３` passa a `123`.

## O que mais acompanha o idioma

O texto que o PlaidCloud envia a partir do servidor também acompanha o idioma, em todos os idiomas oferecidos pelo PlaidCloud:

- **Correio eletrónico.** Mensagens do sistema, como convites, reposições de palavra-passe, avisos de fluxos de trabalho e de migração, e mensagens de inscrição, de faturação e de suporte.
- **Ecrãs de início de sessão.** Os ecrãs de início de sessão, de definição de palavra-passe e de sessão terminada, e as mensagens que o Keycloak envia a partir deles.
- **Mensagens de erro.** As mensagens que o PlaidCloud apresenta quando um pedido falha, na interface, através da API REST e através de JSON-RPC.
- **PDF de documentação do projeto.** O PDF que o PlaidCloud gera para documentar um projeto.

## Como o PlaidCloud escolhe o idioma

| Onde | Idioma utilizado |
|---|---|
| Dentro do PlaidCloud | O idioma escolhido com o botão **Idioma**. A página de início de sessão e as mensagens de correio eletrónico seguem a mesma escolha. |
| Início de sessão e outros ecrãs antes de iniciar sessão | O idioma do navegador. |
| Inscrição | O idioma do navegador. O PlaidCloud guarda-o na organização, e as mensagens de faturação e de conta enviadas à organização utilizam-no. |

Se o navegador ou o perfil utilizar um idioma que o PlaidCloud não oferece, o texto aparece em English (US). Os navegadores configurados para chinês tradicional (zh-TW ou zh-HK) recorrem a English (US) para o texto do servidor.

## O que permanece em inglês

- As mensagens e os registos de execução de fluxos de trabalho e de passos, e o fluxo de atividade. Muitas pessoas leem-nos, e mantê-los num único idioma facilita a pesquisa e garante coerência.
- O texto do assistente de IA e das ferramentas MCP.
- As mensagens de correio eletrónico escritas pelo próprio, incluindo modelos de correio eletrónico e mensagens enviadas por passos de relatório.
- A documentação OpenAPI.
- O texto de erro dos motores de SQL e de expressões.
- Os ecrãs de inscrição.
- O conteúdo criado pelo utilizador, como os nomes de projetos, tabelas e passos.
