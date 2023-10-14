class JourneyModel:
    def __init__(self, source: str, destination: str, journey_mode: str, reserve_seat: str, additional_info: str):
        self.source = source
        self.destination = destination
        self.journey_mode = journey_mode
        self.reserve_seat = reserve_seat
        self.additional_info = additional_info


journey_cards: list[JourneyModel] = []
