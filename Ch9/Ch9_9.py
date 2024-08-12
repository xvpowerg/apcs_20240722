import a.b.A
from a.c import A
import a.c.B as B

print(a.b.A.name)
a.b.A.show()
print(A.name)
print(B.name)

A.show()
B.show()
