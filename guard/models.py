from tortoise import Model, fields


class Project(Model):
    name = fields.CharField(max_length=50, unique=True)
    secret = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Log(Model):
    project = fields.ForeignKeyField("models.Project")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
