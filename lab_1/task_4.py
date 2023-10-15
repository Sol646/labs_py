users = ["comp1", "comp2", "tel1", "tel2", "comp2", "tel1", "comp2", "tel2"]
dict_ = {
    "Общее количество: ": 0,
    "Уникальные посещения: ": 0
}
dict_["Общее количество: "] = len(users)
dict_["Уникальные посещения: "] = len(set(users))

print(dict_)
