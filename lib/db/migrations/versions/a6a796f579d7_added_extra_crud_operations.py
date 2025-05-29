from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    with op.batch_alter_table("guest_rooms") as batch_op:
        batch_op.drop_constraint("fk_guest_rooms_room_id", type_="foreignkey")
        batch_op.drop_constraint("fk_guest_rooms_guest_id", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_guest_rooms_room_id",
            "rooms",
            ["room_id"],
            ["id"],
            ondelete="CASCADE",
        )
        batch_op.create_foreign_key(
            "fk_guest_rooms_guest_id",
            "guests",
            ["guest_id"],
            ["id"],
            ondelete="CASCADE",
        )


def downgrade() -> None:
    with op.batch_alter_table("guest_rooms") as batch_op:
        batch_op.drop_constraint("fk_guest_rooms_room_id", type_="foreignkey")
        batch_op.drop_constraint("fk_guest_rooms_guest_id", type_="foreignkey")
        batch_op.create_foreign_key(
            "fk_guest_rooms_room_id",
            "rooms",
            ["room_id"],
            ["id"],
        )
        batch_op.create_foreign_key(
            "fk_guest_rooms_guest_id",
            "guests",
            ["guest_id"],
            ["id"],
        )
