from sqlalchemy.dialects.postgresql import UUID

from db import db
from models import User
from models.mixins import CreatedUpgradeTimeMixin

# class SocialAccount(CreatedUpgradeTimeMixin):
#     """
#     social_id:
#         строка, которая определяет уникальный идентификатор из сторонней службы аутентификации,
#         используемой для входа в систему.
#     """
#
#     __tablename__ = 'social_account'
#
#     user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
#     user = db.relationship(User, backref=db.backref('social_accounts', lazy=True))
#
#     social_id = db.Column(db.String(length=100), nullable=False)
#     social_name = db.Column(db.String(length=100), nullable=False)
#
#     __table_args__ = (db.UniqueConstraint('social_id', 'social_name', name='social_pk'),)
#
#     def __repr__(self) -> str:
#         return f'<SocialAccount {self.social_name}:{self.user_id}>'