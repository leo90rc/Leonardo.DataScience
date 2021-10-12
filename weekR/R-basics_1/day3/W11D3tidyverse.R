# WEEK 11 - day 3 Tidyverse

# para instalar una paquete que no tengais instalada
# install.packages("tidyverse")

# http://www.sthda.com/english/wiki/r-built-in-data-sets
# para ver todos los datasets cargados 
# en R
data()

#data(mtcars)
#head(mtcars)

# eliminar variables ya creadas

rm(mtcars)

##############
# Tidyverse  #
##################################################
# Un paquete para transformar y visualizar datos #
##################################################

# cargamos o bien 
# library(tidyr)
# library(dplyr)
# library(ggplot2)

# o que importará todas los paquetes  
library(tidyverse)

## En este caso vamos a trabajar con el dataset de gapminder
## Para ello vamos a instalar un paquete que tiene el mismo
## nombre

# instalando paquete con los datos
# install.packages("gapminder")

# data(gapminder)
# este gapminder es el que viene con el paquete `.`
# que no es lo mismo que el gapminder que viene con
# el paquete `gapminder`

# cargando paquete con los datos
library(gapminder)

# cargando datos a entorno
data(gapminder)

gapminder
# cargando datos a entorno
head(gapminder)

####################
# filter con dplyr #
####################

# filtrar datos por pais sin %>% 
filter(gapminder, country == 'Mexico')

# filtrar datos por pais
# para hacer %>% en RStudio (cntrl + shift + M)
gapminder %>% 
  filter(country == 'Mexico')
# coge lo que hay a la izquierda y lo pasa la derecha como primer argumento

# filtrar datos por año
gapminder %>% 
  filter(year == 2002)

# filtrar datos por año y pais
gapminder %>%
  select(continent, country, year) %>% 
  filter(continent == "Europe", year==2007, country == "Spain") 
# select si solo quisieramos mostrar las columnas country y year

# filtrar paises con esperanza de vida 
# menor o igual a 40 y el año en 2002
gapminder %>% 
  filter(lifeExp <= 40, year == 2002)

# ejemplo para añadir or  |
# filter(starwars, hair_color == "none" | eye_color == "black")

#####################
# arrange con dplyr #
#####################

# filtrar año 2002 y ordenar por gdpPercap
gapminder %>%
  filter(year == 2002) %>%
  arrange(desc(gdpPercap))
# si queremos que sea de forma descendente añadimos arrange(desc())

#######################
# summarise con dplyr #
#######################

# cantidad de paises en Asia
gapminder %>% # el pipe se pone usando Ctrl+Shift+M
  filter(continent == 'Asia',
         year =='2007') %>% 
  summarise(conteo = n())
# conteo es un nombre que nosotros elegimos para darle a esa variable
# conteo no es una funcion

# maxima esperanza de vida
gapminder %>% 
  summarise(max_lifeExp = max(lifeExp))


#####################
# groupby con dplyr #
#####################
# summarise() and summarize() are synonyms.

gapminder %>%
  group_by(continent) %>% 
  summarise(medianLifeExp = median(lifeExp),
            maxGdpPercap = max(gdpPercap))

# agrupando esperanza de vida promedio por año
plot(
  gapminder %>% 
    group_by(year) %>% 
    summarise(prom_vida = mean(lifeExp)))

####################
# mutate con dplyr #
####################

gapmindermutado <- gapminder %>%
  mutate(pop = pop/1000000)

gapminder %>%
  mutate(gdp = gdpPercap*pop)

####################
# select con dplyr #
####################

gapminder %>%
  filter(year == 2007) %>%
  mutate(lifeExpMonths = 12 * lifeExp) %>%
  arrange(desc(lifeExpMonths)) %>%
  select(continent, year)

###################
# count con dplyr #
###################

# número de países que hay en el conjunto de datos para el año 2002
# ordenamos por esta cuenta
gapminder %>%
  filter(year == 2002) %>%
  group_by(continent) %>% 
  summarise(counting = n())


gapminder %>%
  filter(year == 2002) %>%
  count(continent)
# count es como hacer un value_counts() en pandas

####################
# plot con ggplot2 #
####################

by_year <- gapminder %>%
  group_by(year) %>% 
  summarise(medianLifeExp = median(lifeExp),
            maxGdpPercap = max(gdpPercap))

