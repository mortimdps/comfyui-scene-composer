from src.components import Component
from src.character.clothes.piece import Piece
from src.utils import stringify_tags


class Underwear(Component):

    def __init__(self, data):
        super().__init__(data)
        self.build_prompt()

    def get_bra(self):
        type = stringify_tags(self.data.random_data["clothes"]["bra"]["types"])
        color = stringify_tags(self.data.random_data["clothes"]["bra"]["colors"])
        extras = stringify_tags(self.data.random_data["clothes"]["bra"]["extras"]["types"])
        return [
            f"{extras} {color} {type}"
        ]
    def get_panties(self):
        type = stringify_tags(self.data.random_data["clothes"]["panties"]["types"])
        color = stringify_tags(self.data.random_data["clothes"]["panties"]["colors"])
        extras = stringify_tags(self.data.random_data["clothes"]["panties"]["extras"]["types"])
        return [
            f"{extras} {color} {type}"
        ]
    def get_socks(self):
        type = stringify_tags(self.data.random_data["clothes"]["socks"]["types"])
        color = stringify_tags(self.data.random_data["clothes"]["socks"]["colors"])
        extras = stringify_tags(self.data.random_data["clothes"]["socks"]["extras"]["types"])
        return [
            f"{extras} {color} {type}"
        ]
        
    def build_prompt(self):
        bra = self.get_bra()
        panties = self.get_panties()
        socks = self.get_socks()
        
        self.prompt = bra + panties + socks
        
