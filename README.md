install mysql connector
pip3 install mysql-connector-python
pip3 install xlrd
pip3 install openpyxl
pip3 install python-dateutil

clear db
delete from hotel_map_compsets;
delete from hotel_user_maps;
delete from stat_details;
delete from stats;
delete from user_report_links;
delete from hotels;

delete s, sd
from stats s
join stat_details sd on sd.`stats_id` = s.`id`
where s.`hotel_id` =1

delete s, sd
from stats s
join stat_details sd on sd.stats_id = s.id
where s.created_at like '2021-09-28%'

SELECT *
FROM hotels AS a
WHERE EXISTS (
  SELECT *
  FROM ota_locations AS b 
  WHERE a.city=b.name
)
and ota_hotel_id is null 
and addr = 'pilot_hotel'


delete s, sd
from stats s
join stat_details sd on sd.`stats_id` = s.`id`
join hotels h on h.id = s.hotel_id
where h.name like 'Data %'


delete hum
from hotel_user_maps hum
join hotels h on h.id = hum.hotel_id
where h.name like 'Data %'

delete hotels where hotels.name like 'Data %'