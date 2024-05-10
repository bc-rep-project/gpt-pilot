# from peewee import *
from peewee import ForeignKeyField, AutoField, TextField, IntegerField, CharField
from database.config import DATABASE_TYPE
from database.models.components.base_models import BaseModel
from database.models.app import App
from database.models.components.sqlite_middlewares import JSONField
from playhouse.postgres_ext import BinaryJSONField


class DevelopmentSteps(BaseModel):
    id = AutoField()  # This will serve as the primary key
    app = ForeignKeyField(App, on_delete='CASCADE')
    prompt_path = TextField(null=True)
    llm_req_num = IntegerField(null=True)
    token_limit_exception_raised = TextField(null=True)

    if DATABASE_TYPE == 'postgres':
        messages = BinaryJSONField(null=True)
        llm_response = BinaryJSONField(null=False)
        prompt_data = BinaryJSONField(null=True)
    else:
        messages = JSONField(null=True)  # Custom JSON field for SQLite
        llm_response = JSONField(null=False)  # Custom JSON field for SQLite
        prompt_data = JSONField(null=True)

    previous_step = ForeignKeyField('self', null=True, column_name='previous_step')
    high_level_step = CharField(null=True)

#--------------no.1-----

    # parent_step = ForeignKeyField('self', backref='child_steps', null=True)
    
    # # (Optional) Add a field to store the type of action 
    # # (file change, command, human intervention) for easier processing during undo/redo.
    # action_type = CharField(null=True)

#--------------no.2-----

    parent_step = ForeignKeyField(
        'self', 
        null=True, 
        backref='child_steps',
        on_delete='CASCADE'  # Ensure child steps are deleted when parent is deleted 
    )

    # Additional fields for undo/redo
    previous_file_content = TextField(null=True)  # Stores previous content for file changes
    command_to_undo = TextField(null=True)  # Stores undo command (if applicable)

    class Meta:
        database = db  # This is the database connection
        
        # (Optional) Add indexes for faster querying 
        indexes = (
            (('parent_step', 'action_type'), False), 
        )

    # class Meta:
    #     table_name = 'development_steps'
    #     indexes = (
    #         (('app', 'previous_step', 'high_level_step'), True),
    #     )