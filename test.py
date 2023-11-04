from sqlalchemy import select

from db import get_session, ProductOrm
from db import service

session = get_session()
# new_product = ProductOrm(name='asdddd')
# session.add(new_product)
# session.commit()
test = session.execute(select(ProductOrm).order_by(ProductOrm.id).limit(20))
for i in test:
    print(**i[0].dict())