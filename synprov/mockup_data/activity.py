import uuid
import json


from synprov.models.activity import Activity
from synprov.mockup_data.dict import ActivityClasses
from synprov.util import get_datetime


class MockActivity(Activity):

    activity_classes = ActivityClasses

    def __init__(self, name='', class_idx=0):
        super().__init__(name=name)
        self.id = str(uuid.uuid1())
        self._class = self.activity_classes[class_idx]
        self.created_at = get_datetime()
        self.label = 'Activity'
        self.openapi_types.update({'label': str})

    def select_class(self, class_idx):
        self._class = self.activity_classes[class_idx]

    def get_class_count(self):
        return len(self.activity_classes)

    def get_data(self):
        return self.to_dict()
