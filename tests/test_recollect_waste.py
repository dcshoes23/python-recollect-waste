# tests for recollect_waste
import recollect_waste
from datetime import date

class TestRecollectWaste:
    def test_get_next_pickup(self):
        place_id = '85E562F0-49EC-11E6-A261-153143E100E1'
        service_id = 339
        client = recollect_waste.RecollectWasteClient(place_id, service_id)
        pickup_event = client.get_next_pickup()

        assert hasattr(pickup_event, 'event_date')
        assert type(pickup_event.event_date) is date

        assert hasattr(pickup_event, 'pickup_types')
        assert type(pickup_event.pickup_types) is list
        assert len(pickup_event.pickup_types) > 0

        assert hasattr(pickup_event, 'area_name')
        assert pickup_event.area_name == "Abbotsford"