from sqlalchemy import Column, Integer, String, ForeignKey
from models.Base import Base
from sqlalchemy.orm import relationship


class Course(Base):
    __tablename__ = 'course'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    subject = Column('subject', String)
    language = Column('language', String)
    author = Column(Integer, ForeignKey('author.id'))
    user = Column(Integer, ForeignKey('user.id'))

    def __str__(self) -> str:
        return self.get_details().__str__()

    def get_details(self):
        info = {
            'name': self.name,
            'subject': self.subject,
            'language': self.language,
            'author': self.author,
            'user': self.user,
        }
        if hasattr(self, 'id'):
            info['id'] = self.id
        return info

    def from_csv(self, headers: str, values: str, sep=','):
        headers_list = headers.split(sep)
        values_list = values.split(sep)
        print(headers_list)
        print(values_list)
        assert len(headers_list) == len(values_list)
        for header, value in zip(headers_list, values_list):
            if hasattr(self, header):
                value = self.validate_header_value(header, value)
                setattr(self, header, value)

    def validate_header_value(self, header, value):
        return value
