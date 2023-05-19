from dataclasses import dataclass


@dataclass
class League:
    id: int
    name: str = None

    @property
    def url(self):
        return f"liga/{id}"

