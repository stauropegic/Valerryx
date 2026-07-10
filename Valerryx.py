import os, sys
import pymem
import pymem.process
process_name = "ac_client.exe"
base_address = 0x400000
local_entity_pointer_offset = 0x17E0A8

# Offsets -----------------------------------
offset_health = 0xEC
offset_current_ammo = 0x140
offset_magazine_ammo = 0x11C

# Colors -----------------------------------
rs = "\033[90m"
w = "\033[37m" 
gy = "\033[0m" 
def banner():
    print(rf"""{rs}
                     .
                    / V\
                  /{gy} `{rs}  /
                 <<   |
                 /    |
               /      |
             /        |
           /    \  \ /
          (      ) | |     
  ________|   _/_  | |            {gy}> Made by Rest{rs}
<__________\______)\__)      {gy}Valerryx - AC Game Trainer{rs}
""")
def exit():
    sys.exit(0)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def title(title):
    if os.name == "nt":
        os.system(f"title {title}")
    else:
        print(f"\33]0;{title}\a", end="", flush=True)
def get_local_entity_address(pm):
    module = pymem.process.module_from_name(pm.process_handle, process_name)
    base = module.lpBaseOfDll
    local_entity_addr = pm.read_int(base + local_entity_pointer_offset)
    return local_entity_addr
def change_value(pm, local_entity_addr, offset, value, value_type):
    if value_type == 'int':
        pm.write_int(local_entity_addr + offset, value)
        print(f"Value at offset {hex(offset)} set to: {value}")
    elif value_type == 'float':
        pm.write_float(local_entity_addr + offset, value)
        print(f"Value at offset {hex(offset)} set to: {value}")
def main():
    title("Valerryx * AC Game Trainer")
    try:
        pm = pymem.Pymem(process_name)
        local_entity_addr = get_local_entity_address(pm)
        while True:
            clear()
            banner()
            print(fr"{rs}[{gy}")
            print(f"    {gy}1{rs}: {gy}Health")
            print(f"    {gy}2{rs}: {gy}Current Ammo")
            print(f"    {gy}3{rs}: {gy}Magazine Ammo")
            print(f"    {gy}4{rs}: {gy}Exit")
            print(f"{rs}]{gy}")
            choice = input(f"\n{rs}root{gy}@{rs}valerryx{gy}:~#")
            if choice == '1':
                new_value = int(input("Enter new health value: "))
                change_value(pm, local_entity_addr, offset_health, new_value, 'int')  
            elif choice == '2':
                new_value = int(input("Enter new current ammo value: "))
                change_value(pm, local_entity_addr, offset_current_ammo, new_value, 'int')  
            elif choice == '3':
                    new_value = int(input("Enter new magazine ammo value: "))
                    change_value(pm, local_entity_addr, offset_magazine_ammo, new_value, 'int') 
            elif choice == '4':
                exit()
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...") 
    except pymem.exception.MemoryReadError as e:
        print(f"Memory read error: {e}")
    except pymem.exception.MemoryWriteError as e:
        print(f"Memory write error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()
