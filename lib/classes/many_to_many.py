class Game:
    def __init__(self, title):
        if isinstance(title, str) and len(title) > 0:
            self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if (hasattr(self, "title")):
            print('Cannot change title')
        else:
            self._title = value
         
    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        if isinstance(username, str) and len(username) > 0:
            self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    def __init__(self, player, game, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self.player = player
            self.game = game
            self.score = score
        else:
            raise ValueError("Score must be number between 1 and 5000")

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if (hasattr(self, "score")):
            print('Cannot change score')
        else:
            self._score = value