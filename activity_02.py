# Margaret Ridder/Noah Tashbook, 4/4/18, ASTRO 480
# Radio Loud Galaxies, Kitt Peak, 2nd half of April, from ROSAT Radio Loud Quasars Catalog

import astroplan
import numpy as np
from astropy.table import QTable
from astropy.coordinates import SkyCoord 
from astropy.time import Time
from astroplan import FixedTarget, Observer, is_observable, observability_table, constraints, AirmassConstraint, AtNightConstraint, is_always_observable, months_observable
import astropy.units as u

t = QTable.read('data/01_data.csv', format='ascii.csv')
# The t stands for table

l = len(t)
# The l stands for lengh

targs = []
# The targs stands for targets

obs = []
# Array of observability tables

kitt = Observer.at_site('Kitt Peak')

for i in range(0, l-1):
	targs.append(FixedTarget(coord=SkyCoord(ra=(t[i]['ra']), dec=(t[i]['dec']), unit=(u.hourangle, u.deg)), name=t[i]['alt_name']))
	# Accounting for the fact that ra is in [hour min sec] and dec is in [deg arcmin arcsec]
	
	# print((targs[len(targs)-1].name)) # This was just to check where errors occurred

time_range = Time(["2018-04-15 00:01", "2018-04-30 23:59"])
# This just takes the whole swath of time, not refining it or anything 

cons = [AirmassConstraint(37), AtNightConstraint.twilight_civil()]
# That airmass is hardly a constraint since it will accept anything up until the horizon but we can easily change it

obs_tab = observability_table(cons, kitt, targs, time_range=time_range)
print(obs_tab)

print("finished")