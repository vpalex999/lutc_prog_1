from redirect import redirect
from teststreams import interact

(result, output) = redirect(interact, (), {}, '4\n5\n6\n')

print(result)

print(output)

pass