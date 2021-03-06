from .models import db


class Warehouse:
    def __init__(self, schema):
        self._schema = schema

    def register(self, **kwargs):
        """ Register e  new object into the database.
            Args:
                parameters : List of object parameters.
            Returns:
                object: Database Object
        """
        _obj = self._schema(**kwargs)
        db.session.add(_obj)
        db.session.commit()

        return _obj

    def query(self, **kwargs):
        """ Query db objects filtering by parameters
            Args:
                parameters : List of parameters used to filter. 
        """
        objects = self._schema.query.filter_by(**kwargs).all()
        return objects

    def first(self, **kwargs):
        """ Query and return the first occurence.
            Args:
                parameters: List of parameters used to filter.
            Return:
                object: First object instance.
        """
        return self._schema.query.filter_by(**kwargs).first()

    def last(self, **kwargs):
        """ Query and return the first occurence.
            Args:
                parameters: List of parameters used to filter.
            Return:
                object: Last object instance.
        """
        return (
            self._schema.query.filter_by(**kwargs)
            .order_by(self._schema.id.desc())
            .first()
        )

    def contains(self, **kwargs):
        """ Check if the object id already exists into the database.
            Args:
                id: Object ID.
        """
        return self.first(**kwargs) != None

    def delete(self, **kwargs):
        """ Delete an object from the database.
            Args:
                parameters: Parameters used to filter the object.
        """
        object_to_delete = self.query(**kwargs)
        db.session.delete(object_to_delete)
        db.session.commit()

    def update(self):
        db.session.commit()
