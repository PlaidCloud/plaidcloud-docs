---
title: "Copiar e colar etapas"
description: Copie e cole etapas de fluxo de trabalho entre fluxos de trabalho do PlaidCloud para reutilizar configurações de etapas e acelerar o desenvolvimento de fluxos de trabalho.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/copy-paste-steps.md
---

## Copiar etapas


Muitas vezes é útil copiar etapas em vez de começar do zero a cada vez. O PlaidCloud permite copiar etapas dentro de um fluxo de trabalho, entre fluxos de trabalho e até para outros projetos. Você pode selecionar várias etapas para copiar de uma só vez. Selecione as etapas do fluxo de trabalho na hierarquia e clique no botão **Copiar etapas selecionadas** na parte superior da tabela.



Isso coloca as etapas selecionadas na área de transferência e permite colá-las no fluxo de trabalho atual ou em outro.

A área de transferência fica armazenada no seu navegador, portanto sobrevive ao recarregamento da página e é compartilhada por todas as guias do PlaidCloud que você tiver abertas. Copie de um projeto em uma guia, mude para um projeto em outra e cole lá. Ela não é compartilhada entre navegadores diferentes, entre navegadores em máquinas diferentes nem com outras pessoas, e trocar de espaço de trabalho a limpa.

Uma única área de transferência atende a todos os lugares em que você copia uma etapa — a tabela de etapas, a tabela mais antiga que você acessa ao manter Ctrl (ou Cmd) pressionada ao abrir um fluxo de trabalho e a tela do fluxo de trabalho avançado — então você pode copiar em qualquer um deles e colar em qualquer um deles. Copie algumas etapas de uma tabela e cole-as em uma tela avançada, ou o contrário; é a mesma área de transferência.



Copiar uma etapa cria uma etapa duplicada dentro do projeto — uma nova etapa, com configuração própria, independente da original.

Uma etapa pode aparecer no máximo uma vez na estrutura de qualquer fluxo de trabalho. **Anexar** e **Inserir** sempre colam uma duplicata nova, então nunca esbarram nessa regra. Colar uma *referência* a uma etapa que você já posicionou — veja **Colar como etapa vinculada** abaixo — é diferente: é a mesma etapa, então colá-la em um fluxo de trabalho que já a contém, inclusive aquele de onde você a copiou, é recusado com uma mensagem que cita a etapa. Vincule-a a um fluxo de trabalho *diferente*.



## Colar etapas


Depois de selecionar etapas para copiar e colocá-las na área de transferência, você pode colá-las no mesmo fluxo de trabalho ou em outro, até mesmo em outro projeto. Há duas opções ao colar as etapas no fluxo de trabalho:


* Anexar ao final do fluxo de trabalho
* Inserir após a última linha selecionada

A opção de anexar simplesmente adiciona as etapas ao final do fluxo de trabalho selecionado. A opção de inserir coloca as etapas copiadas após a linha selecionada. Observe que, se várias etapas foram copiadas para a área de transferência a partir de várias áreas de um fluxo de trabalho, elas serão coladas em ordem, mas sem nenhuma informação da hierarquia aninhada que tinham quando foram copiadas. A colagem será apenas uma lista simples de etapas a inserir. Isso pode ser inesperado, mas é mais seguro do que criar no fluxo de trabalho de destino toda a estrutura de diretórios que existia no fluxo de trabalho de origem.


## Colar como etapa vinculada


**Colar → Adicionar etapas vinculadas (avançado)** coloca a *mesma* etapa no fluxo de trabalho de destino, em vez de uma cópia dela. As duas posições são uma única etapa: edite-a em qualquer um dos fluxos de trabalho e ambos mudam, porque há apenas uma etapa a alterar.


Uma etapa vinculada só pode ser colada no projeto de onde foi copiada. Vincular é uma segunda posição de uma etapa que pertence a um projeto, então não faz sentido fora desse projeto — se você colar em um projeto diferente, o PlaidCloud recusa e orienta você a usar **Anexar** ou **Inserir**, que copiam as etapas para o projeto de destino como etapas próprias.

