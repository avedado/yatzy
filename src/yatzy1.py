
class Yatzy:

    @staticmethod
    def chance(dado1, dado2, dado3, dado4, dado5):
        puntos = 0
        puntos += dado1
        puntos += dado2
        puntos += dado3
        puntos += dado4
        puntos += dado5
        return puntos
    '''que refactorizamos y pq'''


    @staticmethod
    def yatzy(dice):
        counts = [0] * (len(dice) + 1)
        for die in dice:
            counts[die - 1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    @staticmethod
    def ones(dado1, dado2, dado3, dado4, dado5):
        sum = 0
        if (dado1 == 1):
            sum += 1
        if (dado2 == 1):
            sum += 1
        if (dado3 == 1):
            sum += 1
        if (dado4 == 1):
            sum += 1
        if (dado5 == 1):
            sum += 1

        return sum

    @staticmethod
    def twos(dado1, dado2, dado3, dado4, dado5):
        sum = 0
        if (dado1 == 2):
            sum += 2
        if (dado2 == 2):
            sum += 2
        if (dado3 == 2):
            sum += 2
        if (dado4 == 2):
            sum += 2
        if (dado5 == 2):
            sum += 2
        return sum

    @staticmethod
    def threes(dado1, dado2, dado3, dado4, dado5):
        s = 0
        if (dado1 == 3):
            s += 3
        if (dado2 == 3):
            s += 3
        if (dado3 == 3):
            s += 3
        if (dado4 == 3):
            s += 3
        if (dado5 == 3):
            s += 3
        return s

    def __init__(self, dado1=0, dado2=0, dado3=0, dado4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = dado1
        self.dice[1] = dado2
        self.dice[2] = dado3
        self.dice[3] = dado4
        self.dice[4] = _5

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    def score_pair(self, dado1, dado2, dado3, dado4, dado5):
        counts = [0] * 6
        counts[dado1 - 1] += 1
        counts[dado2 - 1] += 1
        counts[dado3 - 1] += 1
        counts[dado4 - 1] += 1
        counts[dado5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_pair(dado1, dado2, dado3, dado4, dado5):
        counts = [0] * 6
        counts[dado1 - 1] += 1
        counts[dado2 - 1] += 1
        counts[dado3 - 1] += 1
        counts[dado4 - 1] += 1
        counts[dado5 - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, dado3, dado4, dado5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[dado3 - 1] += 1
        tallies[dado4 - 1] += 1
        tallies[dado5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(dado1, dado2, dado3, dado4, dado5):
        t = [0] * 6
        t[dado1 - 1] += 1
        t[dado2 - 1] += 1
        t[dado3 - 1] += 1
        t[dado4 - 1] += 1
        t[dado5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(dado1, dado2, dado3, dado4, dado5):
        tallies = [0] * 6
        tallies[dado1 - 1] += 1
        tallies[dado2 - 1] += 1
        tallies[dado3 - 1] += 1
        tallies[dado4 - 1] += 1
        tallies[dado5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(dado1, dado2, dado3, dado4, dado5):
        tallies = [0] * 6
        tallies[dado1 - 1] += 1
        tallies[dado2 - 1] += 1
        tallies[dado3 - 1] += 1
        tallies[dado4 - 1] += 1
        tallies[dado5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(dado1, dado2, dado3, dado4, dado5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[dado1 - 1] += 1
        tallies[dado2 - 1] += 1
        tallies[dado3 - 1] += 1
        tallies[dado4 - 1] += 1
        tallies[dado5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
