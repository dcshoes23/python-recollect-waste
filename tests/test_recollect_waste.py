# tests for recollect_waste
import recollect_waste
from datetime import datetime

class TestRecollectWaste:
    def test_get_next_pickup(self):
        place_id = '85E562F0-49EC-11E6-A261-153143E100E1' # 1010 Cole Rd, Abbotsford
        client = recollect_waste.RecollectWasteClient(place_id)
        pickupevent = client.get_next_pickup()

        assert hasattr(pickupevent, 'event_date')
        assert type(pickupevent.event_date) is datetime

        assert hasattr(pickupevent, 'pickup_types')
        assert type(pickupevent.pickup_types) is list
        assert len(pickupevent.pickup_types) > 0

        assert hasattr(pickupevent, 'area_name')
        assert pickupevent.area_name == "Abbotsford"