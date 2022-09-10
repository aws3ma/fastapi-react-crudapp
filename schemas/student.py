def student_entity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "full_name": db_item["full_name"],
        "email": db_item["email"],
        "phone": db_item["phone"]
    }


def list_of_students(db_item_list) -> list:
    list_stud_entity = []
    print(db_item_list)
    for item in db_item_list:
        list_stud_entity.append(student_entity(item))
    return list_stud_entity
