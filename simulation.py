import player
import parser
import spinner
import recorder

class SimClass:
    def __init__(self):
        self.__record_init()

    def __spin_job(self):
        self.spin = spinner.SpinClass()
        self.spin.generate_compile_spin()
        return self.spin.mazify()

    def __parse_job(self):
        self.parse = parser.ParserClass()
        return self.parse.main_functionality()

    def __play_init(self):
        self.game = player.skeleton_game.format(immovable="", mover="", chaser=player.chaser_str)
        self.player = player.GameClass(actions_list=self.moves, game_desc=self.game, level_desc=self.maze)

    def __play_perform(self):
        return self.player.play()

    def __record_init(self):
        self.db = recorder.StubDBWrapper()

    def __record_job(self, winnable=True, outcome=True):
        self.db.submit_gameplay(self.maze, self.game, winnable, self.moves, outcome)

    def simulate(self): #is a chain reaction of model checking, parsing, playing and recording.
        self.maze = self.__spin_job()

        try:
            self.moves = self.__parse_job()
        except ValueError: #If we cannot win, report but continue.
            self.__record_job(winnable=False, outcome=False)
            return
            #self.simulate()

        self.__play_init()
        if self.__play_perform() > 0:
            self.__record_job(outcome=True)
        else:
            self.__record_job(outcome=False)

if __name__ == "__main__":
    s = SimClass()
    s.simulate()
