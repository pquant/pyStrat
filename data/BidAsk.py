_bidAsk_list = ["BID", "ASK", "MID"]


class BidAsk:
    def __init__(self, ba):
        if ba not in _bidAsk_list:
            ValueError(
                "Unexpected input {0} Bid/Ask. Allowed Bid/Asks are {1}".
                format(ba, _bidAsk_list))
        self.ba = ba
