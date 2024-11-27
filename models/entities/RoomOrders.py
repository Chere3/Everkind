class RoomOrders:
    def __init__(
        self, id, user_id, room_id, order_date, status, created_at, updated_at
    ):
        self.id = id
        self.user_id = user_id
        self.room_id = room_id
        self.order_date = order_date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
