from datetime import datetime

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            # id=self.id,
            ogirinal=self.original,
            short=self.short,
            # timestamp=self.timestamp,
        )

    def from_dict(self, data):

        fields = {
            "url": "original",
            "custom_id": "short"
        }
        """Десириализация данных: добавление в пустой объект класса URLMap 
        значения полей, которые были получены в POST-запросе"""
        for field in ['url', 'custom_id']:
            if field in data:
                field_name = fields[field]
                setattr(self, field_name, data[field])