def create_booking(client, payload):
    return client.post("/booking", json=payload)


def get_booking(client, booking_id):
    return client.get(f"/booking/{booking_id}")


def update_booking(client, booking_id, payload, token):
    return client.put(
        f"/booking/{booking_id}",
        json=payload,
        headers={"Cookie": f"token={token}"},
    )


def delete_booking(client, booking_id, token):
    return client.delete(
        f"/booking/{booking_id}",
        headers={"Cookie": f"token={token}"},
    )