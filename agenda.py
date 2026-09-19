contactos = {}

def añadir():
    nombre = input("Nombre: ")
    if nombre in contactos:
        print(f"⚠️ {nombre} ya existe")
        return
    telefono = input("Teléfono: ")
    contactos[nombre] = telefono
    print(f"✅ {nombre} añadido")
    
def buscar():
    nombre = input("¿A quien buscas? ")
    if nombre in contactos:
        print(f"📞 {nombre}: {contactos[nombre]}")
    else:
        print(f"❌ No encontré a {nombre}")
        
def ver_todos():
    if not contactos:
        print("📭 La agenda está vacía")
        return
    for nombre, telefono in contactos.items():
        print(f"📞 {nombre}: {telefono}")

def eliminar():
    nombre = input("¿A quién quieres eliminar? ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"🗑️ {nombre} eliminado")
    else:
        print(f"❌ No encontré a {nombre}")
        
def editar():
    nombre = input("¿A quién quieres editar? ")
    if nombre in contactos:
        nuevo = input(f"Nuevo teléfono para {nombre}: ")
        contactos[nombre] = nuevo
        print(f"✏️ {nombre} actualizado")
    else:
        print(f"❌ No encontré a {nombre}")
        
    
while True:
    print("\n=== MI AGENDA ===")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Ver todos")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        añadir()
    elif opcion == "2":
        buscar()
    elif opcion == "3":
        ver_todos()
    elif opcion == "4":
        editar()
    elif opcion == "5":
        eliminar()
    elif opcion == "6":
        print("¡Hasta luego! 👋")
        break
        
    
    else:
        print("❌ Opción no válida")