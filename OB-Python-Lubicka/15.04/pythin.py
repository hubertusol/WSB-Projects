import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def getInstance():
        if Singleton._instance is None:
            with Singleton._lock:
                if Singleton._instance is None:
                    Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        
        pass

    def query(self, sql):
        pass

s = Singleton.getInstance()
print(s)
z = Singleton.getInstance()
print(z)