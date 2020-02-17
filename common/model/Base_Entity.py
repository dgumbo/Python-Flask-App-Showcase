class BaseEntity:

    def __init__(self, id=0, active_status=True, created_by="", creation_time="", updated_by="", update_time=""):
        self.id=id 
        self.active_status=active_status 
        self.created_by=created_by
        self.creation_time=creation_time
        self.updated_by=updated_by
        self.update_time=update_time
