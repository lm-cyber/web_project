from typing import List, Optional

from pydantic import BaseModel, ConfigDict, constr, conint







class ImageModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    proudct_id: int



