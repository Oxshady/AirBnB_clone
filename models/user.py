from models.base_model import BaseModel as b_S
class User(b_S):
    email=""
    password=""
    first_name=""
    last_name=""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self) -> str:
        """
        string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"
    