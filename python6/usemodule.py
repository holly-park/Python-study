import mymodule1

print(mymodule1.sigma(100))
mymodule1.gugudan(7)

import mymodule1 as mm    #as-ailasing: 별명  - 다른이름으로
print(mm.sigma(1000))
mm.gugudan(9)

from mymodule1 import sigma
from mymodule1 import gugudan

print(sigma(1000))
gugudan(4)

from mymodule1 import * #  *는 모든 것을 다 가져오라는 뜻
print(sigma(1000))
gugudan(4)