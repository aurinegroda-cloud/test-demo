# Shopify desde cero

En este capítulo vas a aprender a armar una tienda online con Shopify, elegir un producto, calcular si te conviene venderlo y conseguir tus primeros visitantes. Vamos despacio y con números reales.

Antes de empezar, una verdad incómoda: **la mayoría de las tiendas nuevas no vende nada en su primer mes.** Montar la tienda es la parte fácil. Lo difícil es encontrar un producto que la gente quiera y llevar gente a verlo. No te prometo ingresos; te prometo un método claro para probar sin perder más plata de la necesaria.

> Datos verificados con búsqueda web el 28 de noviembre de 2026. Precios, comisiones y normas aduaneras cambian seguido: confírmalos en [shopify.com/es](https://www.shopify.com/es) y en el [Centro de ayuda de Shopify](https://help.shopify.com/es) antes de pagar nada.

## 1. Qué es Shopify y qué modelos de negocio existen

### 1.1. La idea en una frase

Shopify es una plataforma que te alquila una tienda online por una cuota mensual. Te da el diseño, el carrito de compras, el checkout (la página donde el cliente paga), la gestión de pedidos y miles de **apps** (complementos que agregan funciones). Tú pones los productos, los textos y los clientes.

### 1.2. Los cuatro modelos

| Modelo | Cómo funciona | A favor para un principiante en LatAm | En contra |
|---|---|---|---|
| **Producto propio** | Compras o fabricas stock y lo envías tú. | Controlas calidad y tiempos de envío. Ideal para vender en tu propio país. | Necesitas capital para el stock y lugar para guardarlo. Riesgo de que no se venda. |
| **Dropshipping** | Vendes un producto que no tienes. Cuando alguien compra, el proveedor lo envía directo al cliente. | No necesitas stock. Puedes probar muchos productos con poco dinero. | Márgenes chicos, tiempos de envío largos, poco control de calidad. Hacia Argentina, la aduana lo complica mucho (ver sección 2). |
| **Impresión bajo demanda** | Diseñas camisetas (remeras), tazas o cuadros. Un proveedor los imprime y envía cuando hay una venta. | Sin stock. Tu diseño te diferencia. | Márgenes bajos. Los proveedores suelen estar en EE. UU. o Europa. |
| **Productos digitales** | Vendes archivos: plantillas, ebooks, presets, cursos. | Sin envíos ni aduana. Margen alto. Funciona igual desde cualquier país. | Necesitas crear algo valioso. Para cursos, Hotmart (capítulo anterior) suele ser más simple. |

**Recomendación para empezar:**

- Si vives en **Argentina** y quieres vender en Argentina: producto propio en pocas unidades, o productos digitales.
- Si quieres vender a **otros países** (EE. UU., México, España): dropshipping con proveedores que tengan depósito en ese país, o productos digitales. Ojo con los cobros (sección 2).

> **Tarea:** elige uno de los cuatro modelos y escribe en una línea por qué. Si dudas, empieza por el que requiera menos dinero.

## 2. Lo que tienes que saber antes de pagar (verificado)

### 2.1. Precios de los planes

Precios en dólares estadounidenses según la página oficial y comparativas de 2026. **Shopify ajusta precios por país**, así que el importe que veas desde Argentina puede ser distinto. Mira el precio exacto en tu panel antes de elegir.

| Plan | Pago mensual | Pago anual (por mes) | Comisión extra si usas una pasarela externa |
|---|---|---|---|
| Starter | US$ 5 | — | No tiene tienda completa: vende con enlaces en redes |
| Basic | US$ 39 | US$ 29 | 2 % |
| Grow | US$ 105 | US$ 79 | 1 % |
| Advanced | US$ 399 | US$ 299 | 0,6 % |
| Plus | desde US$ 2.300 | — | 0,2 % |

**Prueba gratis:** Shopify ofrece **3 días gratis** y después **US$ 1 por mes durante los primeros 3 meses** en los planes elegibles. Según comparativas, no pide tarjeta para la prueba. Para empezar, el plan **Basic** alcanza y sobra.

### 2.2. ¿Hay Shopify Payments en Argentina?

**No.** Shopify Payments es el procesador de pagos propio de Shopify. Según el Centro de ayuda (citado por varias fuentes en 2026), **Argentina no está en la lista de países admitidos**. En Latinoamérica, **México sí lo tiene desde marzo de 2025**.

Qué significa esto para ti:

1. Necesitas una **pasarela de pago externa**. Una **pasarela de pago** es el servicio que cobra la tarjeta del cliente y te deposita el dinero.
2. Shopify te cobra la **comisión extra por pasarela externa** (2 % en Basic), además de lo que cobra la pasarela.
3. Sin Shopify Payments, tu tienda procesa los pedidos **en una sola moneda**.

### 2.3. Qué pasarela usar

| Pasarela | Cuándo conviene | Notas |
|---|---|---|
| **Mercado Pago** | Vender dentro de Argentina (y otros países donde opera). | Se instala con la app oficial "Mercado Pago Checkout Pro". Comisión según el plazo de cobro; fuentes de 2026 indican aprox. **6,29 % + IVA** si cobras al instante y **1,49 % + IVA** si esperas 35 días (hay escalones intermedios). Confírmalo en tu cuenta, en la sección de costos. |
| **PayPal** | Cobrar a clientes del exterior. | Muy conocido fuera de LatAm. Desde Argentina, recibir y retirar fondos tiene limitaciones y costos: verifícalo antes de depender de él. |
| **Shopify Payments** | Solo si tu negocio está en un país admitido (por ejemplo México, EE. UU., España). | No disponible en Argentina. |
| **Pago manual** (transferencia, efectivo) | Ventas locales chicas. | Más trabajo y menos confianza del comprador. |

Una opción avanzada que vas a escuchar: abrir una empresa en EE. UU. para acceder a Shopify Payments y vender en dólares. Tiene costos, impuestos y obligaciones en dos países. No es para tu primer mes; si algún día lo consideras, hazlo con un contador.

### 2.4. Dropshipping hacia Argentina: por qué es difícil

Si el proveedor envía desde China u otro país a un cliente argentino, el paquete entra por **courier** (servicio de envío internacional puerta a puerta) y pasa por la aduana. Según fuentes de 2026 (verifica en ARCA porque cambia seguido):

- Tope de **US$ 3.000 por envío** y **50 kg**.
- **Franquicia de US$ 400**: en los primeros cinco envíos del año por persona no se pagan derechos de importación hasta ese valor, pero **el IVA del 21 % se paga igual**.
- En julio de 2026 un decreto (604/2026) equiparó el correo postal con el courier, y hubo anuncios de posibles cambios en la franquicia. **No pude confirmar el estado final**: revisa la normativa vigente.
- El **comprador** muchas veces tiene que declarar el envío con su CUIT y clave fiscal, y la aduana puede retener o revisar el paquete.

En la práctica: el cliente paga impuestos que no esperaba, el envío tarda y aparecen reclamos. **Para vender en Argentina, conviene tener stock local** (aunque sean pocas unidades) o trabajar con proveedores nacionales. Para vender solo en pesos dentro de Argentina, también existe **Tiendanube**, que cobra en moneda local y tiene plan gratuito; compáralo con Shopify.

### 2.5. Vender a otros países desde Argentina

- **EE. UU.:** desde 2025 se suspendió la exención "de minimis" (que dejaba entrar sin impuestos paquetes de hasta US$ 800). Para China terminó en mayo de 2025 y para el resto de los países en agosto de 2025; en junio de 2026 la aduana estadounidense la suspendió de forma indefinida. Resultado: casi todo paquete importado paga aranceles. Prefiere **proveedores con depósito en EE. UU.**: envían más rápido y sin sorpresas para el cliente.
- **España / Unión Europea:** el IVA se cobra desde el primer euro en compras de fuera de la UE. Busca proveedores con depósito en Europa.
- **México:** los paquetes importados también pagan impuestos. Hay proveedores con depósito local.
- **El cobro sigue siendo el cuello de botella:** sin Shopify Payments, cobrar tarjetas internacionales desde Argentina es más difícil. Resuélvelo antes de gastar en anuncios.

> **Tarea:** decide a qué país vas a vender primero y qué pasarela vas a usar. Si es Argentina, abre o revisa tu cuenta de Mercado Pago y anota la comisión exacta que te muestra.

## 3. Crear la tienda paso a paso

### 3.1. Cuenta y configuración inicial

1. Entra a [shopify.com/es](https://www.shopify.com/es) y toca **Comenzar prueba gratis**.
2. Responde las preguntas iniciales (qué vas a vender, dónde).
3. Elige bien el **país de tu negocio**: define monedas, impuestos y pasarelas disponibles.
4. En **Configuración → Detalles de la tienda**, completa nombre, correo de contacto, dirección y moneda.
5. Activa la verificación en dos pasos en tu cuenta.

### 3.2. Elegir un tema

Un **tema** es la plantilla de diseño de tu tienda.

1. Ve a **Tienda online → Temas**.
2. Empieza con un tema **gratuito** (por ejemplo, "Dawn"). Son rápidos y se ven bien en el celular.
3. Personaliza: logo, colores (dos o tres como máximo), tipografía legible.
4. Más del 70 % de las visitas suelen llegar desde el celular: revisa siempre la vista móvil.

**Atajo:** tu cuenta en **Curso Dropshipping Gratis** ([cursodropshippinggratis.com](https://cursodropshippinggratis.com)) trabaja con AutoDS y te ayuda con el **diseño de la tienda**. Puedes usarla para tener una base armada y después ajustar los detalles.

### 3.3. Páginas obligatorias

Sin estas páginas, la tienda pierde confianza y las plataformas de anuncios pueden rechazar tus campañas.

1. **Política de reembolsos y devoluciones.**
2. **Política de privacidad.**
3. **Términos del servicio.**
4. **Política de envíos:** plazos reales, costos, países.
5. **Contacto:** formulario, correo y, si puedes, WhatsApp.
6. **Sobre nosotros:** quién está detrás (sin inventar historias).
7. **Preguntas frecuentes.**

Shopify genera plantillas de políticas en **Configuración → Políticas**. **Léelas y adáptalas**: no publiques nada que no vayas a cumplir.

**Si vendes en Argentina**, la Ley de Defensa del Consumidor da al comprador online **10 días para arrepentirse** de la compra, y las tiendas deben mostrar un **"Botón de arrepentimiento"** visible. También se suele pedir el formulario **"Data Fiscal"** de ARCA en el sitio. Confírmalo con tu contador.

### 3.4. Dominio

El **dominio** es la dirección de tu tienda (por ejemplo, `mitienda.com`). Shopify te da uno gratis del tipo `mitienda.myshopify.com`, que sirve para probar. Para vender, conviene uno propio: puedes comprarlo desde **Configuración → Dominios**. Para Argentina, un `.com.ar` se registra en NIC Argentina.

### 3.5. Pasarela de pago

1. Ve a **Configuración → Pagos**.
2. Si estás en Argentina, instala la app **Mercado Pago** desde la Shopify App Store y conecta tu cuenta.
3. Si vendes al exterior, agrega **PayPal** u otra opción que funcione en tu país.
4. Haz una **compra de prueba** con un producto barato y reembólsala. Así ves todo el recorrido del cliente.

### 3.6. Envíos e impuestos

1. **Configuración → Envío y entrega:** crea zonas (por ejemplo, "Argentina" o "EE. UU.") y tarifas. Para empezar, una tarifa fija o "envío gratis" con el costo incluido en el precio es lo más simple.
2. Escribe **plazos honestos**. Si el proveedor tarda 10 a 15 días, dilo.
3. **Configuración → Impuestos y aranceles:** activa lo que corresponda a tu país. En Argentina, define con tu contador si los precios incluyen IVA.

### 3.7. Apps esenciales (pocas y buenas)

Cada app suma un costo mensual y puede hacer más lenta la tienda. Empieza con lo mínimo:

1. **App de proveedor / dropshipping** (AutoDS, DSers o Zendrop) si haces dropshipping.
2. **Reseñas de productos** (para mostrar opiniones reales de clientes).
3. **Email marketing** (Shopify Email viene incluido con un cupo gratuito).
4. **Botón de WhatsApp** para atención.
5. **Descargas digitales** (la app gratuita de Shopify) si vendes archivos.

> **Tarea:** crea la tienda en la prueba gratis, elige un tema, publica las 7 páginas obligatorias y haz una compra de prueba.

## 4. Investigar productos

### 4.1. Criterios de un producto "ganador"

Un **producto ganador** es uno que se vende bien con anuncios y deja margen. Ningún producto es ganador para siempre ni para todos. Buscas que cumpla la mayoría de estos criterios:

1. **Resuelve un problema o despierta deseo** claro ("efecto wow").
2. **Se entiende en 3 segundos** en un video.
3. **No se consigue fácil** en el negocio de la esquina ni en el supermercado.
4. **Precio de venta** que permita multiplicar el costo por 2,5 a 3 (lo vemos en la sección 5).
5. **Liviano y resistente:** envío barato, pocas roturas.
6. **Sin tallas complicadas** ni temas médicos o regulados.
7. **Demanda comprobable:** otros ya lo están anunciando y tiene comentarios reales.

### 4.2. Herramientas

| Herramienta | Para qué sirve |
|---|---|
| **TikTok Creative Center** (gratis) | Ver anuncios y tendencias populares en TikTok por país y categoría. |
| **Meta Ad Library / Biblioteca de anuncios** (gratis) | Ver qué anuncios están activos en Facebook e Instagram. Si un anunciante mantiene un anuncio activo semanas o meses, probablemente le funciona. |
| **AutoDS** | Buscar productos, importarlos a Shopify y automatizar pedidos. |
| **DSers** | Importar productos y gestionar pedidos de dropshipping. |
| **Zendrop** | Proveedor con catálogo propio y opciones de envío más rápido. |

**Usa tu cuenta de Curso Dropshipping Gratis.** Como ya tienes cuenta en [cursodropshippinggratis.com](https://cursodropshippinggratis.com) y trabaja con AutoDS, puedes usar su **informe de productos**: desde la web, con un botón, te arma una lista de los mejores productos de AutoDS con su nota. Es un buen punto de partida para no empezar a ciegas. Después, valida cada candidato con la Biblioteca de anuncios y el Creative Center.

### 4.3. Método de investigación en 5 pasos

1. Genera el informe de productos en tu cuenta del curso.
2. Elige 10 candidatos y pásalos por los 7 criterios.
3. Busca cada uno en la Biblioteca de anuncios de Meta y en TikTok: ¿hay anuncios activos? ¿Comentarios de gente real?
4. Calcula el margen (sección 5). Descarta los que no den números.
5. Quédate con **3 productos** para probar.

> **Tarea:** genera tu informe de productos, filtra hasta 3 candidatos y anota para cada uno: costo, precio de venta estimado y un enlace a un anuncio de la competencia.

## 5. Una ficha de producto que vende

### 5.1. Fotos y video

1. Mínimo 5 imágenes: producto con fondo limpio, producto en uso, detalle, tamaño (con la mano o un objeto de referencia), qué incluye la caja.
2. Un video corto mostrando el producto funcionando.
3. Todas en el mismo formato (cuadradas) y buena luz.
4. No uses fotos de otras tiendas sin permiso.

### 5.2. Título

Claro y con el beneficio: "Organizador de cables magnético – Escritorio ordenado en 2 minutos". Evita mayúsculas en todo el título y promesas exageradas.

### 5.3. Descripción

Estructura simple:

1. **Una frase con el problema** que resuelve.
2. **3 a 5 beneficios** en lista (qué gana el cliente, no solo características técnicas).
3. **Especificaciones:** medidas, materiales, qué incluye.
4. **Envío y garantía** en una línea, con plazos reales.
5. **Preguntas frecuentes** del producto.

### 5.4. Precio y margen (con números)

Primero, tres términos:

- **Margen:** lo que te queda de cada venta después de pagar los costos del producto.
- **CPA** (costo por adquisición): lo que gastas en anuncios para conseguir **una** venta.
- **ROAS** (retorno sobre la inversión publicitaria): cuántos dólares vendes por cada dólar de anuncios. Se calcula como *ventas ÷ gasto en anuncios*.

**Ejemplo** (en dólares, vendiendo con plan Basic y pasarela externa):

| Concepto | Monto |
|---|---|
| Precio de venta | US$ 34,90 |
| Costo del producto (proveedor) | − US$ 9,00 |
| Envío | − US$ 5,00 |
| Comisión de la pasarela (aprox. 5 %) | − US$ 1,75 |
| Comisión de Shopify por pasarela externa (2 %) | − US$ 0,70 |
| **Margen por venta antes de anuncios** | **US$ 18,45** |

Ahora, el **punto de equilibrio**: el momento en que no ganas ni pierdes.

- **CPA de equilibrio = US$ 18,45.** Si cada venta te cuesta más que eso en anuncios, pierdes plata.
- **ROAS de equilibrio = 34,90 ÷ 18,45 = 1,89.** Necesitas vender al menos US$ 1,89 por cada dólar de anuncios para no perder.

Dos escenarios con US$ 150 de anuncios:

| Escenario | Ventas | CPA | ROAS | Resultado |
|---|---|---|---|---|
| A | 6 | 150 ÷ 6 = US$ 25 | 209,40 ÷ 150 = 1,40 | Pierdes US$ 6,55 por venta: **− US$ 39,30** |
| B | 10 | 150 ÷ 10 = US$ 15 | 349 ÷ 150 = 2,33 | Ganas US$ 3,45 por venta: **+ US$ 34,50** |

Ojo: todavía faltan los costos fijos (plan de Shopify, apps, dominio), las devoluciones y los impuestos. Por eso conviene que el precio de venta sea **al menos 2,5 a 3 veces** el costo del producto más el envío.

**Si vendes en Argentina en pesos**, haz la misma cuenta en pesos e incluye la comisión de Mercado Pago según el plazo que elijas y el IVA de esa comisión.

> **Tarea:** arma una planilla con la tabla del ejemplo y completa los números de tus 3 productos. Calcula el CPA y el ROAS de equilibrio de cada uno. Descarta los que tengan un ROAS de equilibrio mayor a 2,5.

## 6. Tráfico: cómo llevar gente a tu tienda

**Tráfico** son las visitas a tu tienda. Sin tráfico, no hay ventas, por linda que sea la tienda.

### 6.1. Tráfico orgánico (gratis)

**Orgánico** quiere decir que no pagas por mostrarlo: lo ven porque el algoritmo lo recomienda o porque te siguen.

1. **TikTok:** videos cortos mostrando el producto en uso, antes y después, reacciones, "3 usos que no conocías". Publica 1 a 3 por día durante las primeras semanas.
2. **Instagram Reels:** reutiliza los mismos videos (sin la marca de agua de TikTok).
3. **YouTube Shorts:** igual.
4. **Enlace en la bio** a la tienda o al producto.

Esto se conecta con los otros capítulos del curso: las mismas habilidades de crear contenido que usas para promocionar productos de Hotmart te sirven aquí. Incluso puedes combinar: una tienda de productos para cocina y un ebook de recetas en Hotmart para el mismo público.

### 6.2. Anuncios pagos (Meta y TikTok Ads)

Con anuncios pagas para que tu video aparezca a personas que todavía no te conocen.

**Mínimos verificados:**

- **TikTok Ads:** presupuesto mínimo de **US$ 50 por día por campaña** y **US$ 20 por día por grupo de anuncios**, según la ayuda oficial de TikTok.
- **Meta Ads (Facebook e Instagram):** el mínimo técnico citado por varias fuentes es de alrededor de **US$ 1 por día**, pero no lo pude confirmar en la ayuda oficial de Meta. Con tan poco presupuesto, la plataforma casi no aprende.

**Presupuesto de prueba realista (ejemplo):**

| Paso | Presupuesto | Duración |
|---|---|---|
| Producto 1: 3 a 5 videos distintos | US$ 10 a 15 por día | 5 a 7 días |
| Producto 2 | US$ 10 a 15 por día | 5 a 7 días |
| Producto 3 | US$ 10 a 15 por día | 5 a 7 días |
| **Total aproximado** | **US$ 150 a 300** | 3 semanas |

Para un principiante, **Meta** suele ser más accesible por su mínimo bajo. TikTok Ads exige más presupuesto diario.

**Reglas para la prueba:**

1. Antes de gastar, instala el **píxel** (un código que avisa a Meta o TikTok cuando alguien compra) desde las apps oficiales de Facebook & Instagram y TikTok en Shopify.
2. No cambies los anuncios todos los días: deja que corran al menos 3 días.
3. Si un producto gastó el equivalente a **2 veces tu CPA de equilibrio** sin ninguna venta, apágalo.
4. Si el ROAS supera tu ROAS de equilibrio varios días seguidos, sube el presupuesto de a poco (20 % cada 2 o 3 días).
5. **Nunca** gastes en anuncios plata que necesitas para vivir.

**Nota para Argentina:** si pagas los anuncios con una tarjeta argentina en dólares, pueden aplicarse percepciones impositivas que encarecen la inversión. Pregunta a tu banco o contador cómo conviene pagar.

> **Tarea:** publica 10 videos orgánicos de tu producto en 10 días. Mira cuál tiene más visualizaciones y guardados: ese es tu mejor candidato para un anuncio.

## 7. Atención al cliente, devoluciones y reputación

1. **Responde rápido:** dentro de las 24 horas, idealmente en el día. Un botón de WhatsApp ayuda mucho.
2. **Envía el número de seguimiento** apenas lo tengas. La mayoría de los mensajes son "¿dónde está mi pedido?".
3. **Respuestas preparadas** para las 5 preguntas más comunes (envío, demora, cambio, reembolso, uso del producto).
4. **Devoluciones:** en dropshipping, devolver el producto al proveedor muchas veces cuesta más que el producto. Muchas tiendas reembolsan sin pedir la devolución cuando el monto es bajo. Decide tu regla antes de vender y escríbela en la política.
5. **Reembolsos:** cumple lo que dice tu política. Si el cliente pide un **contracargo** (reclamo al banco), puedes perder el dinero y la pasarela puede limitar tu cuenta. Es mejor reembolsar a tiempo.
6. **Reseñas:** pide opinión a cada cliente unos días después de recibir el producto. **Nunca** inventes reseñas: es engañoso, puede ser ilegal y destruye la confianza.
7. **En Argentina**, respeta los 10 días de arrepentimiento y el botón de arrepentimiento.

> **Tarea:** escribe tus 5 respuestas preparadas y la regla de devoluciones de tu tienda.

## 8. Plan de 60 días, errores comunes y expectativas

### 8.1. Plan de 60 días

| Semana | Objetivo | Acciones |
|---|---|---|
| 1 | Decidir | Elegir modelo, país de venta y pasarela. Abrir la prueba de Shopify. |
| 2 | Tienda base | Tema, páginas obligatorias, pasarela, envíos. Compra de prueba. |
| 3 | Productos | Informe de productos en tu cuenta del curso. Filtrar a 3. Calcular márgenes. |
| 4 | Fichas | Importar los 3 productos, fotos, títulos, descripciones, precios. |
| 5 | Orgánico | 1 a 3 videos por día en TikTok, Reels y Shorts. Medir cuáles funcionan. |
| 6 | Preparar anuncios | Instalar píxel. Elegir los 3 a 5 mejores videos. Fijar presupuesto de prueba. |
| 7 | Prueba producto 1 y 2 | Anuncios con presupuesto chico. Anotar CPA y ROAS todos los días. |
| 8 | Prueba producto 3 | Igual. Apagar lo que no funciona. |
| 9 (días 57 a 60) | Decidir | Si algún producto superó el ROAS de equilibrio, mejorar su ficha y escalar de a poco. Si ninguno, volver a la semana 3 con lo aprendido. |

### 8.2. Errores comunes

1. **Pasar semanas perfeccionando el diseño** sin tener producto ni tráfico.
2. **Elegir el producto porque te gusta a ti**, no porque los datos lo respalden.
3. **No calcular el margen** antes de anunciar.
4. **Prometer envíos rápidos** que el proveedor no cumple.
5. **Hacer dropshipping desde el exterior a clientes argentinos** sin entender la aduana.
6. **Instalar 20 apps:** tienda lenta y gastos mensuales altos.
7. **Copiar fotos y textos** de otras tiendas.
8. **Apagar un anuncio a las 6 horas** o dejarlo gastar sin control semanas.
9. **No guardar plata para los reembolsos.**
10. **Olvidarse de los impuestos.**

### 8.3. Expectativas realistas

- Es normal que la tienda **no venda en el primer mes**. Eso no significa que fracasaste: significa que todavía estás probando.
- La mayoría de los productos que pruebes **no van a funcionar**. Es parte del método: pruebas barato, descartas rápido y sigues.
- Considera el dinero de la prueba (plan, apps, anuncios) como el **costo de aprender**. Fija un tope antes de empezar y respétalo.
- Si después de 60 días no encontraste un producto rentable, igual saliste con habilidades útiles: crear contenido, leer números y armar una tienda.

> **Tarea:** escribe tu tope de inversión total para estos 60 días y pégalo donde lo veas.

## 9. Aspectos legales e impositivos básicos en Argentina

> **Advertencia:** esto es información general, no asesoramiento profesional. **Consulta a un contador antes de vender.**

1. **Inscripción en ARCA:** para vender de forma habitual necesitas estar inscripto, normalmente en el **monotributo** al empezar. Para noviembre de 2026, según medios especializados, el tope anual de la categoría A es de **$ 12.009.410,45** y el máximo del monotributo (categoría K) es de **$ 126.610.838,75**. Verifica en [arca.gob.ar](https://www.arca.gob.ar).
2. **Facturación:** cada venta a un consumidor en Argentina lleva factura (en monotributo, Factura C).
3. **Ventas al exterior:** si vendes a clientes de otros países, el tratamiento puede ser distinto (exportación). Las mercaderías físicas que salen de Argentina tienen trámites aduaneros; el dropshipping entre un proveedor extranjero y un cliente extranjero es un caso particular que tu contador tiene que analizar.
4. **Ingresos brutos:** además de ARCA, cada provincia cobra Ingresos Brutos (en monotributo suele estar unificado, según la provincia).
5. **Defensa del consumidor:** derecho de arrepentimiento de 10 días, botón de arrepentimiento, información clara de precios y condiciones.
6. **Importaciones:** si traes stock, consulta los regímenes de courier e importación vigentes y si necesitas inscribirte como importador.
7. **Otros países de LatAm:** en México, por ejemplo, el RESICO es un régimen frecuente para personas que empiezan; en otros países existen regímenes simplificados parecidos. Consulta a un contador local.

> **Tarea:** agenda una consulta con un contador y lleva estas preguntas: ¿en qué categoría del monotributo me inscribo? ¿Cómo facturo ventas locales y al exterior? ¿Qué obligaciones tengo como tienda online?

## 10. Fuentes

Consultadas el 28 de noviembre de 2026. Algunas páginas oficiales no se pudieron abrir directamente y se verificaron a partir de los resultados de búsqueda: confirma los valores en la fuente oficial.

**Shopify (oficial):**

- [Planes y precios de Shopify (español)](https://www.shopify.com/es/precios) y [versión España](https://shopify.com/es-es/precios)
- [Planes y precios (México)](https://www.shopify.com/mx/precios)
- [Países admitidos para Shopify Payments](https://help.shopify.com/es/manual/payments/shopify-payments/supported-countries)
- [Shopify Payments disponible en México (changelog)](https://changelog.shopify.com/posts/shopify-payments-available-in-mexico)
- [Mercado Pago: métodos de pago (blog de Shopify)](https://www.shopify.com/es/blog/mercado-pago-metodos-de-pago)
- [Integraciones de proveedores de pagos (Shopify México)](https://www.shopify.com/mx/aceptar-pagos-en-linea)
- [Centro de ayuda de Shopify](https://help.shopify.com/es)
- [Comunidad Shopify: pagos en Argentina](https://community.shopify.com/t/shopify-payments-mercadopago-pagos-argentina/191541)

**Pagos y anuncios:**

- [Mercado Pago Developers: integración con Shopify](https://www.mercadopago.com.ar/developers/en/docs/shopify/overview.md)
- [iProfesional: comisiones y plazos de Mercado Pago](https://www.iprofesional.com/tecnologia/386153-mercado-pago-que-debes-saber-sobre-comisiones-plazos-y-montos)
- [TikTok Ads Manager: presupuestos](https://ads.tiktok.com/help/article/budget?lang=en)
- [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter)
- [Biblioteca de anuncios de Meta](https://www.facebook.com/ads/library)

**Aduana y comercio exterior:**

- [ARCA: Régimen de Courier](https://servicioscf.afip.gob.ar/publico/sitio/contenido/novedad/ver.aspx?id=5939)
- [Impuestito: compras del exterior en 2026, franquicia y courier](https://impuestito.org/blog/impuestos-en-compras-del-exterior-argentina-2026-franquicia-y-courier)
- [Tiendanube: cómo importar en Argentina](https://www.tiendanube.com/blog/como-importar-en-argentina/)
- [Federal Register (EE. UU.): suspensión indefinida de "de minimis", junio de 2026](https://www.federalregister.gov/documents/2026/06/24/2026-12670/indefinite-suspension-of-the-de-minimis-exemption-for-merchandise-arriving-through-all-modes-other)

**Impuestos en Argentina (verificar con un contador):**

- [ARCA – sitio oficial](https://www.arca.gob.ar)
- [iProfesional: topes del monotributo en noviembre de 2026](https://www.iprofesional.com/impuestos/468898-monotributo-como-quedan-los-topes-de-facturacion-y-los-montos-de-noviembre)

**Tu cuenta del curso:**

- [Curso Dropshipping Gratis](https://cursodropshippinggratis.com): informe de productos (AutoDS) y diseño de la tienda.
