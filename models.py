import os
import hashlib

import sqlalchemy as sa
from sqlalchemy import func

from config import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(255), nullable=False)
    encoded_passwd = db.Column(db.String(255), nullable=False)

    def __init__(self, account, passwd):
        self.account = account
        self.encoded_passwd = User.encode_passwd(passwd)

    @classmethod
    def encode_passwd(cls, passwd):
        data = passwd + os.getenv('SECRET_TOKEN', '')
        m = hashlib.md5()
        m.update(data.encode('utf8'))
        encoded_passwd = m.hexdigest()
        return encoded_passwd


class Spot(db.Model):
    __tablename__ = 'Spots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    zone = db.Column(db.String(20), nullable=False)
    describe = db.Column(db.String(5000))
    tel = db.Column(db.String(255))
    website = db.Column(db.String(500))
    keyword = db.Column(db.String(255))
    address = db.Column(db.String(500))
    pic1 = db.Column(db.String(500))
    pic2 = db.Column(db.String(500))
    pic3 = db.Column(db.String(500))
    px = db.Column(db.Float(precision=18))
    py = db.Column(db.Float(precision=18))

    def __init__(self, name, zone, describe, tel, website, keyword, address, pic1, pic2, pic3, px, py):
        self.name = name
        self.zone = zone
        self.describe = describe
        self.tel = tel
        self.website = website
        self.keyword = keyword
        self.address = address
        self.pic1 = pic1
        self.pic2 = pic2
        self.pic3 = pic3
        self.px = px
        self.py = py

    def to_dict(self):
        return dict(
            name=self.name,
            zone=self.zone,
            describe=self.describe,
            tel=self.tel,
            website=self.website,
            keyword=self.keyword,
            address=self.address,
            pic=[p for p in [self.pic1, self.pic2, self.pic3] if p],
            px=self.px,
            py=self.py,
        )


class Project(db.Model):
    __tablename__ = 'Projects'

    proj_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    start_day = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    end_day = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    plan = db.Column(db.String(5000), nullable=False)
    created_time = db.Column(db.TIMESTAMP(timezone=True), nullable=False,
                             server_default=func.now())
    update_time = db.Column(
        db.TIMESTAMP(timezone=True), nullable=False,
        server_default=func.now(), onupdate=func.current_timestamp()
    )

    def __init__(self, name, owner, start_day, end_day, plan):
        self.name = name
        self.owner = owner
        self.start_day = start_day
        self.end_day = end_day
        self.plan = plan


class FavoriteSpot(db.Model):
    __tablename__ = 'FavoriteSpots'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    spot_id = db.Column(db.Integer, db.ForeignKey("Spots.id"), nullable=False)

    def __init__(self, user_id, spot_id):
        self.user_id = user_id
        self.spot_id = User.spot_id
