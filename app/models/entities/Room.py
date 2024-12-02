class Room:
    def __init__(self, room, type):
        self.id = room.id
        self.name = room.name
        self.description = type.description
        self.room_number = room.room_number
        self.capacity = room.capacity
        self.room_type = type.id
        self.room_photo = type.photo
        self.created_at = room.created_at
        self.updated_at = room.updated_at
