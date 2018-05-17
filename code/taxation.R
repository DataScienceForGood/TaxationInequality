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
  rename(wohnviertelid = X__1
         , Reineinkommensklasse = "Reineinkommensklasse in Fr."
         , Veranlagungen = "Anzahl Veranlagungen"
         , Reineinkommen = "Summe Reineinkommen"
         , "Einkommenssteuerbetrag" = "Summe Einkommenssteuerbetrag"
         )

vermoegen <-  readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 122) %>% 
  slice(1:105) %>% 
  select(1:6) %>% 
  fill(X__1, X__2) %>% 
  rename(wohnviertelid = X__1
         , Wohnviertel = X__2
         , "Reinvermoegensklasse" = "Reinvermögensklasse in Fr."
         , "Veranlagungen" = "Anzahl Veranlagungen"
         , "Reinvermoegen" = "Summe Reinvermögen"
         , "Vermoegenssteuerbetrag" = "Summe Vermögenssteuerbetrag"
         )

einkommen2 <- readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 8) %>% 
  slice(1:105) %>% 
  select(8:13) %>% 
  fill(X__3, X__4) %>% 
  rename(wohnviertelid = X__3
         , Wohnviertel = X__4, einkommenquintile = X__5
         , "Veranlagungenq" = "Anzahl Veranlagungen__1"
         , "Reineinkommenq" = "Summe Reineinkommen__1"
         , "Einkommenssteuerbetragq" = "Summe Einkommenssteuerbetrag__1"
         )

vermoegen2 <- readxl::read_excel('data/Steuern_Klassen_Wohnviertel_plus_Quintile.xlsx', skip = 122) %>% 
  slice(1:105) %>% 
  select(8:13) %>% 
  fill(X__4, X__5) %>% 
  rename(wohnviertelid = X__4
         , Wohnviertel = X__5
         , vermoegensquintile = X__6
         , "Veranlagungenq" = "Anzahl Veranlagungen__1"
         , "Reinvermoegenq" = "Summe Reinvermögen__1"
         , "Vermögenssteuerbetragq" = "Summe Vermögenssteuerbetrag__1"
         )

write_csv(einkommen,  'data/einkommen2015.csv')
write_csv(einkommen2, 'data/einkommen2015q.csv')
write_csv(vermoegen,  'data/vermoegen2015.csv')
write_csv(vermoegen2, 'data/vermoegen2015q.csv')
