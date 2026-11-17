---
title: Cree aplicaciones Panel con Weave
description: Describa la aplicación que desea, deje que Weave la escriba en Panel Studio y apruebe el cambio exacto antes de que se guarde nada.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weave puede escribir y modificar aplicaciones Panel por usted. Funciona en [Panel Studio](/es/guides/panel-apps/studio/) sobre la aplicación que tiene abierta, y nada de lo que propone cambia la aplicación hasta que usted lo apruebe.

## Preguntar a Weave

1. Abra la aplicación en Panel Studio.
2. Elija **Preguntar a Weave**. El [dock de Weave](/es/guides/ai-assistant/weave-dock/) se abre en la conversación de la aplicación.
3. Describa lo que desea, por ejemplo "Agrega un filtro de región y un gráfico de ingresos por mes".

Weave ya conoce la aplicación en la que trabaja: sus archivos, su estado de compilación y los errores de compilación, y la tabla o vista en la que se basa. No necesita pegar código ni errores en la conversación. Si una compilación falla, elija **Preguntar a Weave sobre este error** en el estado de compilación: el dock se abre con el error en el cuadro, listo para que usted lo envíe.

Weave trabaja con aplicaciones que pertenecen a un proyecto. Para una aplicación que no pertenece a ninguno, Panel Studio indica *Asigne esta aplicación a un proyecto para usar Weave.*

## Aprobar el cambio

Cuando Weave quiere cambiar el código de la aplicación, muestra una tarjeta de aprobación con la diferencia completa: cada línea que agrega y elimina, archivo por archivo.

1. Lea la diferencia.
2. Elija **Aprobar** para guardar el cambio en el borrador de la aplicación, o **Rechazar** para descartarlo.

Aprobar guarda un borrador. No publica. Obtenga una vista previa del resultado y luego [publique](/es/guides/panel-apps/studio/#publicar) cuando esté conforme.

### Las aprobaciones solo están disponibles en la web

Solo puede aprobar un cambio de código en PlaidCloud en la web. En la aplicación móvil de PlaidCloud puede rechazar un cambio de código propuesto, pero no aprobarlo. Los demás cambios de Weave aún se pueden aprobar en su teléfono. Consulte [Weave en el móvil](/es/guides/mobile-app/weave-on-mobile/).

## Siguientes pasos

- [Panel Studio](/es/guides/panel-apps/studio/): guardar, obtener una vista previa y publicar.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): los componentes con los que Weave construye.
