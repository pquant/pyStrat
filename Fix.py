

class FixTy:

    @classmethod
    def open(cls):
        c = cls.__new__(cls)
        c.fixFlag = "OPEN"
        c.fixTimes = None
        return c

    @classmethod
    def close(cls):
        c = cls.__new__(cls)
        c.fixFlag = "CLOSE"
        c.fixTimes = None
        return c

    @classmethod
    def high(cls):
        c = cls.__new__(cls)
        c.fixFlag = "HIGH"
        c.fixTimes = None
        return c

    @classmethod
    def low(cls):
        c = cls.__new__(cls)
        c.fixFlag = "LOW"
        c.fixTimes = None
        return c

    @classmethod
    def fixes(cls, times):
        c = cls.__new__(cls)
        c.fixFlag = "HIGH"
        c.fixTimes = times
        return c
