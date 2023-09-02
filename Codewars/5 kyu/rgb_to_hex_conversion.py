# 5 kyu
# RGB To Hex Conversion
# 
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# 
# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    return f'{hex(min(255, max(r, 0)))[2:].upper().zfill(2)}{hex(min(255, max(g, 0)))[2:].upper().zfill(2)}{hex(min(255, max(b, 0)))[2:].upper().zfill(2)}'



# Best Practices

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))