import uuid
from app.utils.database import db
from sqlalchemy.dialects.postgresql import UUID

class Customers(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  name = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  phone = db.Column(db.String(80), nullable=True)

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "phone": self.phone
    }