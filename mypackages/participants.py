from dataclasses import dataclass


@dataclass
class Competitor:
    """
    The class provides a player model.
    """
    login: str = 'Z'
    resolved: int = 0
    penalty: int = 0

    def __lt__(self, other: 'Competitor') -> bool:
        """
        The winner is smaller (<) than the loser.
        """
        return (
            (-self.resolved, self.penalty, self.login)
            < (-other.resolved, other.penalty, other.login)
        )

    def __repr__(self):
        return self.login
