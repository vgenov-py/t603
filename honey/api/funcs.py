import json

def get_all(con, t_n):
    result = {"data": []}
    cur = con().cursor()
    query = f"SELECT * FROM {t_n};"
    fields = tuple(field[1] for field in cur.execute(f"PRAGMA table_info({t_n})"))
    for element in cur.execute(query):
        result["data"].append(dict(zip(fields, element)))
    return json.dumps(result, sort_keys=False) 

def get_by_id(con, t_n, id):
    cur = con().cursor()
    fields = tuple(field[1] for field in cur.execute(f"PRAGMA table_info({t_n})"))
    query = f"SELECT * FROM {t_n} WHERE id= '{id}';"
    result = {"data": None}
    register = next(cur.execute(query), False)
    if register:
        result["data"]=dict(zip(fields, register))
        return json.dumps(result, sort_keys=False)
    else:
        return result["data"]
    

def gen_id(cur,t_n):
    last_id = next(cur.execute(f"SELECT max(id) FROM {t_n};"))[0]
    return last_id[0:3] + str(int(last_id[3:]) + 1).zfill(4)

def insert_into(con, t_n, form):
    cur = con().cursor()
    last_id = gen_id(cur, t_n)
    query = f'''INSERT INTO {t_n} VALUES ('{last_id}', "{form["name"]}", "{form["email"]}", 0);''' if t_n == "collectors" else f'''INSERT INTO {t_n} VALUES ('{last_id}', "{form["name"]}", "{form["email"]}");'''
    cur.execute(query)
    con().commit()
    return True