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

print("=== Player Inventory System ===\n")

user = "alice"

print(f"=== {user.capitalize()}'s Inventory ===")

user_items = data.get('players', {}).get(user, {}).get('items', {})
inventory_value = data.get('players', {}).get(user, {}).get('total_value', 0)
item_count = data.get('players', {}).get(user, {}).get('item_count', 0)
catalog = data['catalog']
items_types = {}


# for item, count in alice_inventory.items():

#     print(f"{item} ({catalog[item]['type']}, {catalog[item]['rarity']}): "
#           f"{count}x @ {catalog[item]['value']} gold each "
#           f"= {count * catalog[item]['value']} gold")

#     if catalog[item]['type'] in items_types:
#         items_types[catalog[item]['type']] += 1
#     else:
#         items_types[catalog[item]['type']] = 1

# print(f"\nInventory value: {inventory_value} gold")
# print(f"Item count: {item_count} items")
# print("Categories: ", end="")

# dict_len = len(items_types)

# for item, count in items_types.items():
#     print(f"{item}({count})", end="")
#     if dict_len > 1:
#         print(",", end=" ")
#     dict_len -= 1

fromm, to, item, count = "alice" , "bob", "pixel_sword", 1

print(f"\n\n=== Transaction: {fromm.capitalize()} gives {to.capitalize()} {count} {item} ===")

from_items = data.get('players', {}).get(fromm, {}).get('items', {})
to_items = data.get('players', {}).get(to, {}).get('items', {})
how_many = from_items.get(item, -1)

def update_inventory():

    from_inventory = data.get('players', {}).get(fromm, {})
    from_items = from_inventory.get('items', {})
    to_inventory = data.get('players', {}).get(to, {})
    to_items = to_inventory.get('items', {})
    how_many = from_items.get(item, -1)

    print(from_items)
    print(to_items)

    if how_many != -1:
        if how_many - count >= 0:

            if how_many - count > 0:
                from_items[item] -= count
            else:
                del from_items[item]
            
            from_inventory['total_value'] -= catalog[item]['value'] * count

            if item in to_items.items():
                to_items[item] += count
            else:
                to_items[item] = count

            to_inventory['total_value'] += catalog[item]['value'] * count
            print("Transaction successful!")
            
        else:
            print(f"Alice have only {how_many} of {item}")
    else:
        print(f"Alice do not have the item '{item}'")

    print(from_items)
    print(to_items)

update_inventory()

# print("=== Updated Inventories ===")

print(f"Alice potions: {from_items.get(item, 0)}")
print(f"Bob potions: {to_items.get(item, 0)}")

from_value = data.get('players', {}).get(fromm, {}).get('total_value', 0)
to_value = data.get('players', {}).get(to, {}).get('total_value', 0)

if from_value > to_value:
    print(f"Most valuable player: {fromm} ({from_value} gold)")
else:
    print(f"Most valuable player: {to} ({to_value} gold)")

from_count = data.get('players', {}).get(fromm, {}).get('item_count', 0)
to_count = data.get('players', {}).get(to, {}).get('item_count', 0)

if from_count > to_count:
    print(f"Most items: {fromm} ({from_count} items)")
else:
    print(f"Most items: {to} ({to_count} items)")

# if alice_items > bob_items:
#     print(f"Most items: Alice ({alice_value} items)")
# else:
#     print(f"Most items: Bob ({bob_value} items)")

# rarest_items = []

# for key in alice_inventory:
#     if alice_inventory[key]["rarity"] == "rare":
#         rarest_items.append(key)

# for key in bob_inventory:
#     if bob_inventory[key]["rarity"] == "rare":
#         rarest_items.append(key)

# items_len = len(rarest_items)

# print("Rarest items:", end=" ")
# for item in rarest_items:
#     print(item, end="")
#     if items_len > 1:
#         print(", ", end="")
#     items_len -= 1