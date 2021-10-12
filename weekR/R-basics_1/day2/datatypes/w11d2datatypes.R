# WEEK 11 - day 2 DATATYPES


# Si necesitas informacion sobre una funcion
# ?(funcion)
# help(funcion)

ls()

##############
# VARIABLES  #
##############

## assignment operator
a <- 10 # el mas utilizado
b = TRUE
"hello" -> c

d <- 2.5
e <- 5L

## que tipo de variable es?
  
class(c)

is.logical(b)

print(1/0)


#############
# VECTORES  #
#############

## CREAR VECTORES 

# crear vector caracter con nombre de peliculas
nombre_peliculas <- c("El diario de Noa", "Pocahontas", "Jojo Rabbit", "Joker")

# crear vector numerico con puntuacion de las peliculas
puntuacion <- c(7.9,7.2,6.1,6.3)

# crear vector logico sobre si la pelicula es posterior a 2015
posterior_2005 <- c(FALSE,FALSE,TRUE,TRUE)

# poner nombre a un vector
some_vector <- c("Clara Piniella", "TA")
names(some_vector) <- c("Name", "Profession")

## OPERACIONES CON VECTORES

# sumar 2 a la puntuaciOn
puntuacion + 2

# dividir la puntuaciOn entre 2
puntuacion/2

# crear otro vector con mi puntuacion
puntuacion_de_clara <- seq(7,10)

# calcular diferencia entre puntuaciones
puntuacion_de_clara - puntuacion

# calcular la longitud del vector
length(puntuacion)

# calcular el promedio del vector puntuacion
mean(puntuacion)

## SUBCONJUNTO

## seleccion basada en posicion
# seleccionar la tercera pelIcula
nombre_peliculas[3]
nombre_peliculas

# seleccionar la primera y la última pelicula
nombre_peliculas[c(1,4)]

## seleccion basada en condicion logica (mascara)
## los operadores comparadores son iguales que en Python

###################################
# < for less than                 #
# > for greater than              #
# <= for less than or equal to    #
# >= for greater than or equal to #
# == for equal to each other      #
# != not equal to each other      #
###################################

# crear condicion logica
puntuacion_7 <- puntuacion < 7

# mostrar condicion para ver TRUE/FALSE
puntuacion_7 

# mostrar puntuaciones bajas
puntuacion[puntuacion_7]

# tambien
puntuacion[puntuacion < 7]

# mostrar nombres de peliculas con puntuaciones bajas
nombre_peliculas[puntuacion_7]

## ELIMINAR DATOS NULOS

# de un vector
nanes <- c(1, 2,NA,4,NA)

bad <- is.na(nanes)
bad
nanes[!bad]

otro_nanes <- c("a","b", NA, "p",NA)

# de mas de uno
good <- complete.cases(nanes, otro_nanes) # misma longitud
good

nanes[good]
otro_nanes[good]

## LOS VECTORES NO PUEDEN TENER OBJECTOS DE DIFERENTE TIPO

otro_vector <- c(1,2,5,"hola")
vector_log <- c(TRUE, 2) ### TRUE en R es tambien interpretado como 1 
ahora_vector <- vector("numeric", length = a) # valor por defecto 0

## pasar de un tipo a otro
as.character(ahora_vector)

#############
# FACTORES  #
#############

# crear vector de ventas
tallas <- c('m', 'g', 'P', 'P','m', 'M')

# intentar graficar
# error, son caracteres 
plot(tallas)

## CREAR FACTORES

# crear factor de un vector
# cuenta cuantas veces se repite cada elemento
tallas_factor <- factor(tallas)

# graficar factor
plot(tallas_factor)

# mirar niveles de factor
levels(tallas_factor)

## RECODIFICAR FACTORES

# creando factor recodificado
tallas_recodificado <- factor(tallas,
                              levels = c("g", "m", "M", "P"),
                              labels = c("G", "M", "M", "P"))



