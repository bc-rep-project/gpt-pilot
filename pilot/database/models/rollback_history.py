from peewee import ForeignKeyField
from database.models.components.base_models import BaseModel
from database.models.app import App
from database.models.components.sqlite_middlewares import JSONField


class RollbackHistory(BaseModel):
    app = ForeignKeyField(App, on_delete='CASCADE')
    step_id = UUIDField()
    step_data = JSONField()