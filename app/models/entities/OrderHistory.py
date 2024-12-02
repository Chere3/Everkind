class OrderHistory:
    def __init__(
        self,
        user_id,
        occupant_id,
        visit_id,
        order_id,
        action,
        action_date,
        created_at,
        updated_at,
    ):
        self.user_id = user_id
        self.occupant_id = occupant_id
        self.visit_id = visit_id
        self.order_id = order_id
        self.action = action
        self.action_date = action_date
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"OrderHistory: {self.user_id} {self.occupant_id} {self.visit_id} {self.order_id} {self.action} {self.action_date} {self.created_at} {self.updated_at}"