# graficando ventas_recodificado
plot(tallas_recodificado)

## ORDENAR LOS NIVELES DE UN FACTOR

# ordenando niveles 
tallas_ordenado <- factor(tallas,
                          ordered = TRUE,
                          levels = c("P", "m", "M", "g"),
                          labels = c("P", "M", "M", "G"))


# viendo el orden en los niveles
summary(tallas_ordenado)


# graficando el factor ordenado
plot(tallas_ordenado)

## EXTRA

survey_vector <- c("M", "F", "F", "M", "M")
factor_survey_vector <- factor(survey_vector)
levels(factor_survey_vector) <- c("Female", "Male")
factor_survey_vector

# generar un resumen del contenido del vector
summary(survey_vector)

# resumen del contenido del factor
summary(factor_survey_vector)

# saca la frecuencia de cada label
table(factor_survey_vector)

# convierte las labels a valores numericos
unclass(factor_survey_vector)


#############
# MATRICES  #
#############

## CREAR MATRICES

# crear vectores para las columnas de la matriz
warner <- c(20,20,16,17,17,22,17,18,19)
disney <- c(11,13,11,8,12,11,12,8,10)
fox <- c(18,15,15,15,16,17,15,13,11)

# creando matriz a partir de vectores
peliculas <- matrix(c(warner,disney,fox), nrow = length(warner), ncol = 3)

# imprimir matriz en consola
peliculas

# agregar nombres de columnas
colnames(peliculas)<- c("warner", "fox", "disney")

# agregar nombres de filas
rownames(peliculas)<-c('2010','2011','2012', '2013','2014', '2015', '2016', '2017','2018')

# imprimir matriz por segunda vez
peliculas

# dimensiones de la matriz
dim(peliculas)

# resumen estadístico
summary(peliculas)


## OPERACIONES ARITMETICAS CON MATRICES

# resta 5 a la matriz
peliculas - 5

# sumar matriz consigo misma
peliculas + peliculas

# crear la matriz matriz_18
matriz_18 <- matrix(1:18, nrow = 9, ncol = 3)

# añadir nombres a la matriz
dimnames(matriz_18) <- list(c("c", "d", "e", "f", "g", "h", "i", "j", "k"), c("a", "b", "c"))


# multiplicar la matriz por matriz_18
peliculas * matriz_18


## SUBCONJUNTOS DE UNA MATRIZ

# seleccionar un elemento de la matriz
peliculas[3,2]
peliculas["2012", "fox"]


# seleccionar mas de un elemento de la matriz
peliculas[c(3,2), c(2,3)]
peliculas[c(3,4), c("disney", "fox")]


# selecciona las tres primeras filas y las dos ultimas
peliculas[1:3,2:3]


# seleccionar una fila 
peliculas[3,]
peliculas["2010",]


# seleccionar una columna
peliculas[,"fox"]
peliculas[,2]


## EXTRA

# crear matriz 
ventas <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8, 565.89, 78.98, 344.3, 590.99, 100.00, 345.67, 321.4, 890.99, 33.33, 789.12, 678.345)
ventas_worlwide <- matrix(ventas, nrow = 9, byrow = TRUE,
                           dimnames = list(c("Naranjas", "Peras", "Platanos", "Uvas", "Mangos", "Papaya", "Kiwis", "Ciruelas", "Tomates"), 
                                           c("US", "non-US")))

ventas_worlwide
# calcular el numero de ventas en US y fuera
worldwide_vector <- colSums(ventas_worlwide)

# concatenando dos matrices y un vector
big_matrix <- cbind(ventas_worlwide, peliculas, ventas[1:9])

data.frame(big_matrix)
data.matrix(big_matrix)

###############
# DATAFRAMES  #
###############

# utilizamos los vectores nombre_peliculas, puntuacion y posterior_2005

## CREAR DATAFRAME

