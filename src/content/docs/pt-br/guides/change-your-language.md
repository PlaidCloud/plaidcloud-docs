---
title: Alterar o idioma
description: Exiba o PlaidCloud em English (US), English (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 ou 简体中文, e faça sua escolha acompanhar você em outros dispositivos.
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
| Polonês | Polski |
| Japonês | 日本語 |
| Coreano | 한국어 |
| Chinês (simplificado) | 简体中文 |

Todos começam em inglês (EUA). Nada muda até você escolher um idioma.

## Alterar o idioma

1. No cabeçalho superior, clique no botão **Idioma**, ao lado do botão **Aparência**. O menu lista cada idioma pelo próprio nome, então você encontra o seu qualquer que seja o idioma exibido.
2. Escolha um idioma.
3. Uma mensagem confirma que o PlaidCloud será recarregado nesse idioma. As alterações não salvas são perdidas, então salve seu trabalho antes. Clique em **Recarregar** para continuar ou cancele para permanecer como está.

O PlaidCloud salva sua escolha no seu perfil e recarrega no novo idioma. Para voltar, escolha **English (US)** da mesma forma.

## Onde sua escolha se aplica

- **Outros dispositivos e navegadores.** Sua escolha acompanha você. Quando você entra no mesmo espaço de trabalho em outro dispositivo ou navegador, ela vale a partir do próximo carregamento de página.
- **Por espaço de trabalho.** A escolha pertence ao seu perfil em um espaço de trabalho. Se você usa vários espaços de trabalho, defina o idioma em cada um.

## Números e datas

Números e datas são exibidos no formato do idioma escolhido. Em alemão, por exemplo, mil duzentos e trinta e quatro e meio aparece como `1.234,5`. Em polonês, 1234567,89 aparece como `1 234 567,89` e 12 de outubro de 2026 como `12.10.2026`. Japonês e chinês exibem essa data como `2026/10/12`, e coreano como `26. 10. 12.`. O inglês (Reino Unido) usa a ortografia e os formatos britânicos.

Apenas a exibição muda. Os valores que você salva, exporta ou envia a integrações mantêm o formato habitual.

## Digitação em japonês, coreano e chinês

Os métodos de entrada de japonês, coreano e chinês funcionam em campos numéricos e em outros campos que limitam o que você pode digitar. Os dígitos de largura total são convertidos à medida que você digita, então `１２３` vira `123`.

## O que mais acompanha o seu idioma

O texto que o PlaidCloud envia a você a partir do servidor também segue o seu idioma, em todos os idiomas oferecidos pelo PlaidCloud:

- **E-mails.** E-mails do sistema, como convites, redefinições de senha, avisos de fluxo de trabalho e de migração, e e-mails de cadastro, cobrança e suporte.
- **Telas de login.** As telas de login, de definição de senha e de saída, e os e-mails que o Keycloak envia a partir delas.
- **Mensagens de erro.** As mensagens que o PlaidCloud exibe quando uma solicitação falha, na interface, pela API REST e por JSON-RPC.
- **PDF da documentação do projeto.** O PDF que o PlaidCloud gera para documentar um projeto.

## Como o PlaidCloud escolhe o idioma

| Onde | Idioma usado |
|---|---|
| Dentro do PlaidCloud | O idioma que você escolheu com o botão **Idioma**. Sua página de login e seus e-mails seguem a mesma escolha. |
| Login e outras telas antes de você entrar | O idioma do seu navegador. |
| Cadastro | O idioma do seu navegador. O PlaidCloud o armazena na sua organização, e os e-mails de cobrança e de conta enviados à organização o utilizam. |

Se o seu navegador ou perfil usar um idioma que o PlaidCloud não oferece, o texto aparece em inglês (EUA). Navegadores configurados para chinês tradicional (zh-TW ou zh-HK) usam o inglês (EUA) como alternativa para o texto do servidor.

## O que permanece em inglês

- Mensagens e logs de execução de fluxos de trabalho e etapas, e o fluxo de atividades. Muitas pessoas leem esses textos, e mantê-los em um único idioma os torna pesquisáveis e consistentes.
- Texto do assistente de IA e das ferramentas MCP.
- E-mails que você mesmo escreve, incluindo modelos de e-mail e e-mails enviados por etapas de relatório.
- A documentação OpenAPI.
- Texto de erro dos mecanismos de SQL e de expressões.
- As telas de cadastro.
- Conteúdo que você cria, como os nomes de projetos, tabelas e etapas.
