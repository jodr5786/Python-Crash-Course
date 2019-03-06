import sandwhiches_func
sandwhiches_func.make_sandwich('swiss','turkey','mayo')

from sandwhiches_func import make_sandwich
make_sandwich('ham','cheddar')

from sandwhiches_func import make_sandwich as ms 
ms('roast beef','sharp cheddar')

import sandwhiches_func as s 
s.make_sandwich('turkey','provolone')

from sandwhiches_func import *
make_sandwich('test','test')