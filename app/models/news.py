from pydantic import BaseModel, ConfigDict, constr, conint


class NewNewsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=128)
    description: constr(max_length=1024)


class Image(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int


class NewsAdded(NewNewsModel):
    id: int


class NewsModel(NewsAdded):
    images: list[Image]
