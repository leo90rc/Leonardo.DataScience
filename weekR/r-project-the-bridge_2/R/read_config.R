#' @title read_config
#' 
#' @param path 
#'
#' @return
#' 
#' @import XML
#' @import logging
#' 

read_config <- function (path){
  
  library(XML)
  
  configPath <- paste0(path, "config/config.xml")
  
  
  tryCatch(expr = {
    
    #Read xml and convert it to a list
    config <- XML::xmlToList(xmlParse(configPath))
    
    
  }, error = function(e){
    
    logerror("Config was not find on the path. Check if it´s called config.xml",
             logger = 'log')
    stop()
  })
  
  loginfo("Config readed.", logger = 'log')
  
  validateConfigNodes(config)
  
  config$data$predictors <- trimws(strsplit(config$data$predictors, ",")[[1]])
  
  
  checkCountry <- is.null(config$data$prediction$country)
  if(checkCountry){
    logerror("You need to choose one country", logger = 'log')
    stop()
  }
  
  checkCountry <- is.na(config$data$prediction$country)
  if(checkCountry){
    logerror("You need to choose one country", logger = 'log')
    stop()
  }
  
  checkYear <- is.null(config$data$prediction$year)
  
  if(checkYear){
    logerror("You need to choose the year", logger = 'log')
    stop()
    
  }else{
    
    config$data$prediction$year <- as.numeric(config$data$prediction$year)
    
  }
  
  checkYearNa <- is.na(config$data$prediction$year)
  
  if(checkYearNa){
    logerror("The year should be a number", logger = 'log')
    stop()
    
  } 
  checkTestSize <- is.null(config$testSize)
  
  if(checkTestSize){
    
    logerror("You need to choose the test rate", logger = 'log')
    stop()
    
  }else{
    
    config$testSize <- as.numeric(config$testSize)
  } 
  
  checkMenorUno <- config$testSize < 1
  checkMayorZero <- config$testSize > 0
  
  if(!(checkMenorUno && checkMayorZero)){
    
    logerror("The test rate should ne a number between 0 and 1 ", logger = 'log')
    stop()    
    
  }
  
  checkTestSizeNa <- is.na(config$testSize)
  
  if(checkTestSizeNa){
    
    logerror("The test rate should be a number", logger = 'log')
    stop()
    
  }
  
  checkOutputFile <- is.null(config$outputFile)
  if(checkOutputFile){
    
    logerror("No output file, create it", logger = 'log')
    
    stop()
  }
  
  separadoresAceptados <- config$sep %in% c(",", ";")
  if(!separadoresAceptados){
    loggeror("Sep just can be , or ;", logger = "log")
    stop()
  }
  
  return(config)
  
} 

# validateConfigNodes function

validateConfigNodes <- function(config){
  
  nodoPrincipal <- identical(names(config), c("sep", "data", "testSize", "outputFile"))
  nodoData <- identical(names(config$data), c("predictors", "target", "prediction"))
  nodoPrediction <- identical(names(config$data$prediction), c("country", "year"))
  
  nodos <- c("nodoPrincipal" = nodoPrincipal, "nodoData" = nodoData, 
             "nodoPrediction" = nodoPrediction)
  
  check <- all(nodos)
  
  if(!check){
    
    nodosMalos <- names(nodos)[!nodos]
    
    logerror(paste0("Los nodos: ", paste(nodosMalos, collapse = ", "),
                    " estan mal estructurados!"), logger = 'log')
    stop()
    
  }
  
}