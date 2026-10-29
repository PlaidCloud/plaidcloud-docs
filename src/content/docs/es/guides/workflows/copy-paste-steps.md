---
title: "Copiar y pegar pasos"
description: Copie y pegue pasos de flujo de trabajo entre flujos de trabajo de PlaidCloud para reutilizar configuraciones de pasos y acelerar el desarrollo de flujos de trabajo.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/copy-paste-steps.md
---

## Copiar pasos


A menudo resulta útil copiar pasos en lugar de empezar desde cero cada vez. PlaidCloud permite copiar pasos dentro de un mismo flujo de trabajo y también entre flujos de trabajo, incluso en otros proyectos. Puede seleccionar varios pasos para copiarlos a la vez. Seleccione los pasos del flujo de trabajo dentro de la jerarquía y haga clic en el botón **Copiar pasos seleccionados** en la parte superior de la tabla.



Esto coloca los pasos seleccionados en el portapapeles y permite pegarlos en el flujo de trabajo actual o en otro.

El portapapeles se guarda en su navegador, por lo que se conserva al volver a cargar la página y es compartido por todas las pestañas de PlaidCloud que tenga abiertas. Copie desde un proyecto en una pestaña, cambie a un proyecto en otra y pegue allí. No se comparte entre navegadores distintos, entre navegadores de equipos diferentes ni con otras personas, y al cambiar de espacio de trabajo se borra.

Un solo portapapeles sirve para todos los lugares desde los que se copia un paso: la tabla de pasos, la tabla anterior a la que se accede al mantener presionada la tecla Ctrl (o Cmd) mientras abre un flujo de trabajo, y el lienzo del flujo de trabajo avanzado. Así, puede copiar en cualquiera de ellos y pegar en cualquiera de ellos. Copie algunos pasos de una tabla y péguelos en un lienzo avanzado, o al revés; es el mismo portapapeles.



Al copiar un paso se crea un paso duplicado dentro del proyecto: un paso nuevo, con su propia configuración, independiente del original.

Un paso puede aparecer como máximo una vez en la estructura de un flujo de trabajo determinado. **Anexar** e **Insertar** siempre pegan un duplicado nuevo, por lo que nunca se topan con esta restricción. Pegar una *referencia* a un paso que ya colocó (consulte **Pegar como paso vinculado** más abajo) es distinto: se trata del mismo paso, así que pegarlo en un flujo de trabajo que ya lo contiene, incluido aquel desde el que lo copió, se rechaza con un mensaje que indica el nombre del paso. En su lugar, vincúlelo a un flujo de trabajo *distinto*.



## Pegar pasos


Después de seleccionar los pasos que desea copiar y colocarlos en el portapapeles, puede pegarlos en el mismo flujo de trabajo o en otro, incluso en otro proyecto. Al pegar los pasos en el flujo de trabajo hay dos opciones:


* Anexar al final del flujo de trabajo
* Insertar después de la última fila seleccionada

La opción de anexar simplemente agrega los pasos al final del flujo de trabajo seleccionado. La opción de insertar coloca los pasos copiados después de la fila seleccionada. Tenga en cuenta que, si se copiaron al portapapeles varios pasos de distintas áreas de un flujo de trabajo, se pegarán en orden pero sin la información de jerarquía anidada que tenían al copiarse. El resultado será una lista plana de pasos que solo se insertan. Esto puede ser inesperado, pero es más seguro que crear en el flujo de trabajo de destino toda la estructura de directorios que existía en el flujo de trabajo de origen.


## Pegar como paso vinculado


**Pegar → Agregar pasos vinculados (avanzado)** coloca el *mismo* paso en el flujo de trabajo de destino en lugar de una copia. Ambas ubicaciones son un único paso: si lo edita en cualquiera de los flujos de trabajo, cambian ambos, porque solo hay un paso que modificar.


Un paso vinculado solo se puede pegar en el proyecto desde el que se copió. Vincular es una segunda ubicación de un paso que pertenece a un proyecto, por lo que no tiene sentido fuera de ese proyecto: si lo pega en un proyecto distinto, PlaidCloud lo rechaza y le indica que use **Anexar** o **Insertar**, que copian los pasos en el proyecto de destino como pasos propios.

