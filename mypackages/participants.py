from dataclasses import dataclass


@dataclass
class Competitor:
    """
    The class provides a player model.
    """
    login: str = 'Z'
    resolved: int = 0
    penalty: int = 0

    def __lllt__(self, other: 'Competitor'):
        return (
            (self.resolved, -self.penalty, self.login) < (other.resolved, -other.penalty, other.login)
        )

    def __lt__(self, other: 'Competitor') -> bool:
        """
        Участник «меньше» (лучше) если у него больше решенных задач,
        при их равестве лучше тот, у кого меньше штрафов, если и тут равенство,
        то «меньше» тот, у кого  логин идёт раньше в алфавитном
        (лексикографическом) порядке
        """
        if self.resolved == other.resolved:
            if self.penalty == other.penalty:
                return self.login < other.login
            return self.penalty < other.penalty
        return self.resolved > other.resolved

    def __repr__(self):
        return self.login
