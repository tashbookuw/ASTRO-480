# Margaret Ridder/Noah Tashbook, 4/4/18, ASTRO 480
# Radio Loud Galaxies, Kitt Peak, 2nd half of April, from ROSAT Radio Loud Quasars Catalog

import astroplan
import numpy as np
from astropy.table import QTable
from astropy.coordinates import SkyCoord 
from astropy.time import Time
from astroplan import FixedTarget, Observer, is_observable, observability_table, constraints, AirmassConstraint, AtNightConstraint, is_always_observable, months_observable, moon_illumination
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

for i in range(0, l):
	targs.append(FixedTarget(coord=SkyCoord(ra=(t[i]['ra']), dec=(t[i]['dec']), unit=(u.hourangle, u.deg)), 
							 name=t[i]['alt_name'] + " [" + t[i]['iau_name'] + ", " + t[i]['ra'] + ", " + t[i]['dec'] + "]"))
	# Accounting for the fact that ra is in [hour min sec] and dec is in [deg arcmin arcsec]
	# the "name" attribute is all of the information just smashed together and I know it's unclean, please don't judge me
	
	# print((targs[len(targs)-1].name)) # This was just to check where errors occurred

time_range = Time(["2018-04-15 00:01", "2018-04-30 23:59"])
# This just takes the whole swath of time, not refining it or anything 

cons = [AirmassConstraint(2), AtNightConstraint.twilight_astronomical()]
# don't use civil twilight because astronomers aren't civil

obs_tab = observability_table(cons, kitt, targs, time_range=time_range)
# print(obs_tab)

obs_targs = []
total_save = []
# total_save is to keep all the data, not just some of it

for i in range(0, len(obs_tab)):
	if obs_tab[i]['ever observable']:
		obs_targs.append([obs_tab[i]['target name'],obs_tab[i]['fraction of time observable']])
		total_save.append(obs_tab[i])

obs_targs.sort(key=lambda obs: obs[1])
total_save.sort(key=lambda obs: obs['fraction of time observable'])
# tell it to sort by the second element in the observable targets array, which is the fraction of time observable
# print(total_save)

those_ten = [["11 53 12.7" , "+80 58 30"],["12 23 29.3", "+75 36 29"],["13 46 8.4", "+73 20 54"],["15 20 47.5", "+72 25 06"],["14 59 7.5", "+71 40 19"],["15 04 13.2", "+68 56 10"],["13 25 29.6", "+65 15 13"],["14 36 45.7", "+63 36 38"],["14 43 58.6", "+63 32 26"],["13 58 17.5", "+57 52 05"]]
newFixedTargs = []

def most_obs(n):
	output = "The " + str(n) + " most (or equally) observable Radio Loud Galaxies in the 2nd half of April: \n"
	for i in range(0, n):
		output += str(i+1) + ". " + obs_targs[len(obs_targs)-(1+i)][0] + " is observable for " + str(obs_targs[len(obs_targs)-(1+i)][1]) + " of the second half of April. \n"
		#those_ten.append(total_save[len(obs_targs)-(1+i)])
		newFixedTargs.append(FixedTarget(coord=SkyCoord(ra=those_ten[i][0], dec=those_ten[i][1], unit=(u.hourangle, u.deg))))
	newOutput = observability_table(cons, kitt, newFixedTargs, time_range=Time(["2018-05-15 00:01", "2018-05-31 23:59"]))
	return [output, newOutput]

print(most_obs(10)[0])
print("\n ------------------ \n")
print(most_obs(10)[1])

 # We can change it to whatever, obviously

moon_ang1 = moon_illumination(Time(['2018-04-15']))
moon_ang2 =  moon_illumination(Time(['2018-04-30']))
# I changed the function here so now the variables are poorly named but I'm leaving it to build character


mrt1 = Time(kitt.moon_rise_time(Time(['2018-04-15']), 'nearest'), format='iso')[0]
mst1 = Time(kitt.moon_set_time(Time(['2018-04-15']), 'nearest'), format='iso')[0]
mrt2 = Time(kitt.moon_rise_time(Time(['2018-04-30']), 'nearest'), format='iso')[0]
mst2 = Time(kitt.moon_set_time(Time(['2018-04-30']), 'nearest'), format='iso')[0]

#print("moon illumination begins at: " + str(moon_ang1) + " and ends with: " + str(moon_ang2))
#print("In the middle of the month, the moon rises at " + str(mrt1) + " and sets at " + str(mst1) + ". At the end of the month, the moon rises at " + str(mrt2) + " and sets at " + str(mst2) + ".")