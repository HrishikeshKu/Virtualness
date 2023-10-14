from src.model import journey as journey_model


def store_journey_cards(journey_cards: list):
    # TODO: Do input validation if required.
    #  For the sake of simplicity and time constraint, it is ignored at this point.
    journey_model.journey_cards = []
    for journey_card in journey_cards:
        journey = journey_model.JourneyModel(
            journey_card['source'],
            journey_card['destination'],
            journey_card['journey_mode'],
            journey_card['reserve_seat'],
            journey_card['additional_info'])
        journey_model.journey_cards.append(journey)
    return journey_model.journey_cards


# Assumptions: No back edge present in journey.
# i.e. {a->b, b->c, b->c} is INVALID input.
# {a->b, b->c, c->d} is VALID input.
# {a->b, b->c, c->b, b->d} is INVALID input as back-edge present as c->b
# If back edge is allowed, problem is not possible to solve, unless we have source node.
def get_sorted_end_to_end_journey_details():
    journey_cards = journey_model.journey_cards
    src_node, dest_node = _get_source_destination_from_journey_cards(journey_cards)
    output: list[journey_model.JourneyModel] = _get_journey(journey_cards, src_node, dest_node)
    return _generate_text_from_sorted_journey_cards(output)


# Utility method for getting source and destination of journey.
# Logic is based on no. of indegree and outdegree of each node.
def _get_source_destination_from_journey_cards(journey_cards: list[journey_model.JourneyModel]):
    indegree_map: dict[str, int] = {}
    outdegree_map: dict[str, int] = {}

    for journey in journey_cards:
        indegree_map[journey.destination] = 1
        outdegree_map[journey.source] = 1
    src: str = ""
    destination: str = ""

    for journey_card in journey_cards:
        if journey_card.source not in indegree_map or indegree_map[journey_card.source] == 0:
            src = journey_card.source
        if journey_card.destination not in outdegree_map or outdegree_map[journey_card.destination] == 0:
            destination = journey_card.destination
    return src, destination


# Utility method to get end-to-end journey.
# Basic logic is do simple DFS. With assumption on input, each node will have one indegree and one outdegree.
# First create graph in `map_for_journey` and do DFS on graph to generate output.
def _get_journey(journey_cards: list[journey_model.JourneyModel], src: str, dest: str):
    map_for_journey: dict[str, journey_model.JourneyModel] = {}
    for journey in journey_cards:
        map_for_journey[journey.source] = journey

    end_to_end_journey: list[journey_model.JourneyModel] = []
    curr_node: str = src
    while curr_node != dest:
        end_to_end_journey.append(map_for_journey[curr_node])
        curr_node = map_for_journey[curr_node].destination

    return end_to_end_journey


# Utility method to generate sentence from JourneyModel.
def _generate_text_from_sorted_journey_cards(journey_cards: list[journey_model.JourneyModel]):
    output = ""
    id = 1
    for journey in journey_cards:
        output += "\n{}. Take {} from {} to {}.".format(id, journey.journey_mode, journey.source, journey.destination)
        if journey.reserve_seat == "":
            output += " No seat assignment."
        else:
            output += " Seat in the seat {}.".format(journey.reserve_seat)
        output += " {}".format(journey.additional_info)
        id += 1
    output += "\n{}. You have arrived at your final destination.".format(id)
    return output
