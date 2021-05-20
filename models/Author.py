from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.Person import Person


class Author(Person):
    __tablename__ = 'author'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    email = Column('email', ForeignKey('person.email'), nullable=False)
    courses = relationship('Course')

    def __str___(self) -> str:
        return super().__str___()

    def get_info(self):
        info = super(Author, self).get_info()
        return info

    def validate_header_value(self, header, value):
        value = super().validate_header_value(header, value)
        if header == 'id':
            value = int(value)
        return value
