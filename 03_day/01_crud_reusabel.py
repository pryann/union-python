def generate_id(items):
    try:
        return max(item["id"] for item in items) + 1
    except ValueError:
        return 1


def get_items(items):
    return items


def find_item(id, items):
    for item in items:
        if item["id"] == id:
            return item


def create_item(item, items):
    new_item = {"id": generate_id()}
    new_item.update(item)
    items.append(new_item)
    return items[-1]


def update_item(id, item, items):
    item_from_list = find_item(id)
    if item_from_list is not None:
        index = items.index(item_from_list)
        items[index].update(item)
        return items[index]


def delete_item(id, items):
    item = find_item(id)
    if item is not None:
        items.remove(item)
