from app import db

class Transaction(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
   member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
   issue_date = db.Column(db.Date, nullable=False)
   return_date = db.Column(db.Date, nullable=True)
   fee_charged = db.Column(db.Float, default=0.0)

   def to_dict(self):
      return {
         "id": self.id,
         "book_id": self.book_id,
         "member_id": self.member_id,
         "issue_date": self.issue_date,
         "return_date": self.return_date,
         "fee_charged": self.fee_charged
      }