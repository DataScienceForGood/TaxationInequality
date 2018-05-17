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


einkommen <- readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 8) %>% 
  slice(1:105) %>% 
  select(1:6) %>% 
  fill(X__1, Wohnviertel) %>% 
  rename(wohnviertelid = X__1)

vermoegen <-  readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 122) %>% 
  slice(1:105) %>% 
  select(1:6) %>% 
  fill(X__1, X__2) %>% 
  rename(wohnviertelid = X__1, Wohnviertel = X__2)

einkommen2 <- readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 8) %>% 
  slice(1:105) %>% 
  select(8:13) %>% 
  fill(X__3, X__4) %>% 
  rename(wohnviertelid = X__3, Wohnviertel = X__4, einkommenquintile = X__5)

vermoegen2 <- readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 122) %>% 
  slice(1:105) %>% 
  select(8:13) %>% 
  fill(X__4, X__5) %>% 
  rename(wohnviertelid = X__4, Wohnviertel = X__5, vermoegensquintile = X__6)
