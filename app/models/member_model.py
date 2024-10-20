from app import db

class Member(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(100), unique=True, nullable=False)
   outstanding_debt = db.Column(db.Float, default=0.0)

   def to_dict(self):
      return {
         "id": self.id,
         "name": self.name,
         "email": self.email,
         "outstanding_debt": self.outstanding_debt
      }