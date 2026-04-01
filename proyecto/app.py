import json

#CARGAR USUARIOS (SEGURO)
#si el JSON está vacío o da error → el programa muere

#lo arreglamos así:
try:
    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)
except:
    usuarios = {}

while True:
    print("\n1. Login")
    print("2. Registro")
    print("3. Salir")
    
    opcion = input("Elige: ")
    
    if opcion == "1":
        user = input("Usuario: ")
        password = input("Contraseña: ")
        
        if user in usuarios:
            if usuarios[user] == password:
                print(" ✅ Login correcto")
            else:
                print("❌ Contraseña incorrecta")
        else:
            print("❌ Usuario no existe")    
            
    
    elif opcion == "2":
        user = input("Nuevo Usuario: ")
        password = input("Nueva contraseña: ")
        
        if user in usuarios:
            print("⚠️ Ya existe")
        else:
            password = input("Nueva contraseña: ")
            usuarios[user] = password
            
            with open("usuarios.json","w") as f:
                json.dump(usuarios, f)
    
    
    elif opcion == "3":
        print("Cerrar")
        break
