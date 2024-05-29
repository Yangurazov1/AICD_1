from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: int) -> str:
        area_id = str(area_id) # думаю, что не суть, как эта строка реализована

        for country in self.__data:
            for area in country.areas:
                for sity in area.areas:
                    if sity.id == area_id:
                        return f"{country.name} {area.name} {sity.name}"
                if area.id == area_id:
                    return f"{country.name} {area.name}"
            if country.id == area_id:
                return f"{country.name}"

        raise NotImplementedError()