Tampoco se puede colocar un paso vinculado en un flujo de trabajo que ya lo contiene, ya que sería el mismo paso dos veces en la estructura de un flujo de trabajo, y PlaidCloud lo rechaza. Es más probable que esto ocurra si una operación de vinculación parece fallar y la intenta de nuevo: el primer intento sí se realizó, y el reintento se rechaza en lugar de dañar el flujo de trabajo. El error indica el nombre del paso para que pueda confirmar que ya está allí.


## Copiar y pegar en el lienzo avanzado


En un flujo de trabajo avanzado puede copiar y pegar pasos directamente en el lienzo con el teclado, y los vínculos entre ellos se conservan.


Seleccione los pasos que desee (arrastre un recuadro a su alrededor, o haga clic en uno y use Mayús o Ctrl/Cmd con clic para agregar más) y presione **Ctrl/Cmd+C**. Vaya al flujo de trabajo en el que los quiere, ya sea en este proyecto o en otro, señale el lugar donde deben ir y presione **Ctrl/Cmd+V**. Los pasos se copian con la misma disposición que tenían y quedan seleccionados para que pueda arrastrarlos a su lugar. También puede hacer ambas cosas sin el teclado. Haga clic con el botón derecho en un espacio vacío del lienzo y elija **Copiar N pasos** (se muestra cuando hay pasos seleccionados) o **Pegar N pasos aquí** (se muestra cuando el portapapeles contiene pasos); los pasos pegados quedan donde hizo clic. Cuando el portapapeles contiene pasos, la barra de herramientas muestra “N pasos de *flujo de trabajo*” con un botón **Pegar** que pega en el centro de la parte del lienzo que está viendo.


**Un grupo se pega como grupo.** Haga clic en el encabezado de un grupo y el grupo y todos sus pasos se seleccionan juntos; al copiar, el recuadro del grupo y sus miembros se pegan como un conjunto. Un recuadro de selección dibujado alrededor de un grupo completo lo selecciona de la misma manera.


**Los vínculos entre los pasos copiados se conservan; los vínculos a pasos que no copió, no.** Un paso de su selección que recibía datos de un paso que dejó fuera llega sin ese vínculo de entrada, porque no hay nada al otro extremo con qué conectarlo. Al pegar se le avisa cuando esto ocurre, de modo que una conexión perdida nunca pasa inadvertida.


**Al pegar en el mismo flujo de trabajo**, las copias se desplazan ligeramente para que no queden exactamente encima de los originales. Al pegar en un flujo de trabajo que no es avanzado, como una tabla de pasos común, se pierden la disposición del lienzo y los vínculos, y simplemente se agregan los pasos; al pegar se le avisa de ello.


**Un pegado grande se realiza automáticamente por lotes.** No hay ningún límite y nada se descarta en silencio: un pegado de cientos de pasos simplemente muestra su progreso mientras trabaja, y usted puede cancelarlo. Si un pegado no puede terminar, los pasos que ya había agregado se eliminan de nuevo para que no quede un flujo de trabajo pegado a medias; en el raro caso de que algunos no se puedan eliminar automáticamente, el mensaje lo indica y señala cuántos quedan, en lugar de afirmar que la reversión fue limpia.


**Para deshacer un pegado**, presione **Ctrl/Cmd+Z** inmediatamente después: los pasos pegados se eliminan. Una vez que un colaborador haya cambiado el flujo de trabajo, o que usted lo haya vuelto a cargar, ese deshacer de un solo paso se aparta para no arriesgarse a eliminar trabajo que ya no es solo suyo.


Los pasos se copian como pasos nuevos y propios. Pegar el *mismo* paso en más de un lugar (el comportamiento de paso vinculado descrito arriba) es una acción de la tabla de pasos; en el lienzo, use **Agregar paso** para colocar una referencia en un flujo de trabajo que todavía no contiene ese paso.
