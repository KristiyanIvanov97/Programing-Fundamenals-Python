jedis = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")
        if force_side not in jedis.keys():
            jedis[force_side] = []
            jedis[force_side].append(force_user)
        else:
            continue
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for value in jedis.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in jedis.keys():
            jedis[force_side] = []
        jedis[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for force_side, force_user in jedis.items():
    if len(force_user) > 0:
        print(f"Side: {force_side}, Members: {len(jedis[force_side])}")
        for user in force_user:
            print(f"! {user}")


