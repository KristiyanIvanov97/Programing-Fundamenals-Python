import re
number_of_barcodes = int(input())
pattern = r"@#+[A-Z][A-Za-z\d]{4,}[A-Z]@#+"
for _ in range(number_of_barcodes):
    barcode = input()
    match = re.fullmatch(pattern, barcode)
    if match:
        new_pattern = r"\d"
        product_group = ''.join(re.findall(new_pattern, barcode))
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
