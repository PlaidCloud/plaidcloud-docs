---
title: "Copiar e colar passos"
description: Copie e cole passos de fluxos de trabalho entre fluxos de trabalho do PlaidCloud para reutilizar configurações de passos e acelerar o desenvolvimento de fluxos de trabalho.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/copy-paste-steps.md
---

## Copiar passos


Muitas vezes é útil copiar passos em vez de começar do zero de cada vez. O PlaidCloud permite copiar passos dentro de um fluxo de trabalho, entre fluxos de trabalho e até para outros projetos. Pode selecionar vários passos para copiar em simultâneo. Selecione os passos do fluxo de trabalho na hierarquia e clique no botão **Copiar passos selecionados** no topo da tabela.



Isto coloca os passos selecionados na área de transferência e permite colá-los no fluxo de trabalho atual ou noutro.

A área de transferência é mantida no browser, pelo que sobrevive à atualização da página e é partilhada por todos os separadores do PlaidCloud que tenha abertos. Copie a partir de um projeto num separador, mude para um projeto noutro separador e cole aí. Não é partilhada entre browsers diferentes, entre browsers em máquinas diferentes, nem com outras pessoas, e a mudança de área de trabalho limpa-a.

Uma única área de transferência serve todos os locais onde se copia um passo — a tabela de passos, a tabela mais antiga a que se acede mantendo premida a tecla Ctrl (ou Cmd) ao abrir um fluxo de trabalho, e a área de desenho do fluxo de trabalho avançado — pelo que pode copiar em qualquer um deles e colar em qualquer um deles. Copie alguns passos de uma tabela e cole-os numa área de desenho avançada, ou o inverso; a área de transferência é a mesma.



Copiar um passo cria um passo duplicado no projeto — um novo passo com a sua própria configuração, independente do original.

Um passo pode aparecer no máximo uma vez na estrutura de um determinado fluxo de trabalho. **Acrescentar** e **Inserir** colam sempre um duplicado novo, pelo que nunca se deparam com esta situação. Colar uma *referência* para um passo que já colocou — veja **Colar como passo ligado** abaixo — é diferente: trata-se do mesmo passo, pelo que colá-lo num fluxo de trabalho que já o contém, incluindo o fluxo de trabalho de onde o copiou, é recusado com uma mensagem que indica o nome do passo. Ligue-o antes a um fluxo de trabalho *diferente*.



## Colar passos


Depois de selecionar os passos a copiar e de os colocar na área de transferência, pode colá-los no mesmo fluxo de trabalho ou noutro, mesmo que noutro projeto. Existem duas opções ao colar os passos no fluxo de trabalho:


* Acrescentar no fim do fluxo de trabalho
* Inserir a seguir à última linha selecionada

A opção de acrescentar limita-se a acrescentar os passos no fim do fluxo de trabalho selecionado. A opção de inserir insere os passos copiados a seguir à linha selecionada. Tenha em atenção que, se tiverem sido copiados para a área de transferência vários passos de várias zonas de um fluxo de trabalho, serão colados por ordem, mas sem a informação de hierarquia aninhada que tinham quando foram copiados. A colagem resulta apenas numa lista simples de passos a inserir. Isto pode ser inesperado, mas é mais seguro do que criar no fluxo de trabalho de destino toda a estrutura de diretórios que existia no fluxo de trabalho de origem.


## Colar como passo ligado


**Colar → Adicionar passos ligados (avançado)** coloca o *mesmo* passo no fluxo de trabalho de destino, em vez de uma cópia do mesmo. Ambas as colocações são o mesmo passo: se o editar num dos fluxos de trabalho, ambos mudam, porque existe apenas um passo para alterar.


Um passo ligado só pode ser colado no projeto de onde foi copiado. A ligação é uma segunda colocação de um passo que pertence a um projeto, pelo que não faz sentido fora desse projeto — se colar noutro projeto, o PlaidCloud recusa e indica que deve utilizar **Acrescentar** ou **Inserir**, que copiam os passos para o projeto de destino como passos independentes.

