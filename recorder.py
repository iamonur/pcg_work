class DBWrapper:
    def __init__(self, ip="127.0.0.1", port="3306", user="root", passwd="toor", default_schema="gg"):
        print("Actual db connection?")

    def __register_game(self, level, game, winnable, moves):
        query = "SELECT COUNT(*) FROM game WHERE level={} AND desc={}".format(level, game)
        #execute query
        #get result
        res = 1 #TODO: Remove
        if res is 1:
            query = "SELECT id FROM game WHERE level={} AND desc={}".format(level, game)
            #execute query
            #get result
            return res
        elif res is 0:
            query = "INSERT INTO game (level, desc, iswinnable, spin, spin_length) VALUES ({},{},{},{},{})".format(level, game, winnable, moves, len(moves))
            #execute query
            query = "SELECT id FROM game WHERE level={} AND desc={}".format(level, game)
            #execute query
            #get result
            return res
        else:
            raise "Important DB Accident that needs attention. Let execution stop and this exception propagate."

    def submit_gameplay(self, level, game, moves, winnable=True,  outcome=True):
        id = self.__register_game(level, game, winnable, moves)
        query = "INSERT INTO gameplay (id, result) VALUES ({},{})".format(id, outcome)
        #execute query.


class StubDBWrapper(DBWrapper): #Same class, but not query, just STDOUT.
    def __init__(self):
        print("A stub database connection!s")

    def __register_game(self, level, game, winnable, moves):
        print("-----------A new game-----------")
        print("The level: {}\n The ruleset: {}\n Expected outcome: {}\n Expected moves to win: {}".format(level, game, winnable, moves))

    def submit_gameplay(self, level, game,  moves, winnable=True, outcome=True):
        id = self.__register_game(level, game, winnable, moves)
        query = "INSERT INTO gameplay (id, result) VALUES ({},{})".format(id, outcome)
        print(query)
