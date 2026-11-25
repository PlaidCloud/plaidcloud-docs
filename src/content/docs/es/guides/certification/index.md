---
title: Certificación de PlaidCloud
description: "Obtenga insignias de PlaidCloud superando laboratorios prácticos que se califican automáticamente: Fundamentos y, después, Profesional y Experto en cada ruta, y Master por revisión."
sidebar:
  label: Resumen
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/index.md
---

La certificación de PlaidCloud demuestra lo que usted sabe hacer mediante laboratorios prácticos. Cada laboratorio le da un proyecto en el que trabajar y una tarea, y califica su trabajo automáticamente cuando lo envía. No hay exámenes que reservar ni cursos en los que inscribirse: usted se prepara leyendo, en orden, las guías que enumera cada [ruta de aprendizaje](#rutas-de-aprendizaje).

## Niveles y rutas

| Nivel | Ruta | Cómo se obtiene |
|---|---|---|
| **Fundamentos** | Sin ruta | Superar el laboratorio de Fundamentos |
| **Profesional** | **Ingeniería de datos**, **Modelado** o **Analítica** | Superar el laboratorio Profesional de la ruta |
| **Experto** | **Ingeniería de datos**, **Modelado** o **Analítica** | Superar el laboratorio Experto de la ruta, que tiene tiempo límite |
| **Máster** | Sin ruta | Tener tres insignias Experto y superar una revisión de PlaidCloud de una implementación en producción |

Las rutas **Operaciones financieras** y **Administración y seguridad** figuran como **Próximamente**. Todavía no tienen laboratorios.

En cada ruta, su insignia Experto se muestra en lugar de su insignia Profesional.

## Abrir Certificaciones

Abra el menú de usuario en la esquina superior derecha y elija **Certificaciones**. El panel se abre en su pestaña de inicio con:

- un banner con su objetivo, cuando un administrador del espacio de trabajo ha fijado uno, que indica si ya tiene esa insignia;
- **Sus insignias**, con la fecha en que obtuvo cada insignia y la fecha en que caduca;
- **Laboratorios**, una cuadrícula de cada ruta frente a **Fundamentos**, **Profesional** y **Experto**. Cada celda muestra **Iniciar laboratorio**, **Obtenida** para una insignia que usted tiene o, en el espacio de trabajo de certificación, la fecha en que el laboratorio vuelve a estar disponible tras una [espera](#la-espera-de-7-días). La fila de su objetivo está marcada con **su objetivo**, y un objetivo de Fundamentos o Master marca **Todas las rutas**;
- **Máster**, con cuántas de las tres insignias Experto tiene;
- **Guía de certificación ›**, que abre esta guía.

**Volver al inicio** cierra el panel.

## El espacio de trabajo de certificación

Los laboratorios se ejecutan solo en el espacio de trabajo de certificación de PlaidCloud. En cualquier otro espacio de trabajo, **Iniciar laboratorio** lo agrega al espacio de trabajo de certificación como miembro que puede construir, con la misma dirección de correo electrónico, y lo abre en una pestaña nueva en su propio panel **Certificaciones**. Elija **Iniciar laboratorio** de nuevo allí para iniciar el laboratorio.

La primera vez, PlaidCloud le envía un correo electrónico para establecer una contraseña para el espacio de trabajo de certificación. Revise su bandeja de entrada.

Si no pertenece a ningún espacio de trabajo de PlaidCloud, comuníquese con PlaidCloud y le invitaremos al espacio de trabajo de certificación.

Iniciar un laboratorio, abandonarlo y obtener una insignia requieren una dirección de correo electrónico verificada, porque sus insignias pertenecen a ella. En cualquier otro espacio de trabajo, **Iniciar laboratorio** requiere que su dirección de correo electrónico esté verificada en ese espacio de trabajo. Allí, **Iniciar laboratorio** y **Compartir desde el espacio de trabajo de certificación** abren el espacio de trabajo de certificación solo un número limitado de veces al día por cada dirección de correo electrónico; superado ese límite, inténtelo de nuevo al día siguiente.

## Cómo funciona un laboratorio

1. Elija **Iniciar laboratorio** en el espacio de trabajo de certificación. PlaidCloud crea el proyecto del laboratorio para usted; solo usted puede abrirlo.
2. El panel muestra el laboratorio: su título, cuándo lo inició, **Su tarea**, y **Enviar para calificar**, **Abrir proyecto** y **Abandonar**. Mientras hay un laboratorio abierto, el panel lo muestra en lugar de sus insignias y la cuadrícula.
3. Elija **Abrir proyecto** y realice la tarea.
4. Elija **Enviar para calificar**. La calificación ejecuta el flujo de trabajo del laboratorio y después comprueba lo que produjo esa ejecución, por lo que puede tardar tanto como la ejecución. Se ejecuta en segundo plano: el panel muestra **Evaluando su laboratorio** y comprueba si hay resultado, y **Enviar para calificar** y **Abandonar** no están disponibles hasta que termina la calificación. Puede salir del panel, o de PlaidCloud, mientras se califica; cuando vuelva a abrir **Certificaciones**, sigue esperando el resultado o lo muestra si la calificación ya terminó. Si el panel no puede contactar con el servidor durante una calificación larga, añade *No se puede contactar con el servidor; se sigue intentando…* y sigue comprobando.
   - Si se superan todas las comprobaciones, la insignia es suya y se elimina el proyecto del laboratorio.
   - Si alguna comprobación falla, **Último resultado** enumera cada comprobación como **Superado** o **Error**. Una comprobación fallida indica qué estaba mal y tiene un enlace **Guía ›** a la guía que lo explica. Corrija su proyecto y envíe de nuevo.

Puede enviar tantas veces como quiera mientras el laboratorio esté abierto. Si envía mientras el flujo de trabajo del laboratorio ya se está ejecutando, no se califica nada; espere a que termine la ejecución y envíe de nuevo. Si la calificación se detiene antes de terminar, **Último resultado** lo indica; envíe de nuevo.

Si se superan todas las comprobaciones pero su dirección de correo electrónico no está verificada, no se concede ninguna insignia. Verifique su dirección de correo electrónico y envíe de nuevo.

### Límites de tiempo

Los laboratorios Experto tienen tiempo límite: la cuadrícula **Laboratorios** muestra **Con tiempo límite · 4 h**, y un laboratorio Experto abierto muestra cuántos minutos quedan. El reloj empieza cuando inicia el laboratorio y sigue corriendo trabaje o no en él.

Un envío que haga antes de que se agote el tiempo se califica aunque la calificación termine después. Si esa calificación se detiene antes de terminar, o se superan todas las comprobaciones pero todavía no se puede conceder ninguna insignia, puede enviar de nuevo durante al menos un día después de que se agote el tiempo.

De lo contrario, cuando se agota el tiempo, el laboratorio ya no se puede superar. Su siguiente envío termina el intento, elimina el proyecto del laboratorio e inicia la espera de 7 días. Si no envía de nuevo, la limpieza nocturna de PlaidCloud termina el intento de la misma manera.

Los laboratorios de Fundamentos y Profesional no tienen límite de tiempo.

### La espera de 7 días

**Abandonar** elimina el proyecto de su laboratorio y termina el intento. Primero debe confirmarlo. Si el proyecto de un laboratorio no se puede eliminar cuando termina su intento, ya sea porque lo supera, lo abandona o se queda sin tiempo, un mensaje lo indica si el panel está abierto, y la limpieza nocturna lo elimina más tarde. Abandonar un laboratorio, o quedarse sin tiempo en un laboratorio Experto, inicia una espera de 7 días antes de poder iniciar de nuevo ese laboratorio; la cuadrícula **Laboratorios** muestra la fecha en que vuelve a estar disponible. Enviar un laboratorio que no supera algunas comprobaciones no inicia una espera.

## Caducidad

Las insignias caducan dos años después de obtenerlas. Una insignia caducada deja de aparecer en **Sus insignias** y para los administradores, y su laboratorio se puede iniciar de nuevo, a menos que aún tenga una insignia superior en la misma ruta.

## Master

Master es la única insignia que no se obtiene en un laboratorio. Requiere tres insignias Experto que no hayan caducado y una implementación en producción, revisada por PlaidCloud.

**Solicitar revisión Master**, en la tarjeta **Máster**, queda disponible cuando tiene tres insignias Experto. Abre **Ayuda y soporte** con un ticket nuevo que ya nombra sus insignias Experto. Agregue los detalles de su implementación y envíelo. La revisión busca:

- una implementación que esté en producción en un cliente o socio con nombre;
- que usted la haya construido o dirigido;
- que use la capacidad de al menos dos rutas;
- un contacto con nombre que lo confirme.

La insignia Master también caduca dos años después de concederse.

## Compartir una insignia

Cada insignia tiene su propia página pública de verificación, que muestra la insignia, su nombre, cuándo se emitió, cuándo caduca y si sigue siendo válida. El nombre es el de su perfil en el espacio de trabajo de certificación cuando hace pública la insignia; si PlaidCloud creó su cuenta allí cuando inició un laboratorio, es la parte de su dirección de correo electrónico anterior a la @. Para mostrar un nombre modificado, haga la insignia privada y luego pública de nuevo. La página nunca muestra su dirección de correo electrónico completa. La página existe solo mientras la insignia es pública.

En el espacio de trabajo de certificación, bajo cada insignia en **Sus insignias**:

- **Hacer público** publica la página de verificación de la insignia. Desactívelo para retirar la página.
- **Copiar enlace** copia la dirección de la página.
- **Añadir a LinkedIn** abre el formulario de LinkedIn para agregar una certificación, rellenado a partir de la insignia.

**Copiar enlace** y **Añadir a LinkedIn** funcionan solo mientras la insignia es pública. En cualquier otro espacio de trabajo, una insignia pública conserva **Copiar enlace** y **Añadir a LinkedIn**, y una insignia que no es pública ofrece **Compartir desde el espacio de trabajo de certificación**, que abre el espacio de trabajo de certificación en su panel **Certificaciones**.

Compartir requiere una dirección de correo electrónico verificada. Hasta que la suya esté verificada, **Sus insignias** no enumera ninguna.

## Qué ven los administradores

Las insignias pertenecen a su dirección de correo electrónico, por lo que se muestran en todos los espacios de trabajo en los que usted es miembro con esa dirección. En la lista **Miembros** de un espacio de trabajo, los administradores ven las insignias y el objetivo de cada miembro, y pueden asignar una ruta objetivo. Ven insignias, no intentos de laboratorio ni resultados, y un miembro cuya dirección de correo electrónico no está verificada no muestra ninguna insignia. Los agentes de IA conectados por MCP pueden leer las insignias y los objetivos de los miembros de la misma manera. Consulte [Insignias de certificación y objetivos](/es/administration/access/member-management/#insignias-de-certificación-y-objetivos).

## Rutas de aprendizaje

- [Fundamentos](/es/guides/certification/foundations/)
- [Ingeniería de datos](/es/guides/certification/data-engineering/)
- [Modelado](/es/guides/certification/modeling/)
- [Analítica](/es/guides/certification/analytics/)
