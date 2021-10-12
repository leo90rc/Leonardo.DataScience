# WEEK 11 - day 3 Caret

library(caret)
library(ggplot2)

#####################
# Linear Regression #
#####################

data(mtcars)
?mtcars
# mpg --> Miles/(US) gallon <-- variable dependiente (a predecir)
# wt --> Weight (1000 lbs) <-- variable independiente

set.seed(333)

# ploteamos ambas variables

plot(x = mtcars$wt, y =mtcars$mpg)

# creamos la regresión linear con R

fit <- lm(mpg ~ wt, data = mtcars)

# ploteamos el modelo generado
# abline -> This function adds one or more straight lines through the current plot.
abline(fit)

# para conocer los datos de entrenamiento
summary(fit)

# añadimos la ecuacion al plot
bs <- round(coef(fit), 3) 
lmlab <- paste0("mpg = ", bs[1],
                ifelse(sign(bs[2])==1, " + ", " - "), abs(bs[2]), " wt ")
mtext(lmlab, 3, line=-2) 


## USANDO CARET

# dividimos train/test
# indicamos cual es la variable a predecir
inTrain <- createDataPartition(y = mtcars$mpg, p = 0.6, list = FALSE)
training <- mtcars[inTrain,]
test <- mtcars[-inTrain,]

dim(training)
dim(test)

# ploteamos los datos de entrenamiento
plot(x= mtcars$wt, y = mtcars$mpg)

# entrenamos el modelo
# el resultado sera similar a lo hecho anteriormente
fit_train <- train(mpg ~ wt, data= training, method = 'lm', metric="RMSE")
fit_train$finalModel

# ploteamos el modelo generado
pred_carstrain <- predict(fit_train, newdata = training)
lines(x = training$wt, y = pred_carstrain)

# calculamos el error RMSE
cal_rmse <- RMSE(pred_carstrain, training$mpg)

# predecimos con el conjunto de test
plot(x = test$wt, y=test$mpg)

# ploteamos la predicción sobre el test
pred_carstest <- predict(fit_train, newdata=test)
lines(x=test$wt, y=pred_carstest )

# evaluamos con test 
comparing <- data.frame(pred = pred_carstest, real = test$mpg)

# calculamos error
postResample(pred_carstest, test$mpg)


