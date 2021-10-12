#' @title  leer_datos
#' 
#' @description función que lee archivos csv. Es llamada por la función main
#' 
#' @param config
#' @param path
#' 
#' @return datos
#' @author leosanchezsoler

leer_datos <- function(config, path){
  
  lista_df <- list()
  
  for (i in config$data$predictors){
    
    tryCatch(expr = {
      pathDatos <- paste0(path, 'data/', i)
      datos <- data.table::fread(pathDatos, sep = config$sep,
                                 encoding = 'UTF-8', data.table = FALSE, header = T)
      
      
    }, error = function(e){
      
      logerror("Data was not found on the path. Check the direction and the config",
               logger = 'log')
      stop()
    })
    
    if(nrow(datos) == 0 | ncol(datos) == 0){
      
      logerror("Data was read poorly, check data format.",
               logger = 'log')
      stop()
      
    }
    
    lista_df[[i]] <- datos
    
  }
  loginfo("Leyendo target", logger = 'log')
  
  target <- leer_target(config, path)
  
  lista_pred_target <- list(predictoras = lista_df, target = target)
  
  return(lista_pred_target)
}


#' @title leer_target
#' 
#' @description es llamada por main y se encarga de leer el target
#' 
#' @param config
#' @param path
#' 
#' @return target
#' @import data.table
#' @import logging
#' 
#' @author leosanchezsoler

leer_target <- function(config, path){
  path_target <- paste0(path, 'data/', config$data$target)
  
  tryCatch(expr = {
    target <- data.table::fread(path_target, sep = config$sep,
                                encoding = 'UTF-8', data.table = F, header = T)
    
  }, error = function(e){
    
    logerror('No se ha encontrado el target en la ruta. Por favor, compruébalo y revisa config.xml',
             logger = 'log')
    stop()
    
    })
  return(target)
}