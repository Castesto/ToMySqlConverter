
from dataclasses import dataclass


@dataclass
class ColumnTables:
    products: [str]
    products_data_all: [str]
    products_stores: [str]
    transactions: [str]


def get_columns() -> ColumnTables:
    return ColumnTables(**{
        "products": ["ID_PRODUCT", "NAME", "CATEGORY", "UNITS", "WEIGHT"],
        "products_data_all": ["ID_PRODUCT", "NAME", "CATEGORY", "UNITS", "WEIGHT", "PRICE", "DATE_UPD", "ID_STORE",
                              "NAME_STORE"],
        "products_stores": ["ID_PRODUCT", "PRICE", "ID_STORE", "DATE_UPD"],
        "transactions": ["USER_ID", "ID_TRANSACTION", "ID_STORE", "ID_PRODUCT", "DATE", "UNIQUE_ID"]
    })


tables = get_columns()
print(', '.join(tables.products_data_all))
