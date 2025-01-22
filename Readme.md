<p align='center'>
<img src ="https://assets.datamation.com/uploads/2023/08/dm08172023-what-is-data-analytics-1024x670.png">
<p>


<h1 align='center'> 
 <b> PROYECTO INDIVIDUAL 2 (DATA ANALYTICS)</b> 
</h1>

Bienvenidos a la presentación de mi segundo proyecto individual para la carrera de Data Science en Henry.
En esta ocasión abordaremos el rol de un Data Analytics para la interpretación de los datos, poder contar que nos dicen, que podemos extraer de la información visual que se presenta por medio de los Dashboard.

Nos centraremos en la conectividad de Argentina, men concreto, a la red de telecomunicaciones, abarcando temas como:
1. Los tipos de conectividad que se encuentran en cada provincia.
2. Como se ha comportado el crecimiento de las conectividades a lo largo de los años 
3. Identificar puntos claves que nos puedan ayudar la toma de decisiones.

Esto y otros puntos los abordaremos a lo largo de este segundo proyecto.

## Herraminetas y tecnologias aplicadas en el proyecto
En el desarollo de este proyecto apliqué las siguientes herramientas:
* Pandas: para la manipulacion de los datos y el analisis
* Numpy: para los calculos numericos eficientes. el manejo de arreglos y operaciones matematicas.
* matplotlib.pyplot: para poder plasmas los datos en forma de graficas y hacer el entendimiento o analisis mas descriptivo.
* Seaborn: Un complemento para o herramienta mas avanzada para la visaluizacion de la infromacion en graficas, poroporciona el uso de graficos mas atractivos y faciles de entender.

Para el caso del EDA correspondiente a **Mapa de conectividad** he utilizado un archivo llamado "provinciaPolygon.shp para poder representar por medio de un mapa de Argentina y sus provincias la distribucion de los tipos de conectividad distribuidos a lo largo de cada una de las provincias que la componen.

Para ello he usado la libreria de **Geopandas** que es por asi llamarlo un complemento de Pandas para poder incluir datos geoespaciales, lo que me permitio poder trabajar con datos como lo fue ubicar los puntos por medio de las referencias geograficas que se muestran en el dataset, pero tambien junto a ello tambien hice uso de **shapely.geometry.Point** lo que proporciona una forma de representar y manipular puntos geometricos, que son un tipo de geometria espacial.



## EDA (Exploratory Data Analysis)

Aunque en los datos provistos comprenden varios archivos excel con varias hojas dentro, en mi caso solo me he centrado en los siguientes archivos y sus hojas correspondientes:
1. Internet
    * Velocidad sin rangos 
    * Totalev VMD
    * Totales Dial-BAf
    * Penetración Totales
    * Ingresos

2. Telefonia movil

3. Mapa Conectividad

Estos son los archivos con los que estuve trabajando para el desarrollo de este proyecto.

Muy bien, ahora viene el proceso de un pequeño ETL, si bien los datos practicamente no requieren limpiezas o transformaciones, si que podemos realizar un analisis pequeño para poder encontar  búsqueda de valores faltantes, valores atípicos/extremos u outliers y registros duplicados.
Este pequeño analisis se encuentran dentro de los archivos EDA correspondientes.

Los EDAs los pueden encontrar dentro de la carpeta **notebooks** e ir corriendo cada bloque de codigo para realizar los pasos correspondientes.

## KPI 
Para la realizacion de los KPI he decidido tomar como mas relevantes el acceso a internet por provincias, la cobertura de conectividad por provincias, la telefonia movil y el acceso de television, considero a mi punto de vista que estos son los que mas relevancia le encuentro principalmente por los grandes cambios tecnologicos y de conectividad se refieren.

En cada uno de los KPI detallo puntos clave, factores que pueden influir en los resultados obtenidos y posibles tomas de decisiones que pueden mejorar, matener o ganar en refencia a lo que se analiza.

Cada KPI se encuentra dentro de la carpeta llamada **KPI** en donde podra ver con mas detalle los resultados.
El uso de estos KPI a diferencia de otras métricas es que dan una métrica clave para medir el progreso hacia un objetivo estratégico de algún proyecto o negocio.
Estos tienen un enfoque limitado y priorizado, pues proporcionan una visión clara del éxito en un área clave. 
En resumen, un KPI requiere de un análisi cuidadoso para asegurarse de que reflejen lso objetivos estratégicos.

## Dashboard
El dashboard abarca de manera enfatizada los KPI que se desarrollaron, ayudando a comprender mejor los puntos claves oestratégicos. 

Proveen una mejor comprensión de lo que se focalizan dichos KPI.


