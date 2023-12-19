from db import init_models
import asyncio

if __name__ == "__main__":
    asyncio.run(init_models())
    print("Done")




#
#
# from shema import TypeOfProductOrm
#
# from sqlalchemy import select, create_engine, Engine
#
#
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # Create an engine and session
# engine: Engine = create_engine("postgresql+psycopg2://docker:docker@localhost/docker")
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Specify the type_of_product name for which you want to retrieve products
# type_of_product_name = "your_type_of_product_name"
#
# # Query the TypeOfProductOrm to get the id of the specified type_of_product
# # type_of_product = session.query(TypeOfProductOrm).filter_by(name=type_of_product_name).first()
#
# if True:
#     # Query the ProductOrm to get all products associated with the specified type_of_product
#     ttt = session.query(TypeOfProductOrm).all()
#
#     for t in ttt:
#         print(t.product)
#         for elem in t.product:
#             print(elem.name)
#
# session.close()
