---
title: Pasos de Oracle EPM (HFM / FCCS)
description: "Pasos de flujo de trabajo que obtienen por su cuenta un segmento de datos ad hoc de Oracle FCCS a través de su conexión de HFM/FCCS: cree un punto de vista, ejecútelo y cargue el resultado como una tabla."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

Pasos de flujo de trabajo que leen de Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) a través de su [conexión de HFM/FCCS](/es/guides/connections/hfm-fccs/). Un usuario de finanzas crea un punto de vista en el formulario del paso, lo ejecuta y la cuadrícula devuelta se carga automáticamente como una tabla del proyecto, sin ticket al equipo de HFM y sin necesidad de conocimientos de consolidación.

## Pasos

- [HFM/FCCS: leer datos (ad hoc)](/es/reference/workflow-steps/oracle-epm/hfm-fccs-read/): obtenga un segmento de datos por su cuenta con un selector de punto de vista; almacena en caché las extracciones repetidas, está listo para la seguridad a nivel de fila y se puede promover a una carga periódica programada.

## Relacionado

- [Extraer de HFM / FCCS (guía)](/es/guides/connections/hfm-fccs/)
- [Conector de HFM / FCCS](/es/reference/connectors/rest/hfm-fccs/)
