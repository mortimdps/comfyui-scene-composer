from src.components import Component
from src.character.clothes.underwear import Underwear
from src.utils import stringify_tags


class HalfDressed(Component):

    def __init__(self, data):
        super().__init__(data)
    
    def get_half_underwear(self):
        if not "half-underwear" in self.data.random_data["clothes"]["half"]:
            return [""]
        half_underwear = self.data.random_data["clothes"]["half-underwear"]
        bra = stringify_tags(half_underwear["bra"])
        panties_type = half_underwear["types"]
        panty_prompt = []
        if "panties" in panties_type:
            panty_prompt = [
                f"panties {stringify_tags(half_underwear['panties'])}"
            ]
        if "panties-around" in panties_type:
            panty_prompt = [
                f"panties around {stringify_tags(half_underwear['panties-around'])}"
            ]
        return [
            f"bra {bra}"
        ] + panty_prompt
    def get_half_clothes(self):
        if not "half-clothes" in self.data.random_data["clothes"]["half"]:
            return [""]
        half_clothes = stringify_tags(self.data.random_data["clothes"]["half-clothes"])
        return [
            f"clothes {half_clothes}"
        ]
        
    def get_top_undressed(self):
        if not "top-undressed" in self.data.random_data["clothes"]["undressed"]["types"]:
            return [""]
        top_undressed = stringify_tags(self.data.random_data["clothes"]["top-undressed"])
        nipple = stringify_tags(self.data.random_data["character"]["body"]["breasts"]["nipples"])
        return [
            f"{top_undressed}",
            nipple
        ]
    
    def get_bottom_undressed(self):
        if not "bottom-undressed" in self.data.random_data["clothes"]["undressed"]["types"]:
            return [""]
        bottom_undressed = stringify_tags(self.data.random_data["clothes"]["bottom-undressed"])
        return [
            f"{bottom_undressed}",
            "pussy"
        ]
