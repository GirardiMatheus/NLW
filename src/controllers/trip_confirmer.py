from typing import Dict

class TripConfirmer:
    def __init__(self, trips_repository) ->None:
        delf.__trips_repository = trips_repository

    def confirm(self, trip_id) -> Dict:
        try:
            self._trips_repository.update_trip_status(trip_id)
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exeption)},
                "status_code": 400
            }