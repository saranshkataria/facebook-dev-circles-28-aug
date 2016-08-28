from sqlalchemy_utils import ChoiceType, EmailType, JSONType
from event_management import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(EmailType, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    contact = db.Column(db.String(10))
    is_walk_in = db.Column(db.Boolean, default=False)
    extra_json = db.Column(JSONType)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    venue = db.Column(db.Text())
    time = db.Column(db.DateTime())
    desc = db.Column(db.Text())
    capacity = db.Column(db.Integer())
    email_template = db.Column(db.Text(), required=False)


class EventAttendee(db.Model):
    INVITE_STATUS_NOT_SENT = 0
    INVITE_STATUS_SENT = 1
    INVITE_STATUS_RSVP_TRUE = 2
    INVITE_STATUS_RSVP_FALSE = 3
    
    INVITE_STATUS_CHOICES = [
        (INVITE_STATUS_NOT_SENT, u'Invite Not Sent'),
        (INVITE_STATUS_SENT, u'Invite Sent'),
        (INVITE_STATUS_RSVP_TRUE, u'Invite Accepted'),
        (INVITE_STATUS_RSVP_FALSE, u'Invite Rejected'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    invite_status = db.Column(ChoiceType(INVITE_STATUS_CHOICES), default=INVITE_STATUS_NOT_SENT)
    is_present = db.Column(db.Boolean(), default=False)

    attendee_id = db.Column(db.Integer, db.ForeignKey('attendee.id'))
    attendee = db.relationship("Attendee", foreign_keys=[attendee_id])

    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event = db.relationship("Event", foreign_keys=[attendee_id])
