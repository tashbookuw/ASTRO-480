# Margaret Ridder/Noah Tashbook, 4/4/18, ASTRO 480
# Radio Loud Galaxies, Kitt Peak, 2nd half of April, from ROSAT Radio Loud Quasars Catalog

import astroplan
import numpy as np
from astropy.table import QTable

t = QTable.read('data/01_data.csv', format='ascii.csv')
# The t stands for table

l = len(t)
# The l stands for lengh

targs = []
# The targs stands for targets

from astropy.coordinates import SkyCoord 
from astropy.time import Time
from astroplan import FixedTarget, Observer, is_observable
import astropy.units as u

kitt = Observer.at_site('Kitt Peak')

for i in range(0, l-1):
	targs.append(FixedTarget(coord=SkyCoord(ra=(t[i]['ra']), dec=(t[i]['dec']), unit=(u.hourangle, u.deg)), name=t[i]['alt_name']))
	# Accounting for the fact that ra is in [hour min sec] and dec is in [deg arcmin arcsec]
	
	# print((targs[len(targs)-1].name)) # This was just to check where errors occurred

# Slide 15 from Wednesday has some different ways to check observability. Airmass, twilight_morn-eve, observing table, &c.

print("finished")