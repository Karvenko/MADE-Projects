set hive.auto.convert.join=False;
set mapreduce.job.reduces=2;

select users.browser,
  sum(if(users.sex = 'male', 1, 0)) as male_count,
  sum(if(users.sex = 'female', 1, 0)) as female_count
from logs join users on (
  users.ip = logs.ip
)
group by users.browser limit 10;
