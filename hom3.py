ORDERED_RANKS = ['King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight', 'Seven',
                  'Six', 'Five', 'Four', 'Three', 'Two', 'Ace']


ORDERED_SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']


class Rank():
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __str__(self):
        return self.rank


class Suit():
    def __init__(self, color):
        self.color = color

    def __eq__(self, other):
        return self.color == other.color

    def __str__(self):
        return self.suit


class Ace(Rank):
    def __init__(self):
        Rank.__init__(self, 'A')

    def __str__(self):
        return "Ace"


class Two(Rank):
    def __init__(self):
        Rank.__init__(self, '2')

    def __str__(self):
        return "Two"


class Three(Rank):
    def __init__(self):
        Rank.__init__(self, '3')

    def __str__(self):
        return "Three"


class Four(Rank):
    def __init__(self):
        Rank.__init__(self, '4')

    def __str__(self):
        return "Four"


class Five(Rank):
    def __init__(self):
        Rank.__init__(self, '5')

    def __str__(self):
        return "Five"


class Six(Rank):
    def __init__(self):
        Rank.__init__(self, '6')

    def __str__(self):
        return "Six"


class Seven(Rank):
    def __init__(self):
        Rank.__init__(self, '7')

    def __str__(self):
        return "Seven"


class Eight(Rank):
    def __init__(self):
        Rank.__init__(self, '8')

    def __str__(self):
        return "Eight"


class Nine(Rank):
    def __init__(self):
        Rank.__init__(self, '9')

    def __str__(self):
        return "Nine"


class Ten(Rank):
    def __init__(self):
        Rank.__init__(self, '10')

    def __str__(self):
        return "Ten"


class Jack(Rank):
    def __init__(self):
        Rank.__init__(self, 'J')

    def __str__(self):
        return "Jack"


class Queen(Rank):
    def __init__(self):
        Rank.__init__(self, 'Q')

    def __str__(self):
        return "Queen"


class King(Rank):
    def __init__(self):
        Rank.__init__(self, 'K')

    def __str__(self):
        return "King"


class Clubs(Suit):
    def __init__(self):
        Suit.__init__(self, 'black')

    def __str__(self):
        return "Clubs"


class Diamonds(Suit):
    def __init__(self):
        Suit.__init__(self, 'red')

    def __str__(self):
        return "Diamonds"


class Hearts(Suit):
    def __init__(self):
        Suit.__init__(self, 'red')

    def __str__(self):
        return "Hearts"


class Spades(Suit):
    def __init__(self):
        Suit.__init__(self, 'black')

    def __str__(self):
        return "Spades"


RANKS = {
    'King': King().__class__,
    'Queen': Queen().__class__,
    'Jack': Jack().__class__,
    'Ten': Ten().__class__,
    'Nine': Nine().__class__,
    'Eight': Eight().__class__,
    'Seven': Seven().__class__,
    'Six': Six().__class__,
    'Five': Five().__class__,
    'Four': Four().__class__,
    'Three': Three().__class__,
    'Two': Two().__class__,
    'Ace': Ace().__class__
}


SUITS = {
    'Hearts': Hearts().__class__,
    'Clubs': Clubs().__class__,
    'Spades': Spades().__class__,
    'Diamonds': Diamonds().__class__
}


class Card():
    def __init__(self, rank, suit):
        self.rank = rank()
        self.suit = suit()

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class CardCollection(Card):
    def __init__(self, collection=[]):
        self.collection = collection

    def __getitem__(self, i):
        return self.collection[i]

    def __len__(self):
        return len(self.collection)

    def draw(self, index):
        return self.collection[index]
        del self.collection[index]

    def draw_from_top(self):
        return self.collection[-1]
        del self.collection[-1]

    def draw_from_buttom(self):
        return self.collection[0]
        del self.collection[0]

    def top_card(self):
        return self.collection[-1]

    def buttom_card(self):
        return self.collection[0]

    def add(self, card):
        return self.collection.append(card)

    def index(self, card):
        counter = 0
        for item in collection:
            if item != card:
                counter += 1
        return counter


def StandartDeck():
    result = []
    for suit in ORDERED_SUITS:
        for rank in ORDERED_RANKS:
            result.append('Card ' + str(Card(RANKS[rank], SUITS[suit])))
    return result


def BeloteDeck():
    result = []
    for suit in ORDERED_SUITS:
        for rank in ORDERED_RANKS:
            if rank != "Two" and rank != "Three" and rank != "Four" \
            and rank != "Five" and rank != "Six":
                result.append('Card ' + str(Card(RANKS[rank], SUITS[suit])))
    return result


def SixtySixDeck():
    result = []
    for suit in ORDERED_SUITS:
        for rank in ORDERED_RANKS:
            if rank != "Two" and rank != "Three" and rank != "Four" \
            and rank != "Five" and rank != "Six" and rank != "Seven" \
            and rank != "Eight":
                result.append('Card ' + str(Card(RANKS[rank], SUITS[suit])))
    return result


# def main():
#     #print(RANKS)
#     #print(RANKS["Ace"]() == RANKS["Ace"]())
#     #print(str(RANKS["Ace"]()))
#     #print(str(SUITS["Spades"]()))
#     #print(RANKS["Ace"])
#     #print(Card(RANKS["Ace"], SUITS["Hearts"]).rank)
#     #print(Card(RANKS["Ace"], SUITS["Hearts"]))
#     #print(Card(RANKS["Ace"], SUITS["Spades"]).rank)
#     #print(StandartDeck())
#     #print(BeloteDeck())
#     #print(SixtySixDeck())
#     #print(RANKS.keys())
#     #print(SUITS.keys())
#     #print(CardCollection.add(Card(RANKS["Ace"], SUITS["Hearts"])))
# if __name__ == '__main__':
#     main()

#for rank in ORDERED_RANKS[:7]:... (add Ace)