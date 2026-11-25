---
title: Certificação PlaidCloud
description: Conquiste selos PlaidCloud passando em laboratórios práticos avaliados automaticamente — Fundamentos, depois Profissional e Especialista em cada trilha, e Master por revisão.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/index.md
---

A certificação PlaidCloud comprova o que você sabe fazer com laboratórios práticos. Cada laboratório dá a você um projeto para trabalhar e uma tarefa, e avalia seu trabalho automaticamente quando você o envia. Não há provas para agendar nem cursos para se matricular: você se prepara lendo, em ordem, os guias que cada [trilha de aprendizagem](#trilhas-de-aprendizagem) lista.

## Níveis e trilhas

| Nível | Trilha | Como conquistar |
|---|---|---|
| **Fundamentos** | Sem trilha | Passe no laboratório Fundamentos |
| **Profissional** | **Engenharia de dados**, **Modelagem** ou **Análise** | Passe no laboratório Profissional da trilha |
| **Especialista** | **Engenharia de dados**, **Modelagem** ou **Análise** | Passe no laboratório Especialista da trilha, que tem tempo limitado |
| **Master** | Sem trilha | Tenha três selos Especialista e passe em uma revisão do PlaidCloud de uma implementação em produção |

As trilhas **Operações financeiras** e **Administração e segurança** aparecem como **Em breve**. Elas ainda não têm laboratórios.

Em cada trilha, seu selo Especialista aparece no lugar do selo Profissional.

## Abrir Certificações

Abra o menu do usuário no canto superior direito e escolha **Certificações**. O painel abre na sua guia Início com:

- um banner com seu alvo, quando um administrador do espaço de trabalho definiu um, informando se você já tem esse selo;
- **Seus selos**, com a data em que você conquistou cada selo e a data em que ele expira;
- **Laboratórios**, uma grade de cada trilha em relação a **Fundamentos**, **Profissional** e **Especialista**. Cada célula mostra **Iniciar laboratório**, **Conquistado** para um selo que você tem, ou, no espaço de trabalho de certificação, a data em que o laboratório fica disponível novamente após uma [espera](#a-espera-de-7-dias). A linha do seu alvo é marcada com **seu alvo**, e um alvo Fundamentos ou Master marca **Todas as trilhas**;
- **Master**, com quantos dos três selos Especialista você tem;
- **Guia de certificação ›**, que abre este guia.

**Voltar ao início** fecha o painel.

## O espaço de trabalho de certificação

Os laboratórios são executados somente no espaço de trabalho de certificação do PlaidCloud. Em qualquer outro espaço de trabalho, **Iniciar laboratório** adiciona você ao espaço de trabalho de certificação como um membro que pode construir, com o mesmo endereço de e-mail, e o abre em uma nova guia, no próprio painel **Certificações**. Escolha **Iniciar laboratório** novamente ali para iniciar o laboratório.

Na primeira vez, o PlaidCloud envia a você um e-mail para definir uma senha para o espaço de trabalho de certificação. Verifique sua caixa de entrada.

Se você não pertence a nenhum espaço de trabalho do PlaidCloud, entre em contato com o PlaidCloud, e nós convidamos você para o espaço de trabalho de certificação.

Iniciar um laboratório, abandoná-lo e conquistar um selo exigem um endereço de e-mail verificado, porque seus selos pertencem a ele. Em qualquer outro espaço de trabalho, **Iniciar laboratório** exige que seu endereço de e-mail esteja verificado nesse espaço de trabalho. Nele, **Iniciar laboratório** e **Compartilhar a partir do espaço de trabalho de certificação** abrem o espaço de trabalho de certificação um número limitado de vezes por dia para cada endereço de e-mail; depois disso, tente novamente no dia seguinte.

## Como um laboratório funciona

1. Escolha **Iniciar laboratório** no espaço de trabalho de certificação. O PlaidCloud cria o projeto do laboratório para você; somente você pode abri-lo.
2. O painel mostra o laboratório: seu título, quando você o iniciou, **Sua tarefa**, e **Enviar para avaliação**, **Abrir projeto** e **Abandonar**. Enquanto um laboratório está aberto, o painel o mostra no lugar dos seus selos e da grade.
3. Escolha **Abrir projeto** e faça a tarefa.
4. Escolha **Enviar para avaliação**. A avaliação executa o fluxo de trabalho do laboratório e depois verifica o que essa execução produziu, portanto pode levar o tempo da execução. Ela é executada em segundo plano: o painel mostra **Avaliando seu laboratório** e verifica o resultado, e **Enviar para avaliação** e **Abandonar** ficam indisponíveis até a avaliação terminar. Você pode sair do painel, ou do PlaidCloud, enquanto ela é avaliada; quando você abrir **Certificações** novamente, ele continua aguardando o resultado ou o exibe, se a avaliação já tiver terminado. Se o painel não conseguir acessar o servidor durante uma avaliação longa, ele acrescenta *Não foi possível conectar ao servidor; tentando novamente…* e continua verificando.
   - Se todas as verificações passarem, o selo é seu, e o projeto do laboratório é excluído.
   - Se alguma verificação falhar, **Último resultado** lista cada verificação como **Aprovado** ou **Falhou**. Uma verificação reprovada diz o que estava errado e tem um link **Guia ›** para o guia que trata do assunto. Corrija seu projeto e envie novamente.

Você pode enviar quantas vezes quiser enquanto o laboratório estiver aberto. Enviar enquanto o fluxo de trabalho do laboratório já está em execução não avalia nada; espere a execução terminar e envie novamente. Se a avaliação parar antes de terminar, **Último resultado** informa isso; envie novamente.

Se todas as verificações passarem, mas seu endereço de e-mail não estiver verificado, nenhum selo é concedido. Verifique seu endereço de e-mail e envie novamente.

### Limites de tempo

Os laboratórios Especialista têm tempo limitado: a grade **Laboratórios** mostra **Com tempo limitado · 4 h**, e um laboratório Especialista aberto mostra quantos minutos restam. O relógio começa quando você inicia o laboratório e continua correndo, quer você esteja trabalhando nele ou não.

Um envio feito antes de o tempo acabar é avaliado mesmo que a avaliação termine depois dele. Se essa avaliação parar antes de terminar, ou se todas as verificações passarem mas nenhum selo puder ser concedido ainda, você ainda pode enviar novamente por pelo menos um dia depois que o tempo acabar.

Caso contrário, esgotado o tempo, o laboratório não pode mais ser aprovado. Seu próximo envio encerra a tentativa, exclui o projeto do laboratório e inicia a espera de 7 dias. Se você não enviar novamente, a limpeza noturna do PlaidCloud encerra a tentativa da mesma forma.

Os laboratórios Fundamentos e Profissional não têm limite de tempo.

### A espera de 7 dias

**Abandonar** exclui o projeto do laboratório e encerra a tentativa. Você o confirma antes. Se o projeto de um laboratório não puder ser excluído quando a tentativa terminar, seja porque você passou, abandonou ou esgotou o tempo, uma mensagem informa isso se o painel estiver aberto, e a limpeza noturna o exclui depois. Abandonar um laboratório, ou esgotar o tempo em um laboratório Especialista, inicia uma espera de 7 dias antes de você poder iniciar esse laboratório novamente; a grade **Laboratórios** mostra a data em que ele fica disponível novamente. Enviar um laboratório que falha em algumas verificações não inicia uma espera.

## Expiração

Os selos expiram dois anos depois de conquistados. Um selo expirado deixa de aparecer em **Seus selos** ou para os administradores, e seu laboratório pode ser iniciado novamente, a menos que você ainda tenha um selo superior na mesma trilha.

## Master

Master é o único selo que não é conquistado em um laboratório. Ele exige três selos Especialista que não tenham expirado e uma implementação em produção, revisada pelo PlaidCloud.

**Solicitar revisão Master**, no cartão **Master**, fica disponível quando você tem três selos Especialista. Ele abre **Ajuda e suporte** com um novo ticket que já cita seus selos Especialista. Adicione os detalhes da sua implementação e envie. A revisão procura:

- uma implementação que esteja em produção em um cliente ou parceiro identificado;
- que você a tenha construído ou liderado;
- que ela use a capacidade de pelo menos duas trilhas;
- um contato identificado que a confirme.

O selo Master também expira dois anos depois de concedido.

## Compartilhar um selo

Cada selo tem a própria página pública de verificação, que mostra o selo, seu nome, quando foi emitido, quando expira e se ainda é válido. O nome é o do seu perfil no espaço de trabalho de certificação quando você torna o selo público; se o PlaidCloud criou sua conta lá quando você iniciou um laboratório, é a parte do seu endereço de e-mail antes do @. Para mostrar um nome alterado, torne o selo privado e depois público novamente. A página nunca mostra seu endereço de e-mail inteiro. A página existe somente enquanto o selo é público.

No espaço de trabalho de certificação, sob cada selo em **Seus selos**:

- **Tornar público** publica a página de verificação do selo. Desmarque para tirar a página do ar.
- **Copiar link** copia o endereço da página.
- **Adicionar ao LinkedIn** abre o formulário do LinkedIn para adicionar uma certificação, preenchido a partir do selo.

**Copiar link** e **Adicionar ao LinkedIn** funcionam somente enquanto o selo é público. Em qualquer outro espaço de trabalho, um selo público mantém **Copiar link** e **Adicionar ao LinkedIn**, e um selo que não é público oferece **Compartilhar a partir do espaço de trabalho de certificação**, que abre o espaço de trabalho de certificação no painel **Certificações**.

Compartilhar exige um endereço de e-mail verificado. Até que o seu seja verificado, **Seus selos** não lista nenhum.

## O que os administradores veem

Os selos pertencem ao seu endereço de e-mail, portanto aparecem em todos os espaços de trabalho em que você é membro com esse endereço. Na lista **Membros** de um espaço de trabalho, os administradores veem os selos e o alvo de cada membro e podem atribuir uma trilha-alvo. Eles veem selos, não tentativas ou resultados de laboratórios, e um membro cujo endereço de e-mail não está verificado não mostra nenhum selo. Agentes de IA conectados por MCP podem ler os selos e os alvos dos membros da mesma forma. Consulte [Selos de certificação e alvos](/pt-br/administration/access/member-management/#selos-de-certificação-e-alvos).

## Trilhas de aprendizagem

- [Fundamentos](/pt-br/guides/certification/foundations/)
- [Engenharia de dados](/pt-br/guides/certification/data-engineering/)
- [Modelagem](/pt-br/guides/certification/modeling/)
- [Análise](/pt-br/guides/certification/analytics/)
