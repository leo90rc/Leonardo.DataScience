#' @title entrenar_modelo
#' 
#' @description esta función es llamada en GapminderApp y se encarga de partir datos y entrenar un modelo
#' 
#' @param df_1
#' @param config
#' 
#' @import caret
#' @author leosanchezsoler
#' 
#' @return output
#' 

entrenar_modelo <- function(df_1, config){
  
  library(caret)

  df_orig <- data.frame(df_1[1])
  y_pred <- data.frame(df_1[2])
  # Separacion del train y test
  validation_index <- createDataPartition(df_orig[, ncol(df_orig)], p=0.80, list=FALSE)
  test_df <- df_orig[-validation_index,]
  train_df <- df_orig[validation_index,]
  
  
  # Simple linear regression model (lm means linear model)
  model <- train( train_df[,3:(ncol(train_df)-1)], train_df[, ncol(train_df)], method = 'lm')
  
  loginfo("Descripción del modelo:", logger = 'log')
  
  predict_test <- predict(model, test_df[,3:(ncol(test_df)-1)])
  
  loginfo("Métricas del modelo:", logger = 'log')
  
  RMSE <- sqrt(mean((predict_test - test_df[, ncol(train_df)])^2))
  
  resultado <- predict(model, y_pred) 
  y_pred[, ncol(y_pred)] <- resultado
  output <- y_pred
  return(output)
}