Uma etapa vinculada também não pode ser colocada em um fluxo de trabalho que já a contém — isso seria a mesma etapa duas vezes na estrutura de um fluxo de trabalho, o que o PlaidCloud recusa. Isso é mais provável de acontecer se uma operação de vinculação parecer ter falhado e você tentar de novo: a primeira tentativa na verdade foi concluída, e a nova tentativa é recusada em vez de corromper o fluxo de trabalho. O erro cita a etapa para que você confirme que ela já está lá.


## Copiar e colar na tela avançada


Em um fluxo de trabalho avançado, você pode copiar e colar etapas diretamente na tela usando o teclado, e as conexões entre elas vão junto.


Selecione as etapas desejadas — arraste uma caixa ao redor delas, ou clique em uma e use Shift ou Ctrl/Cmd com clique para adicionar mais — e pressione **Ctrl/Cmd+C**. Vá até o fluxo de trabalho em que deseja colocá-las, seja neste projeto ou em outro, aponte para o local onde devem ficar e pressione **Ctrl/Cmd+V**. As etapas são copiadas com a mesma disposição que tinham e ficam selecionadas, para que você possa arrastá-las até o lugar certo. Você também pode fazer as duas coisas sem o teclado. Clique com o botão direito em um espaço vazio da tela e escolha **Copiar N etapas** (exibido quando há etapas selecionadas) ou **Colar N etapas aqui** (exibido quando a área de transferência contém etapas); as etapas coladas ficam onde você clicou. Quando a área de transferência contém etapas, a barra de ferramentas mostra "N etapas de *fluxo de trabalho*" com um botão **Colar**, que cola no meio da parte da tela que você está vendo.


**Um grupo é colado como grupo.** Clique no cabeçalho de um grupo e o grupo e todas as suas etapas são selecionados juntos; ao copiar, a caixa do grupo e seus membros são colados como um só. Uma caixa desenhada na seleção ao redor de um grupo inteiro o seleciona da mesma forma.


**As conexões entre as etapas copiadas vão com elas; as conexões com etapas que você não copiou, não.** Uma etapa da sua seleção que recebia dados de uma etapa deixada para trás chega sem essa conexão de entrada — não há nada do outro lado para conectar. A colagem avisa quando isso acontece, de modo que uma conexão perdida nunca passa em silêncio.


**Colar no mesmo fluxo de trabalho** desloca levemente as cópias para que não caiam exatamente sobre os originais. Colar em um fluxo de trabalho que não é avançado — uma tabela de etapas comum — descarta a disposição da tela e as conexões e simplesmente adiciona as etapas; a colagem avisa que fez isso.


**Uma colagem grande é feita em lotes automaticamente.** Nada tem limite e nada é descartado em silêncio — uma colagem de centenas de etapas simplesmente mostra o progresso enquanto é processada, e você pode cancelá-la. Se uma colagem não puder ser concluída, as etapas que já tinham sido adicionadas são removidas novamente, para que você não fique com um fluxo de trabalho colado pela metade; no raro caso de algumas delas não poderem ser removidas automaticamente, a mensagem informa isso e indica quantas restam, em vez de afirmar que a reversão foi completa.


**Para desfazer uma colagem,** pressione **Ctrl/Cmd+Z** logo após ela — as etapas coladas são removidas. Depois que um colaborador alterar o fluxo de trabalho, ou que você o recarregar, esse desfazer de um passo deixa de agir, em vez de arriscar remover um trabalho que já não é só seu.


As etapas são copiadas como novas etapas, com identidade própria. Colar a *mesma* etapa em mais de um lugar — o comportamento de etapa vinculada descrito acima — é uma ação da tabela de etapas; na tela, use **Adicionar etapa** para colocar uma referência em um fluxo de trabalho que ainda não contém essa etapa.
