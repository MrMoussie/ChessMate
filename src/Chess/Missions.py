import random, sys

sys.path.append("../SQL")
import Queries


def current_mission_set():
    get_easy_mission()
    get_medium_mission()
    get_hard_mission()
    get_expert_mission()


def get_easy_mission():
    id = random(10) + 1
    query = ("SELECT description FROM easy_missions WHERE id = %d", id)
    description = Queries.getSQuery(query, None)
    print(description)
    return "kill pawn using pawn"


def get_medium_mission():
    id = random(10) + 1
    query = ("SELECT description FROM medium_missions WHERE id = %d", id)
    description = Queries.query(query, None)
    return description


def get_hard_mission():
    id = random(10) + 1
    query = ("SELECT description FROM hard_missions WHERE id = %d", id)
    description = Queries.query(query, None)
    return description


def get_expert_mission():
    id = random(10) + 1
    query = ("SELECT description FROM expert_missions WHERE id = %d", id)
    description = Queries.query(query, None)
    return description

# def main():
#  current_mission_set()

# if __name__ == "__main__":
#   main()
