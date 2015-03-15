from collections import OrderedDict


class Rank:
    def __init__(self, symbol, rank):
        self.symbol = symbol
        self.rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __str__(self):
        return self.rank


class Suit:
    def __init__(self, color, suit):
        self.color = color
        self.suit = suit

    def __eq__(self, other):
        return self.suit == other.suit

    def __str__(self):
        return self.suit


class Ace(Rank):
    def __init__(self):
        Rank.__init__(self, 'A', 'Ace')


class Two(Rank):
    def __init__(self):
        Rank.__init__(self, '2', 'Two')


class Three(Rank):
    def __init__(self):
        Rank.__init__(self, '3', 'Three')


class Four(Rank):
    def __init__(self):
        Rank.__init__(self, '4', 'Four')


class Five(Rank):
    def __init__(self):
        Rank.__init__(self, '5', 'Five')


class Six(Rank):
    def __init__(self):
        Rank.__init__(self, '6', 'Six')


class Seven(Rank):
    def __init__(self):
        Rank.__init__(self, '7', 'Seven')


class Eight(Rank):
    def __init__(self):
        Rank.__init__(self, '8', 'Eight')


class Nine(Rank):
    def __init__(self):
        Rank.__init__(self, '9', 'Nine')


class Ten(Rank):
    def __init__(self):
        Rank.__init__(self, '10', 'Ten')


class Jack(Rank):
    def __init__(self):
        Rank.__init__(self, 'J', 'Jack')


class Queen(Rank):
    def __init__(self):
        Rank.__init__(self, 'Q', 'Queen')


class King(Rank):
    def __init__(self):
        Rank.__init__(self, 'K', 'King')


class Hearts(Suit):
    def __init__(self):
        Suit.__init__(self, 'red', 'Hearts')


class Clubs(Suit):
    def __init__(self):
        Suit.__init__(self, 'black', 'Clubs')


class Spades(Suit):
    def __init__(self):
        Suit.__init__(self, 'black', 'Spades')


class Diamonds(Suit):
    def __init__(self):
        Suit.__init__(self, 'red', 'Diamonds')


RANKS = OrderedDict([('King', King), ('Queen', Queen), ('Jack', Jack),
                     ('Ten', Ten), ('Nine', Nine), ('Eight', Eight),
                     ('Seven', Seven), ('Six', Six), ('Five', Five),
                     ('Four', Four), ('Three', Three), ('Two', Two),
                     ('Ace', Ace)])


SUITS = OrderedDict([('Diamonds', Diamonds), ('Clubs', Clubs),
                     ('Hearts', Hearts), ('Spades', Spades)])


class Card:
    def __init__(self, rank, suit):
        object.__setattr__(self, 'rank', rank())
        object.__setattr__(self, 'suit', suit())

    def __setattr__(self, *args):
        raise AttributeError('can\'t set attribute')

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return '{0} of {1}'.format(self.rank, self.suit)

    def __repr__(self):
        return '<Card {0} of {1}>'.format(self.rank, self.suit)


class CardCollection:
    def __init__(self, collection=[]):
        self.collection = list(collection)

    def draw(self, index):
        return self.collection.pop(index)

    def draw_from_top(self):
        return self.draw(len(self.collection) - 1)

    def draw_from_bottom(self):
        return self.draw(0)

    def top_card(self):
        return self.collection[len(self.collection) - 1]

    def bottom_card(self):
        return self.collection[0]

    def add(self, card):
        self.collection.append(card)

    def index(self, card):
        if card in self.collection:
            return self.collection.index(card)
        else:
            raise ValueError('{0} is not in collection'.format(card))

    def __getitem__(self, index):
        if index >= 0 and index < len(self.collection):
            return self.collection[index]
        else:
            raise IndexError('index out of range')

    def __len__(self):
        return len(self.collection)


def StandardDeck():
    return list(CardCollection([Card(rank, suit)
                                for suit in SUITS.values()
                                for rank in RANKS.values()]))


def BeloteDeck():
    return list(CardCollection([Card(rank, suit)
                                for suit in SUITS.values()
                                for rank in RANKS.values()
                                if rank().symbol not in
                                {'2', '3', '4', '5', '6'}]))


def SixtySixDeck():
    return list(CardCollection([Card(rank, suit)
                                for suit in SUITS.values()
                                for rank in RANKS.values()
                                if rank().symbol not in
                                {'2', '3', '4', '5', '6', '7', '8'}]))