Um passo ligado também não pode ser colocado num fluxo de trabalho que já o contém — seria o mesmo passo duas vezes na estrutura de um fluxo de trabalho, o que o PlaidCloud recusa. É mais provável que isto aconteça se uma operação de ligação parecer ter falhado e tentar novamente: a primeira tentativa foi, na verdade, concluída com êxito, e a repetição é recusada em vez de corromper o fluxo de trabalho. O erro indica o nome do passo, para que possa confirmar que já lá está.


## Copiar e colar na área de desenho avançada


Num fluxo de trabalho avançado, pode copiar e colar passos diretamente na área de desenho com o teclado, e as ligações entre eles acompanham-nos.


Selecione os passos pretendidos — arraste uma caixa à volta deles, ou clique num e utilize Shift ou Ctrl/Cmd com clique para adicionar mais — e prima **Ctrl/Cmd+C**. Vá para o fluxo de trabalho onde os pretende, neste projeto ou noutro, aponte para o local onde devem ficar e prima **Ctrl/Cmd+V**. Os passos são copiados com a disposição que tinham e ficam selecionados, para que possa arrastá-los para o lugar. Também pode fazer ambas as operações sem o teclado. Clique com o botão direito num espaço vazio da área de desenho e escolha **Copiar N passos** (apresentado quando há passos selecionados) ou **Colar N passos aqui** (apresentado quando a área de transferência contém passos); os passos colados ficam no local onde clicou. Quando a área de transferência contém passos, a barra de ferramentas mostra "N passos de *fluxo de trabalho*" com um botão **Colar** que cola no centro da parte da área de desenho que está a ver.


**Um grupo é colado como grupo.** Clique no cabeçalho de um grupo e o grupo e todos os seus passos ficam selecionados em conjunto; ao copiar, a caixa do grupo e os seus membros são colados como um só. Uma caixa desenhada à volta de um grupo inteiro na seleção por retângulo seleciona-o da mesma forma.


**As ligações entre os passos copiados acompanham-nos; as ligações a passos que não copiou, não.** Um passo da sua seleção que era alimentado por um passo que deixou para trás chega sem essa ligação de entrada — não há nada na outra extremidade a que se ligar. A colagem avisa-o quando isto acontece, pelo que uma ligação perdida nunca passa despercebida.


**Colar no mesmo fluxo de trabalho** desloca ligeiramente as cópias para que não fiquem exatamente por cima dos originais. Colar num fluxo de trabalho que não é avançado — uma tabela de passos normal — descarta a disposição da área de desenho e as ligações, e limita-se a adicionar os passos; a colagem avisa-o de que o fez.


**Uma colagem grande é feita automaticamente em lotes.** Nada tem limite e nada é descartado em silêncio — uma colagem de centenas de passos mostra simplesmente o progresso à medida que decorre, e pode cancelá-la. Se uma colagem não puder ser concluída, os passos que já tinha adicionado são removidos novamente, para que não fique com um fluxo de trabalho colado a meio; no caso raro de alguns deles não poderem ser removidos automaticamente, a mensagem indica-o e diz quantos restam, em vez de afirmar que a reversão foi limpa.


**Para anular uma colagem,** prima **Ctrl/Cmd+Z** logo a seguir — os passos colados são removidos. Depois de um colaborador ter alterado o fluxo de trabalho, ou de o ter recarregado, essa anulação de um passo deixa de se aplicar, para não arriscar remover trabalho que já não é apenas seu.


Os passos são copiados como novos passos independentes. Colar o *mesmo* passo em mais do que um local — o comportamento de passo ligado descrito acima — é uma ação da tabela de passos; na área de desenho, utilize **Adicionar passo** para colocar uma referência num fluxo de trabalho que ainda não contém esse passo.
