# main

# directory set up
path1 <- getwd()
path <- paste0(path1, "/")

setwd(path)

lapply(paste0("R/", list.files(path = "R/", recursive = TRUE)), source)


# Debugging and unbugging
debug(GapminderApp)
GapminderApp(path)
undebug(GapminderApp)