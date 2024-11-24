class Occupant:
    def __init__(
        self,
        id,
        user_id,
        room_id,
        start_date,
        end_date,
        created_at,
        updated_at,
        guest_id,
    ) -> None:
        self.id = id
        self.user_id = user_id
        self.room_id = room_id
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.guest_id = guest_id
