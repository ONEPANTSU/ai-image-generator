from dataclasses import dataclass


@dataclass
class Request:
    width: int
    height: int
    prompt: str
    submitted: bool

    def get_dict(self):
        return {
            'width': self.width,
            'height': self.height,
            'prompt': self.prompt,
        }
