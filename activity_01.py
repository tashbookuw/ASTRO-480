# Noah Tashbook, ASTRO 480, UW Spring 2018, Dr. Sarah Tuttle
#
# ANSWERS, (summarized):
#
#	M31 from Apache
#		1. Autumn, towards the end of September, middle of October
#		2. ~8.7 hours
#		3. The moon *will* interfere with the visibility on this day, for roughly the last ~3 hours
#			3. (cont) 1.915 rad visible which is somewhere between a half-moon and a gibbous (I'm unsure of waxing or waning)
#		4. M31 will be visible for ~7.5 hours, from about 1:30am until 9:00am when the moon gets in the way
#			note: this answer is almost certainly wrong because I didn't take into account the sun but the method is there, I think
#	Spirograph Nebula from Cerro Tololo
#		1. End of Summer, August/September ish
#		2. ~9.5 hours
#		3. The moon interferes for approx. 2 hours, from 6am to 8am
#			3. (cont) Moon will be at the same phase as above 
#				Question: Does moon phase depend on location?
#		4. IC 418 will be visible for ~4.5 hours, from 1:30am until 6am
#			note: This one also just accounts for the moon because the building is about to close and I don't have time to add more sky objects to compare it to


import astroplan

# astroplan.test()
# This did not work but I am moving on anyway

from astroplan import Observer, is_observable 

apache = Observer.at_site('apache point')

from astropy.coordinates import SkyCoord 
from astropy.time import Time
from astroplan import FixedTarget, AtNightConstraint, moon_phase_angle

m31 = FixedTarget.from_name("M31")

# Based on Brian Casey's online tool, 

twi = apache.twilight_evening_astronomical(Time(['2018-03-31']), 'nearest')
mor = apache.twilight_morning_astronomical(Time(['2018-03-31']), 'nearest')
diff = mor-twi

print(Time(diff, format='sec')[0]/3600)
# Comes out to approximately 8.7 hours of view time
# print(Time(twi, format='iso')[0])
# print(Time(mor, format='iso')[0])

twi2 = apache.twilight_evening_astronomical(Time(['2018-12-31']), 'nearest')
mor2 = apache.twilight_morning_astronomical(Time(['2019-01-01']), 'nearest')

print("Visibility begins at: ")
print(Time(twi2, format='iso')[0])
print("Visibility ends at: ")
print(Time(mor2, format='iso')[0])

mrt = apache.moon_rise_time(Time(['2018-12-31']), 'nearest')
mst = apache.moon_set_time(Time(['2018-12-31']), 'nearest')
mrt = Time(mrt, format='iso')[0]
mst = Time(mst, format='iso')[0]
print("Moon rises at: ")
print(mrt)
print("Moon sets at: ")
print(mst)


# astroplan.is_observable([AtNightConstraint.twilight_civil()], apache, m31, time_range=Time([mrt, mst]))
# I didn't end up using this but I spent multiple hours messing with it as a function

moon_ang = moon_phase_angle(Time(['2018-12-31']))
print(moon_ang)
# m = -12.73 + abs(moon_ang) + (.043 * (moon_ang**4))
# magnitude of the moon, from the work of Clabon Allen
#		Doesn't actually work because I didn't convert to radians

#------------------------------------------------------------------------------------------
print("_____________________________________________________")

ctio = Observer.at_site('ctio')

from astropy.coordinates import SkyCoord 
from astropy.time import Time
from astroplan import FixedTarget, AtNightConstraint, moon_phase_angle

ic418 = FixedTarget.from_name("ic418")
print(ic418.name)

twi = ctio.twilight_evening_astronomical(Time(['2018-03-31']), 'nearest')
mor = ctio.twilight_morning_astronomical(Time(['2018-03-31']), 'nearest')
diff = mor-twi

print(Time(diff, format='sec')[0]/3600)
print(Time(twi, format='iso')[0])
print(Time(mor, format='iso')[0])

twi2 = ctio.twilight_evening_astronomical(Time(['2018-12-31']), 'nearest')
mor2 = ctio.twilight_morning_astronomical(Time(['2019-01-01']), 'nearest')

print("Visibility begins at: ")
print(Time(twi2, format='iso')[0])
print("Visibility ends at: ")
print(Time(mor2, format='iso')[0])

mrt = ctio.moon_rise_time(Time(['2018-12-31']), 'nearest')
mst = ctio.moon_set_time(Time(['2018-12-31']), 'nearest')
mrt = Time(mrt, format='iso')[0]
mst = Time(mst, format='iso')[0]
print("Moon rises at: ")
print(mrt)
print("Moon sets at: ")
print(mst)


moon_ang = moon_phase_angle(Time(['2018-12-31']))
print(moon_ang)

# print("end_2")
# this is just so I know if something is loading; there's definitely a cleaner way to do this