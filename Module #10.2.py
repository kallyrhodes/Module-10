
from plotnine.data import huron
from plotnine import ggplot, aes, geom_line

(
    ggplot(huron) 
    + aes(x="year", y="level") 
    + geom_line()
)
