from pydantic import BaseModel, ConfigDict, constr, conint


class NewCertModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: constr(max_length=128)


class Image(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CertAdded(NewCertModel):
    id: int


class CertModel(CertAdded):
    images: list[Image]
