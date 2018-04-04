# Noah Tashbook, 4/4/18, ASTRO 480, w/ Margaret Ridder
# Radio Loud Galaxies, Kitt Peak, 2nd half of April, from ROSAT Radio Loud Quasars Catalog

import astroplan
import numpy as np
from astropy.table import QTable

table = QTable.read('data.csv', format='ascii.csv')

