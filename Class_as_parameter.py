class A(object):
    def go(self):
        print("go A go!")
    def send(self):
        print("send A send!")
class B(object):
    def go(self):
        print("go B go!")
    def send(self):
        print("send B send!")
def Test(C):
    print("ok")
    a=C()
    print(a.send())
Test(B)

