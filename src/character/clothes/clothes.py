from src.components import Component
from src.character.clothes.piece import Piece
from src.character.clothes.underwear import Underwear
from src.character.clothes.half_dressed import HalfDressed
from src.utils import stringify_tags


class Clothes(Component):

    def __init__(self, data):
        super().__init__(data)
        self.underwear = Underwear(self.data)
        self.half_dressed = HalfDressed(self.data)

    def get_clothes(self):
        type = self.data.random_data["clothes"]["types"]
        match type[0]:
            case "swimsuit":
                return self.get_swimsuit()
            case "clothed":
                return self.get_clothed()
            case "nude":
                return ["nude"]
    
    def get_underwear(self):
        type = self.data.random_data["clothes"]["types"]
        match type[0]:
            case "clothed":
                return self.underwear.prompt
            case "swimsuit":
                return self.get_swimsuit()

    def get_clothed(self):
        vest = self.data.random_data["clothes"]["vest"]
        top = self.data.random_data["clothes"]["top"]
        bottom = self.data.random_data["clothes"]["bottom"]
        return [
            f"{stringify_tags(vest['colors'])} {stringify_tags(vest['types'])}",
            f"{stringify_tags(top['colors'])} {stringify_tags(top['types'])}",
            f"{stringify_tags(bottom['colors'])} {stringify_tags(bottom['types'])}"
        ]
    def get_swimsuit(self):
        prefix = "swimsuit"
        swimsuit = self.data.random_data["clothes"]["swimsuit"]
        if "one-piece" in swimsuit["types"]:
            one_piece = swimsuit["one-piece"]
            cleavage = stringify_tags(one_piece["cleavage"]["types"])
            cutout = ""
            if cleavage != "":
                cutout = stringify_tags(one_piece["cleavage"]["cutout"]["types"])
            color = stringify_tags(one_piece["colors"])
            return [
                prefix,
                cleavage,
                cutout,
                f"{color} one-piece swimsuit"
            ]
        if "bikini" in swimsuit["types"]:
            bikini = swimsuit["bikini"]
            color = stringify_tags(bikini["colors"])
            type = stringify_tags(bikini["types"])
            return [
                prefix,
                f"{color} {type} bikini"
            ]
    def get_uniform(self):
        uniform = self.data.random_data["clothes"]["uniform"]
        color = stringify_tags(uniform["colors"])
        type = stringify_tags(uniform["types"])
        return [
            f"{color} uniform",
            f"{type} uniform"
        ]

    def build_prompt(self):
        state = self.data.random_data["clothes"]["states"]
        type = self.data.random_data["clothes"]["types"]
        match state[0]:
            case "clothed":
                prompt = self.get_clothes()
                    
            case "half-clothed":
                top_undressed_prompt = self.half_dressed.get_top_undressed()
                bottom_undressed_prompt = self.half_dressed.get_bottom_undressed()
                half_clothes_prompt = self.half_dressed.get_half_clothes()
                half_underwear_prompt = self.half_dressed.get_half_underwear()
                clothes = self.get_clothes()
                if half_clothes_prompt == [""]:
                    clothes = [""]
                underwear = self.get_underwear()
                if half_underwear_prompt == [""]:
                    underwear = [""]
                prompt = ["partially undressed"] + top_undressed_prompt + bottom_undressed_prompt + clothes + half_clothes_prompt + underwear + half_underwear_prompt
            # case "underwear":
                
            case "nude":
                prompt = ["nude"]
        self.prompt = prompt

