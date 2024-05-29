from api import TreeNode, API
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def tr_tree(self, node: TreeNode, address: str):
        if node is None:
            return
        self.slov.dict[node.id]=address
        for areas in node.areas:
            self.tr_tree(areas, address+', '+areas.name)

    def _apply_geocoding(self, area_id: str) -> str:
       if area_id in self.slov.dict:
            return self.slov.dict[area_id]
        else:
            return "бабаббабабаба"
        raise NotImplementedError()
