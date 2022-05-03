import re

s = 'href="/a/like.php?ul&amp;perm&amp;ifab&amp;ft_ent_identifier=2150994828412545&amp;eav=Afbst2OIk4LszuA3cl4eI9rnH5zX-YQIhDgAgemKFfCTsSFzbmeTpZ2qRWfW6vWvhr0&amp;av=100004779240033&amp;gfid=AQDhQ-3arp4M9vPK66o&amp;ref_component=mbasic_photo_permalink_actionbar&amp;ref_page=%2Fwap%2Fstory.php&amp;refid=52" class="ck cl cm cn" role="button" aria-pressed="false">'

a = re.findall('/a/like.php?.*?"',s)
print(a)