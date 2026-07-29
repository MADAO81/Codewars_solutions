# https://www.codewars.com/kata/52d3b68215be7c2d5300022f/train/python


# class Event():
    
#     def __init__(self):
#         self._handlers = []
    
#     def subscribe(self, handler):
#         self._handlers.append(handler)
    
#     def unsubscribe(self, handler):
#         if handler in self._handlers:
#             self._handlers.remove(handler)
        
#     def emit(self, *args):
#         for h in self._handlers:
#             h(*args)



def Event():
    handlers = []
    
    class EventObject:
        def subscribe(self, handler):
            if handler not in handlers:
                handlers.append(handler)
        
        def unsubscribe(self, handler):
            if handler in handlers:
                handlers.remove(handler)
        
        def emit(self, *args):
            for handler in handlers:
                handler(*args)
    
    return EventObject()
