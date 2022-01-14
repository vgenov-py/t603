import json

DB = "bookshop.json"

def get_all(json_file):
    with open(json_file, encoding="utf8") as file:
        return json.load(file)

def write_data(data):
    with open(DB, "w", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_by_id(book_id):
    return next(filter(lambda book: book["id"] == book_id, get_all(DB)["data"]), False)

def delete_by_id(book_id):
    book_to_delete = get_by_id(book_id)
    if book_to_delete:
        data = get_all(DB)
        data["data"].remove(book_to_delete)
        write_data(data)
        return True
    else:
        return False

def update_book(book_id, request):
    book_to_update = get_by_id(book_id)
    if book_to_update:
        data = get_all(DB)
        i = data["data"].index(book_to_update)
        for k, v in request.form.items():
            if k in book_to_update.keys():
                if k == "stock":
                    book_to_update[k] = int(v)
                else:
                    book_to_update[k] = v
        data["data"][i] = book_to_update
        write_data(data)
        return True
    return False