from sqlalchemy.orm import declarative_base, declared_attr

from sqlalchemy.orm import registry

mapper_registry = registry()


@mapper_registry.as_declarative_base()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


mapper_registry.configure(Base)
