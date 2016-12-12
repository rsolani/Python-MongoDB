from MongoConnection import MongoConnection


def list_transactions():
    con = MongoConnection("transaction")
    col = con.get_collection

    r = col.find({"promotion.type": "MIN_VALUE_PLUS_PRODUCT"})

    for item in r:
        print(item)

    print(r.count())
