from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
config = Config(max_depth=100)
graphviz = GraphvizOutput(output_file=r'trace_detail.png')
with PyCallGraph(output=graphviz,config=config):
    class A(object):
        def go(self):
            print("go A go!")
    class B(A):
        def go(self):
            super().go()
            print("go B go!")
    class C(A):
        def go(self):
            super().go()
            print("go C go!")
    class D(A):
        def go(self):
            super().go()
            print("go D go!")
    class E(B,C,D):
        def go(self):
            super().go()
            print("go E go!")
    e=E()
    e.go()