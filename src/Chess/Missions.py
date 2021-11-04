import random, sys

sys.path.append("../SQL")
import Queries

def current_mission_set():
    get_easy_mission()
    get_medium_mission()
    get_hard_mission()
    get_expert_mission()
    
def get_easy_mission():
    id = random.randint(1,10)
    query = "SELECT description FROM easy_missions WHERE id = %s;"
    description = Queries.getSQuery(query, id)
    return description


def get_medium_mission():
    id = random.randint(1,10)
    query = "SELECT description FROM medium_missions WHERE id = %s;"
    description = Queries.getSQuery(query, id)
    return description


def get_hard_mission():
    id = random.randint(1,10)
    query = "SELECT description FROM hard_missions WHERE id = %s;"
    description = Queries.getSQuery(query, id)
    return description


def get_expert_mission():
    id = random.randint(1,8)
    query = "SELECT description FROM expert_missions WHERE id = %s;"
    description = Queries.getSQuery(query, id)
    return description

# def main():
#  current_mission_set()

# if __name__ == "__main__":
#   main()