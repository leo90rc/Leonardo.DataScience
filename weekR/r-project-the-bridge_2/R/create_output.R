#' @title create_output
#' @description This function is called by the skeleton function and create the 
#' output doc in to Outpute File 
#' 
#' @param output DataFrame 
#' @param path The environment of project
#' 
#' @import logging
#'
#' @return
#' 
createOutput <-  function(output, path){
  
  nameOutput <- paste0(path, "output/Spain_not_fascist_2000.csv")
  
  tryCatch(expr = {
    
    write.csv(output, file = nameOutput, 
              row.names = FALSE)
    
  }, error = function(e){
    
    logerror("Saving failed!", logger = 'log')
    stop()
  })
  
}