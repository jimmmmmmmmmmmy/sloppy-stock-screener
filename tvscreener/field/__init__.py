from enum import Enum


class TimeInterval(Enum):
    ONE_MINUTE = "1"
    FIVE_MINUTES = "5"
    FIFTEEN_MINUTES = "15"
    THIRTY_MINUTES = "30"
    SIXTY_MINUTES = "60"
    TWO_HOURS = "120"
    FOUR_HOURS = "240"
    ONE_DAY = "1D"
    ONE_WEEK = "1W"

    def update_mode(self):
        return f"update_mode|{self.value}"


def add_time_interval(field_name, time_interval):
    return f"{field_name}|{time_interval.value}"


def add_historical(field_name, historical=1):
    return f"{field_name}[{historical}]"


def add_historical_to_label(field_name, historical=1):
    return f"Prev. {field_name}"


def add_rec(field_name):
    return f"Rec.{field_name}"


def add_rec_to_label(label):
    return f"Reco. {label}"


class Field(Enum):

    def __init__(self, label, field_name, format_=None, interval=False, historical=False):
        self.label = label
        self.field_name = field_name
        self.format = format_
        self.interval = interval
        self.historical = historical

    def has_recommendation(self):
        return self.format == 'recommendation'

    def get_rec_label(self):
        if self.has_recommendation():
            return add_rec_to_label(self.label)
        return None

    @classmethod
    def get_by_label(cls, specific_fields, label):
        for specific_field in specific_fields:
            if specific_field.label == label:
                return specific_field
        return None


