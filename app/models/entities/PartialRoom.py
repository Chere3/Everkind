class PartialRoom:
    def __init__(
        self,
        id,
        name,
        room_number,
        capacity,
        created_at,
        updated_at,
        room_type_id,
        room_type_photo,
    ):
        self.id = id
        self.name = name
        self.room_number = room_number
        self.capacity = capacity
        self.created_at = created_at
        self.updated_at = updated_at
        self.room_type_id = room_type_id
        self.room_type_photo = room_type_photo
