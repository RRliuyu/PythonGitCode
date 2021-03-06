
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from pycallgraph import Config
config = Config(max_depth=100)
graphviz = GraphvizOutput(output_file=r'trace_detail.png')
with PyCallGraph(output=graphviz,config=config):
    class Event(object):
        def __init__(self):
            self.name = "tom"
        def getName(self):
            return self.name
    class JavaListen(object):
        def handleEvent(self, event):
            print ("%s is learning java " %(event.getName()))
    class PythonListen(object):
        def handleEvent(self, event):
            print ("%s is learning python " % (event.getName()))
    class EventDispatcher(object):
        def __init__(self):
            self.__observers = list()
        def registerEvent(self, eventlisten):
            self.__observers.append(eventlisten)
        def notifyAll(self, event):
            for eventListen in self.__observers:
                eventListen.handleEvent(event)
    # 事件分发器
    dispatch = EventDispatcher()
    # 事件监听器
    javaListen = JavaListen()
    pythonListen = PythonListen()
    # 向事件分发器中注册事件监听器
    dispatch.registerEvent(javaListen)
    dispatch.registerEvent(pythonListen)
    # 事件源
    event1 = Event()
    # 分发事件
    dispatch.notifyAll(event1)