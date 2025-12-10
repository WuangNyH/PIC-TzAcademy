# BTTH9: Chuẩn hóa họ tên
def standardize_name(name: str) -> str:
    return name.strip().title()


ten = "  nGuyEn vAn a   "
print("Tên chuẩn hóa:", standardize_name(ten))
