select substr(`date`, 1, 8), count(*) as c 
from logs group by substr(`date`, 1, 8) order by c desc limit 10;
