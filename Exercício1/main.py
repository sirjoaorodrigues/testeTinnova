
class Vote:
    def __init__(self, total_votes=1000, valid_votes=800, white_votes=150, null_votes=50):
        self.total_votes = total_votes
        self.valid_votes = valid_votes
        self.white_votes = white_votes
        self.null_votes = null_votes

    def valid_percent(self):
        return f'Percentual de votos válidos: {int((self.valid_votes / self.total_votes) * 100)}%'

    def white_percent(self):
        return f'Percentual de votos em branco: {int((self.white_votes / self.total_votes) * 100)}%'

    def null_percent(self):
        return f'Percentual de votos nulos: {int((self.null_votes / self.total_votes) * 100)}%'

    def __repr__(self):
        return (f'Votos totais: {self.total_votes} votos\n'
                f'Votos válidos: {self.valid_votes} votos\n'
                f'Votos em branco: {self.white_votes} votos\n'
                f'Votos nulos: {self.null_votes} votos\n')


if __name__ == '__main__':
    votes = Vote()

    print(votes)

    print(votes.valid_percent())
    print(votes.white_percent())
    print(votes.null_percent())
