class Signal:
    def __init__(self):
        self.listeners = []

    def send(self):
        for listener in self.listeners:
            listener()

    def dispatch(self, listener, uuid):

        self.listeners.append(listener)
