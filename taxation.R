# read taxation data
library(tidyverse)
library(GGally)

dat <- readr::read_csv('data/data.csv') %>% 
  mutate(auslaenderquote = auslaender/population)

ggpairs(data = dat, 
        columns = ends_with('quote', vars = names(dat)),
        upper = list(continuous = 'density'),
        diag = list(continuous = 'densityDiag'),
        lower = list(continuous = 'smooth_loess')
        )

ggplot(dat, aes(x=praemienverbilligungsquote, y=sozialhilfequote, color=wohnviertel)) + 
  geom_point()
