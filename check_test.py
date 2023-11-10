from db import engine, ProductOrm, ProductModel

engine.connect()

print(engine)

co_orm = ProductOrm(
    name="Testing",
    id_photos=[1, 2, 3],
)
print(co_orm)
co_model = ProductModel.model_validate(co_orm)
print(co_model)
