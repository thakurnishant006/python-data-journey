#---------- Functions-------
def tag_record(record: str, *tags) -> dict:
    return{
        "record" : record,
        "tags" : list(tags)
    }

def build_config(**kwargs) -> dict:
    return kwargs

def find_max(*number : float) -> float:
    big = number[0]
    for i in number:
        if big < i:
            big = i
    return big

def format_record(name : str , value : float , currency : str = "INR" , decimals : int = 2) -> int:
    return f"{name} : {currency}{value:,.{decimals}f}"

def merge_configs(base : dict , override : dict) -> dict:
    merge_dict = base | override
    return merge_dict

if __name__ == "__main__":
    print(tag_record("employee", "active", "senior", "python"))
    print(build_config(host="localhost", port=5432, db="sales"))
    print(find_max(5, 3, 8, 1, 42, 7))
    print(format_record("salary", 95000))
    print(merge_configs({"host": "localhost", "port": 5432}, {"port": 9999, "db": "sales"}))