# crear un scatter plot mostrando el cambio de medianLifeExp 
# a lo largo de los años
ggplot(by_year, aes(x = year, y = medianLifeExp)) +
  geom_point() 


gapminder %>%
  group_by(year) %>% 
  summarise(medianLifeExp = median(lifeExp),
            maxGdpPercap = max(gdpPercap)) %>% 
  ggplot(aes(x = year, y = medianLifeExp)) +
  geom_point()

# 

gapminder %>% 
  filter(year == 2002) %>% 
  ggplot(aes(x = pop, y = lifeExp, colour = continent)) +
  geom_point() +
  # sale_x_log10 es algo específico para estos datos
  # cambia la escala de x
  scale_x_log10() +
  facet_wrap(~ continent) # separa subplots por continente
  # ~ esto es una virgulilla

# %in% se usa para identificar si un elemento 
#pertenece a un vector o dataframe

gapminder %>%
  # Get the start letter of each country
  mutate(startsWith = substr(country, start = 1, stop = 1)) %>%
  # Filter countries that start with "A" or "Z"
  filter(startsWith %in% c("A", "Z")) %>%
  # Make the plot
  ggplot(aes(x = year, y = lifeExp, color = continent)) +
  geom_line() +
  facet_wrap( ~ country)

# Comparando el PIB pc en los continentes
gapminder %>% 
  filter(year == 2002) %>% 
  ggplot(aes(x = continent, y = gdpPercap)) +
  geom_boxplot() +
  #scale_y_log10() +
  ggtitle("Comparing GDP per capita across continents")

# Comparando el PIB pc en los continentes
# Con funcion
gdp_year <- function(parametro_year) {
  gapminder %>% 
    filter(year == parametro_year) %>% 
    ggplot(aes(x = continent, y = gdpPercap)) +
    geom_boxplot() +
    scale_y_log10() +
    ggtitle(paste("Comparing GDP per capita across continents in", parametro_year))
}

gdp_year(1952)

## Gráficos más complejos y CHULOS
# install.package("gganimate")
library(gganimate)
library(gifski)

# gráfica de puntos que muestre la esperanza
# de vida a lo largo de los años

uno <- gapminder %>% 
  group_by(year, continent) %>% 
  summarize(mean_life = mean(lifeExp)) %>% 
  ggplot(aes(x=year,
             y=mean_life,
             color =continent)) +
  geom_line(size = 2) +
  geom_point(size =4)+
  labs(title = "Esperanza de vida en {frame_along}",
       x = "Fecha",
       y = "Años de vida")+
  theme_minimal()+
  transition_reveal(year)

animate(uno, renderer = gifski_renderer()) 

dos <- ggplot(
  gapminder,
  aes(x = gdpPercap, y=lifeExp, size = pop, colour = country)
) +
  geom_point(show.legend = FALSE, alpha = 0.7) +
  scale_color_viridis_d() +
  scale_size(range = c(2, 10)) +
  scale_x_log10() +
  labs(x = "GDP per capita", y = "Life expectancy")

animate(dos + transition_time(year), renderer = gifski_renderer())

#######
# EDA #
#######

#Resumen estadístico

summary(gapminder)

# Distribuciones de frecuencia 

hist(gapminder$lifeExp)


ggplot(data = gapminder,
       mapping = aes(x = gdpPercap)) +
  geom_histogram(binwidth = 100)

# Percentiles y Boxplots

boxplot(gapminder$lifeExp)

ggplot(data = gapminder,
       mapping = aes(x = pop, y = lifeExp)) +
  #geom_boxplot() +
  geom_violin()

# Correlaciones y dispersión
# https://www.tylervigen.com/spurious-correlations

ggplot(data = gapminder,
       mapping = aes(x = pop, y = lifeExp)) +
  geom_point() +
  geom_smooth()

# Otros graficos de interes

install.packages("PerformanceAnalytics")
library("PerformanceAnalytics")
chart.Correlation(gapminder[,3:6], histogram=TRUE, pch="+")

#install.packages("corrplot")
library(corrplot)
M <- cor(gapminder[,3:6])
corrplot(M, method = "circle")
#https://cran.r-project.org/web/packages/corrplot/vignettes/corrplot-intro.html










          















