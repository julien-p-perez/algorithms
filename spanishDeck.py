import collections, random


Card = collections.namedtuple('Card', ['rank', 'suit'])
 
class SpanishDeck: 
    ranks = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    suits = 'oros copas espadas bastos'.split()


    def __init__(self): 
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self): 
        return len(self._cards)
    
    def __getitem__(self, position): 
        return self._cards[position]

    def shuffle(self): 
        random.shuffle(self._cards)

    def deal(self, n): 
        """
        hand = []

        while(n != 0):
            card = random.choice(self._cards)
            hand.append(card)
            n -= 1

        return hand
        """
        return random.sample(self._cards, n)
        


deck = SpanishDeck()
hand = deck.deal(5)

print(hand)