# crear dataframe de vectores
peliculas_df <- data.frame(nombre_peliculas,
                           puntuacion, 
                           posterior_2005)

# mostrar los dos primeros filas del dataframe
head(peliculas_df, 2)

# cambiar nombre de dataframe
names(peliculas_df) <- c('NOMBRE','PUNTUACION','AFTER 2007')

# mostrar dataframe ahora (head y tail muestran 6 elementos)
head(peliculas_df)
tail(peliculas_df)

## SUBCONJUNTO 

# hacer un subset si la putnuacion de la pelicula es mayor a 7
subset(peliculas_df, PUNTUACION > 7)

# tambien
peliculas_df[peliculas_df$PUNTUACION > 7,]

# seleccionar un elemento del dataframe
peliculas_df[3,2]
peliculas_df[3,'PUNTUACION']


# seleccionar mas de un elemento del dataframe
peliculas_df[c(3,4), c(2,3)]
peliculas_df[c(3,2), c('PUNTUACION','AFTER 2007')]

# seleccionar una fila del dataframe
peliculas_df[1,]

# seleccionar una columna del dataframe
peliculas_df[,2]
peliculas_df[,'PUNTUACION']
peliculas_df$PUNTUACION

## ORDENAR DATAFRAME

# mostrar el dataframe
peliculas_df

# mostrar el indice de la columna de puntuacion con order
order(peliculas_df$PUNTUACION)

# esto hace lo mismo que lo de arriba
# funcion order (menor a mayor)
orden_m_m <- order(peliculas_df$PUNTUACION,
                   decreasing = FALSE)


# mostrar el dataframe ordenado
peliculas_df[orden_m_m,]

# funcion order (mayor a menor)
orden_lol <- order(peliculas_df$PUNTUACION,
                   decreasing = TRUE)


# mostrar el dataframe ordenado
peliculas_df[orden_lol,]

# guardar el dataframe ordenado
df_ordenado <- peliculas_df[orden_lol,]


## ELIMINAR DATOS NULOS

# airquality junto con mtcars, y otras, son datasets que 
# vienen incluidos en paquetes basicos de R,
# que se importan con la funcion data("el_nombre")
data("airquality")

head(airquality)

good_air <- complete.cases(airquality)

airquality[good_air,]


###########
# LISTAS  #
###########

# utilizamos nombre_peliculas, puntuacion, posterior_2005, warner, disney, fox, peliculas, peliculas_df

## CREAR UNA LISTA 

# crear lista con un vector y una matriz
lista_curso <- list(nombre_peliculas, peliculas)

# mostrar lista
lista_curso

# cambiar nombre de lista
names(lista_curso) <- c('vector', 'matriz')


# mostrar lista 
lista_curso

# para mostrar la estructura interna del objeto
str(lista_curso)

## SELECCIONAR ELEMENTOS DE UNA LISTA

# Seleccionar vector de la lista
lista_curso[['vector']]

# con $
lista_curso$vector

# Seleccionar el tercer elemento del vector de la lista
lista_curso[['vector']][3]

# Seleccionar fila 5 y columna 3 de la matriz de la lista
lista_curso[['matriz']][5,3]

## AGREGAR/ELIMINAR ELEMENTOS DE UNA LISTA

# agregar dataframe a lista
lista_curso[['data_frame']] <- peliculas_df 

# revisar que esta el dataframe
lista_curso

# eliminar un elemento de lista
lista_curso[['vector']] <- NULL

# revisar que no este el vector
lista_curso


## OTRAS FUNCIONES DE INTERES PARA LISTAS

li <- list(clara = TRUE,
           cristina = "hello",
           int_vec = sort(rep(seq(8,2,by=-2),times=2))
           )

is.list(li)

is.list(otro_vector)

li2 <- as.list(otro_vector)

is.list(li2)

lista_doble <- append(li,rev(li))

str(rev(li))

# convierte la lista a vector
unlist(li)













