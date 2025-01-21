# PROYECTO INDIVIDUAL 1 (DATA ANALYTICS)

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

Muy bien


