# WEEK 11 - day 3 Read data

#############
# Read data #
#############

### IMPORTAR CSV CON INTERFAZ RSTUDIO
# ir a File > Import Dataset > From Text (readr)

### IMPORTAR CSV CON CÓDIGO R

# buscar la ruta del archivo de csv
file.choose()

# Copiar ruta de la consola y guardar en variable
ruta_csv <- "C:\\Users\\clara\\Desktop\\R-basics\\day3\\data\\alumnos.csv"

## elegir bien mi CARPETA DE TRABAJO ORIGEN

getwd() # ¿Cual es mi working directory?

setwd("C:\\Users\\clara\\Desktop") # Cambio mi working directory

getwd()

setwd("C:\\Users\\clara\\Desktop\\R-basics\\day3")

getwd()

# leer los datos

datos <- read.csv("data/alumnos.csv", header = TRUE, sep = ",")
datos

#######
# EDA #
#######

## Dividimos la columna nombre en nombres y apellidos
## Dividimos la columna fecha en dia, mes y año

## Usando la funcion gather de tidyr pasamos las columnas 
## matematica e inglés como observaciones de la variable Materia y
## los puntos como observaciones de la variable Puntos

# por defecto, separate() separa tomando como separador aquello que usando 
# REGEX haga match con cualquier valor que no sea alfanumerico 
dfc <- datos %>% 
  separate(nombre, into = c("Apellido", "Nombre")) %>% 
  separate(fecha, into = c("Dia", "Mes", "Año"), convert = TRUE) %>% 
  gather(Materia, Puntos, matematica, ingles)

# A partir de este nuevo dataframe queremos conocer la media por asignatura

dfc %>% 
  group_by(Materia) %>% 
  summarise(promedio = mean(Puntos))

# A partir de este nuevo dataframe queremos conocer la media por asignatura

dfc %>% 
  group_by(Materia, Nombre, Apellido) %>% 
  summarise(promedio = mean(Puntos))

# La media de puntos en ingles por alumno

dfc %>% 
  filter(Materia == "ingles") %>% 
  group_by(Nombre, Apellido) %>% 
  summarise(promedio = mean(Puntos))

# La media de puntos en matematicas por alumno

dfc %>% 
  filter(Materia == "matematica") %>% 
  group_by(Nombre, Apellido) %>% 
  summarise(promedio = mean(Puntos))

# Lo mismo pero esta vez ordenamos las filas por los valores de la 
# columna Media

dfc %>% 
  filter(Materia == "matematica") %>% 
  group_by(Nombre, Apellido) %>% 
  summarise(Media = mean(Puntos)) %>% 
  arrange(desc(Media))

# Graficamos para ver la evolución de las medias 
# por cada mes, para cada asignatura

dfc %>% 
  group_by(Materia, Mes) %>% 
  summarise(Media = mean(Puntos)) %>% 
  ggplot() +
  geom_line(mapping = aes(x=Mes, y=Media,
                          group = Materia,
                          color = Materia)) +
  labs(title = "Media mensual por asignatura")