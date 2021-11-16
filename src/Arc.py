class Arc():

    def __init__(self, u=None, v=None, t=None, l=None):
        self.u = u
        self.v = v
        self.t = t
        self.l = l

    def __repr__(self):
        return str((self.u, self.v, self.t, self.l))
