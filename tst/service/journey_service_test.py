import unittest
from src.service import journey_service
from src.model.journey import JourneyModel


class TestJourneyService(unittest.TestCase):
    def test_store_journey_cards(self):
        # Define a sample list of journey cards
        journey_cards = [
            {
                "source": "A",
                "destination": "B",
                "journey_mode": "Train",
                "reserve_seat": "A1",
                "additional_info": "Enjoy the journey."
            },
            {
                "source": "B",
                "destination": "C",
                "journey_mode": "Bus",
                "reserve_seat": "",
                "additional_info": "No seat assignment."
            }
        ]

        # Call the function under test
        result: list[JourneyModel] = journey_service.store_journey_cards(journey_cards)

        # Check if the journey cards were stored correctly
        self.assertEqual(len(result), len(journey_cards))
        for index in range(0, len(result)):
            self.assertEqual(result[index].source, journey_cards[index]["source"])
            self.assertEqual(result[index].destination, journey_cards[index]["destination"])
            self.assertEqual(result[index].journey_mode, journey_cards[index]["journey_mode"])
            self.assertEqual(result[index].reserve_seat, journey_cards[index]["reserve_seat"])
            self.assertEqual(result[index].additional_info, journey_cards[index]["additional_info"])

    def test_get_sorted_end_to_end_journey_details(self):
        # Mock journey cards
        journey_service.journey_model.journey_cards = [
            JourneyModel("A", "B", "Train", "A1", "Enjoy the journey."),
            JourneyModel("B", "C", "Bus", "", "Additional info.")
        ]

        # Call the function under test
        result = journey_service.get_sorted_end_to_end_journey_details()

        # Define the expected output
        expected_output = "\n1. Take Train from A to B. Seat in the seat A1. Enjoy the journey.\n2. Take Bus from B to C. No seat assignment. Additional info.\n3. You have arrived at your final destination."

        # Check if the result matches the expected output
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
