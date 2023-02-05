class Task:
    def __init__(self, name, created_at, task_id=None, updated_at=None):
        self.name = name
        self.created_at = created_at
        self.task_id = task_id
        self.updated_at = updated_at

    def get_attrs_as_dict(self):
        return {
            "id": self.task_id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }