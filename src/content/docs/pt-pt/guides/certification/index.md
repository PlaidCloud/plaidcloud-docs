---
title: Certificação PlaidCloud
description: Obtenha emblemas PlaidCloud ao passar em laboratórios práticos classificados automaticamente — Fundamentos, depois Profissional e Especialista em cada percurso, e Master por revisão.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/index.md
---

A certificação PlaidCloud comprova o que sabe fazer através de laboratórios práticos. Cada laboratório dá-lhe um projeto onde trabalhar e uma tarefa, e classifica automaticamente o seu trabalho quando o submete. Não há exames para marcar nem cursos em que se inscrever: prepara-se lendo, por ordem, os guias que cada [percurso de aprendizagem](#percursos-de-aprendizagem) lista.

## Níveis e percursos

| Nível | Percurso | Como o obtém |
|---|---|---|
| **Fundamentos** | Sem percurso | Passar no laboratório de Fundamentos |
| **Profissional** | **Engenharia de dados**, **Modelação** ou **Análise** | Passar no laboratório de Profissional do percurso |
| **Especialista** | **Engenharia de dados**, **Modelação** ou **Análise** | Passar no laboratório de Especialista do percurso, que tem limite de tempo |
| **Master** | Sem percurso | Ter três emblemas de Especialista e passar numa revisão, pelo PlaidCloud, de uma implementação em produção |

Os percursos **Operações financeiras** e **Administração e segurança** estão indicados como **Em breve**. Ainda não têm laboratórios.

Em cada percurso, o seu emblema de Especialista aparece no lugar do emblema de Profissional.

## Abrir as Certificações

Abra o menu do utilizador no canto superior direito e escolha **Certificações**. O painel abre no separador Início com:

- uma faixa com o seu objetivo, quando um administrador da área de trabalho definiu um, a indicar se já tem esse emblema;
- **Os seus emblemas**, com a data em que obteve cada emblema e a data em que expira;
- **Laboratórios**, uma grelha de cada percurso por **Fundamentos**, **Profissional** e **Especialista**. Cada célula mostra **Iniciar laboratório**, **Obtido** para um emblema que tem, ou, na área de trabalho de certificação, a data em que o laboratório volta a estar disponível após uma [espera](#a-espera-de-7-dias). A linha do seu objetivo está marcada com **o seu objetivo**, e um objetivo de Fundamentos ou Master marca **Todos os percursos**;
- **Master**, com quantos dos três emblemas de Especialista tem;
- **Guia de certificação ›**, que abre este guia.

**Voltar ao início** fecha o painel.

## A área de trabalho de certificação

Os laboratórios são executados apenas na área de trabalho de certificação do PlaidCloud. Em qualquer outra área de trabalho, **Iniciar laboratório** adiciona-o à área de trabalho de certificação como membro que pode construir, com o mesmo endereço de correio eletrónico, e abre-a num novo separador no respetivo painel **Certificações**. Escolha novamente **Iniciar laboratório** aí para iniciar o laboratório.

À primeira vez, o PlaidCloud envia-lhe uma mensagem de correio eletrónico para definir uma palavra-passe para a área de trabalho de certificação. Verifique a sua caixa de entrada.

Se não pertencer a nenhuma área de trabalho PlaidCloud, contacte o PlaidCloud e convidamo-lo para a área de trabalho de certificação.

Iniciar um laboratório, abandonar um e obter um emblema exigem todos um endereço de correio eletrónico verificado, porque os seus emblemas pertencem-lhe. Em qualquer outra área de trabalho, **Iniciar laboratório** exige que o seu endereço de correio eletrónico esteja verificado nessa área de trabalho. Aí, **Iniciar laboratório** e **Partilhar a partir da área de trabalho de certificação** abrem a área de trabalho de certificação apenas um número limitado de vezes por dia para cada endereço de correio eletrónico; depois disso, tente novamente no dia seguinte.

## Como funciona um laboratório

1. Escolha **Iniciar laboratório** na área de trabalho de certificação. O PlaidCloud cria o projeto do laboratório para si; só você o pode abrir.
2. O painel mostra o laboratório: o título, quando o iniciou, **A sua tarefa**, e **Submeter para classificação**, **Abrir projeto** e **Abandonar**. Enquanto um laboratório está aberto, o painel mostra-o em vez dos seus emblemas e da grelha.
3. Escolha **Abrir projeto** e execute a tarefa.
4. Escolha **Submeter para classificação**. A classificação executa o fluxo de trabalho do laboratório e depois verifica o que essa execução produziu, pelo que pode demorar tanto como a execução. É executada em segundo plano: o painel mostra **A avaliar o seu laboratório** e verifica o resultado, e **Submeter para classificação** e **Abandonar** ficam indisponíveis até a classificação terminar. Pode sair do painel, ou do PlaidCloud, enquanto classifica; quando abrir **Certificações** novamente, continua a aguardar o resultado ou mostra-o, se a classificação já tiver terminado. Se o painel não conseguir contactar o servidor durante uma classificação demorada, acrescenta *Não é possível contactar o servidor; a tentar novamente…* e continua a verificar.
   - Se todas as verificações passarem, o emblema é seu e o projeto do laboratório é eliminado.
   - Se alguma verificação falhar, **Último resultado** lista cada verificação como **Aprovado** ou **Falhou**. Uma verificação falhada indica o que estava errado e tem uma ligação **Guia ›** para o guia que a aborda. Corrija o seu projeto e submeta novamente.

Pode submeter as vezes que quiser enquanto o laboratório estiver aberto. Submeter enquanto o fluxo de trabalho do laboratório já está em execução não classifica nada; aguarde que a execução termine e submeta novamente. Se a classificação parar antes de terminar, **Último resultado** indica-o; submeta novamente.

Se todas as verificações passarem mas o seu endereço de correio eletrónico não estiver verificado, não é atribuído nenhum emblema. Verifique o seu endereço de correio eletrónico e submeta novamente.

### Limites de tempo

Os laboratórios de Especialista têm limite de tempo: a grelha **Laboratórios** mostra **Com limite de tempo · 4 h**, e um laboratório de Especialista aberto mostra quantos minutos restam. O relógio começa quando inicia o laboratório e continua a contar quer esteja a trabalhar nele ou não.

Uma submissão feita antes de o tempo terminar é classificada mesmo que a classificação termine depois. Se essa classificação parar antes de terminar, ou se todas as verificações passarem mas ainda não for possível atribuir nenhum emblema, pode submeter novamente durante pelo menos um dia depois de o tempo terminar.

Caso contrário, terminado o tempo, já não é possível passar no laboratório. A sua próxima submissão termina a tentativa, elimina o projeto do laboratório e inicia a espera de 7 dias. Se não submeter novamente, a limpeza noturna do PlaidCloud termina a tentativa da mesma forma.

Os laboratórios de Fundamentos e de Profissional não têm limite de tempo.

### A espera de 7 dias

**Abandonar** elimina o projeto do laboratório e termina a tentativa. Confirma-o primeiro. Se não for possível eliminar um projeto de laboratório quando a tentativa termina, quer passe, o abandone ou esgote o tempo, uma mensagem indica-o se o painel estiver aberto, e a limpeza noturna elimina-o mais tarde. Abandonar um laboratório, ou esgotar o tempo num laboratório de Especialista, inicia uma espera de 7 dias antes de poder iniciar esse laboratório novamente; a grelha **Laboratórios** mostra a data em que volta a estar disponível. Submeter um laboratório em que algumas verificações falham não inicia uma espera.

## Expiração

Os emblemas expiram dois anos depois de os obter. Um emblema expirado deixa de aparecer em **Os seus emblemas** ou para os administradores, e o respetivo laboratório pode ser iniciado novamente, a menos que ainda tenha um emblema superior no mesmo percurso.

## Master

Master é o único emblema que não se obtém num laboratório. Exige três emblemas de Especialista que não tenham expirado e uma implementação em produção, revista pelo PlaidCloud.

**Pedir revisão Master**, no cartão **Master**, fica disponível quando tem três emblemas de Especialista. Abre **Ajuda e suporte** com um novo pedido que já indica os seus emblemas de Especialista. Adicione os detalhes da sua implementação e envie-o. A revisão procura:

- uma implementação que esteja em produção num cliente ou parceiro identificado;
- que a tenha construído ou liderado;
- que utilize a capacidade de pelo menos dois percursos;
- um contacto identificado que a confirme.

O emblema Master também expira dois anos depois de ser concedido.

## Partilhar um emblema

Cada emblema tem a sua própria página pública de verificação, que mostra o emblema, o seu nome, quando foi emitido, quando expira e se ainda é válido. O nome é o do seu perfil na área de trabalho de certificação quando torna o emblema público; se o PlaidCloud aí criou a sua conta quando iniciou um laboratório, é a parte do seu endereço de correio eletrónico antes do @. Para mostrar um nome alterado, torne o emblema privado e depois público novamente. A página nunca mostra o seu endereço de correio eletrónico completo. A página só existe enquanto o emblema for público.

Na área de trabalho de certificação, sob cada emblema em **Os seus emblemas**:

- **Tornar público** publica a página de verificação do emblema. Desmarque-o para retirar a página.
- **Copiar ligação** copia o endereço da página.
- **Adicionar ao LinkedIn** abre o formulário do LinkedIn para adicionar uma certificação, preenchido a partir do emblema.

**Copiar ligação** e **Adicionar ao LinkedIn** só funcionam enquanto o emblema for público. Em qualquer outra área de trabalho, um emblema público mantém **Copiar ligação** e **Adicionar ao LinkedIn**, e um emblema que não é público oferece **Partilhar a partir da área de trabalho de certificação**, que abre a área de trabalho de certificação no respetivo painel **Certificações**.

Partilhar exige um endereço de correio eletrónico verificado. Enquanto o seu não for verificado, **Os seus emblemas** não lista nenhum.

## O que os administradores veem

Os emblemas pertencem ao seu endereço de correio eletrónico, pelo que aparecem em todas as áreas de trabalho de que é membro com esse endereço. Na lista **Membros** de uma área de trabalho, os administradores veem os emblemas e o objetivo de cada membro e podem atribuir um percurso-alvo. Veem emblemas, não tentativas nem resultados de laboratórios, e um membro cujo endereço de correio eletrónico não esteja verificado não mostra nenhum emblema. Os agentes de IA ligados por MCP podem ler os emblemas e os objetivos dos membros da mesma forma. Consulte [Emblemas de certificação e objetivos](/pt-pt/administration/access/member-management/#emblemas-de-certificação-e-objetivos).

## Percursos de aprendizagem

- [Fundamentos](/pt-pt/guides/certification/foundations/)
- [Engenharia de dados](/pt-pt/guides/certification/data-engineering/)
- [Modelação](/pt-pt/guides/certification/modeling/)
- [Análise](/pt-pt/guides/certification/analytics/)
