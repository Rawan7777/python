#!/usr/bin/env python3

data = {
    'players': {
        'alice': {
            'items': {
                'pixel_sword': 1,
                'code_bow': 1,
                'health_byte': 1,
                'quantum_ring': 3
            },
            'total_value': 1875,
            'item_count': 6
        },
        'bob': {
            'items': {
                'code_bow': 3,
                'pixel_sword': 2
            },
            'total_value': 900,
            'item_count': 5
        },
        'charlie': {
            'items': {
                'pixel_sword': 1,
                'code_bow': 1
            },
            'total_value': 350,
            'item_count': 2
        },
        'diana': {
            'items': {
                'code_bow': 3,
                'pixel_sword': 3,
                'health_byte': 3,
                'data_crystal': 3
            },
            'total_value': 4125,
            'item_count': 12
        }
    },
    'catalog': {
        'pixel_sword': {
            'type': 'weapon',
            'value': 150,
            'rarity': 'common'
        },
        'quantum_ring': {
            'type': 'accessory',
            'value': 500,
            'rarity': 'rare'
        },
        'health_byte': {
            'type': 'consumable',
            'value': 25,
            'rarity': 'common'
        },
        'data_crystal': {
            'type': 'material',
            'value': 1000,
            'rarity': 'legendary'
        },
        'code_bow': {
            'type': 'weapon',
            'value': 200,
            'rarity': 'uncommon'
        }
    }
}

if __name__ == "__main__":

    print("=== Player Inventory System ===\n")

    user = "alice"
    user_inventory = data.get("players", {}).get(user, {})

    if user_inventory:

        print(f"=== {user.capitalize()}'s Inventory ===")

        user_items = user_inventory.get("items", {})
        catalog = data["catalog"]
        items_types = {}

        for item, count in user_items.items():

            item_type = catalog[item]["type"]
            rarity = catalog[item]["rarity"]
            value = catalog[item]["value"]
            total_item_value = count * value

            print(
                f"{item} ({item_type}, {rarity}): "
                f"{count}x @ {value} gold each "
                f"= {total_item_value} gold"
            )

            if item_type in items_types:
                items_types[item_type] += 1
            else:
                items_types[item_type] = 1

        inventory_value = user_inventory.get("total_value", 0)
        item_count = user_inventory.get("item_count", 0)

        print(f"\nInventory value: {inventory_value} gold")
        print(f"Item count: {item_count} items")
        print(
            "Categories:",
            ", ".join(
                f"{item}({count})"
                for item, count in items_types.items()
            ),
        )

        from_p, to_p, item, count = "alice", "bob", "quantum_ring", 1

        print(
            f"\n=== Transaction: {from_p.capitalize()} gives "
            f"{to_p.capitalize()} {count} {item} ==="
        )

        from_inventory = data.get("players", {}).get(from_p, {})
        from_items = from_inventory.get("items", {})
        to_inventory = data.get("players", {}).get(to_p, {})
        to_items = to_inventory.get("items", {})

        if from_items and to_items:

            how_many = from_items.get(item, -1)

            def update_inventory():

                if how_many != -1:

                    if how_many - count >= 0:

                        if how_many - count > 0:
                            from_items[item] -= count
                        else:
                            del from_items[item]

                        from_inventory["total_value"] -= (
                            catalog[item]["value"] * count
                        )
                        from_inventory["item_count"] -= count

                        if item in to_items:
                            to_items[item] += count
                        else:
                            to_items[item] = count

                        to_inventory["total_value"] += (
                            catalog[item]["value"] * count
                        )
                        to_inventory["item_count"] += count

                        print("Transaction successful!\n")

                    else:
                        print(f"Alice has only {how_many} of {item}")
                        print("Transaction failed!\n")
                else:
                    print(f"Alice does not have the item '{item}'")
                    print("Transaction failed!\n")

            update_inventory()

            print("=== Updated Inventories ===")

            print(f"Alice {item}: {from_items.get(item, 0)}")
            print(f"Bob {item}: {to_items.get(item, 0)}")

        else:
            print(f"One or both players '{from_p}' or '{to_p}' not found")
            print("Transaction failed!\n")

        print("\n=== Inventory Analytics ===")

        values_dict = {}
        items_dict = {}

        players = data["players"]

        for key, value in players.items():
            values_dict[key] = value["total_value"]
            items_dict[key] = value["item_count"]

        max_p_v = max(values_dict, key=values_dict.get)
        max_value = values_dict[max_p_v]

        max_p_c = max(items_dict, key=items_dict.get)
        max_count = items_dict[max_p_c]

        print(f"Most valuable player: {max_p_v} ({max_value} gold)")
        print(f"Most items: {max_p_c} ({max_count} items)")

        rarest_items = set()

        for value in players.values():
            for s_key in value["items"]:
                if catalog[s_key]["rarity"] == "rare":
                    rarest_items.add(s_key)

        rarest_items_string = ", ".join(rarest_items)

        print(f"Rarest items: {rarest_items_string}")

    else:
        print(f"The player {user} is not found")
