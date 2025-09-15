def inicio():
    print("\n🚦 Bienvenido a *Rutas del Destino*")
    print("Estás en una intersección con tres rutas posibles.")
    print("1. Ruta costera (hacia el mar)")
    print("2. Ruta montañosa (hacia la cima)")
    print("3. Ruta urbana (hacia la ciudad)")
    eleccion = input("¿Qué ruta tomas? (1/2/3): ")

    if eleccion == "1":
        ruta_costera()
    elif eleccion == "2":
        ruta_montañosa()
    elif eleccion == "3":
        ruta_urbana()
    else:
        print("❌ Opción inválida.")
        inicio()

def ruta_costera():
    print("\n🌊 La brisa del mar te acompaña mientras conduces.")
    print("Encuentras un muelle con dos opciones:")
    print("1. Subirte a un bote pesquero")
    print("2. Caminar por la playa")
    eleccion = input("¿Qué haces? (1/2): ")

    if eleccion == "1":
        print("\n🚤 El bote te lleva a una isla escondida con una comunidad autosuficiente. 🏝️ Final pacífico.")
    elif eleccion == "2":
        print("\n🦀 Tropiezas con una cueva secreta donde descubres un mapa antiguo. 🗺️ Final aventurero.")
    else:
        print("❌ Opción inválida.")
        ruta_costera()

def ruta_montañosa():
    print("\n⛰️ El camino se vuelve empinado y solitario.")
    print("Encuentras una bifurcación:")
    print("1. Tomar el sendero estrecho")
    print("2. Seguir por la carretera principal")
    eleccion = input("¿Qué haces? (1/2): ")

    if eleccion == "1":
        print("\n🧗 Llegas a un mirador donde ves todo el valle. Te sientes libre. 🌄 Final contemplativo.")
    elif eleccion == "2":
        print("\n🚧 Una tormenta bloquea el paso y debes regresar. 💨 Final frustrante.")
    else:
        print("❌ Opción inválida.")
        ruta_montañosa()

def ruta_urbana():
    print("\n🏙️ La ciudad bulle de actividad. Te detienes en una esquina con dos caminos:")
    print("1. Entrar a una galería de arte")
    print("2. Seguir a un grupo de manifestantes")
    eleccion = input("¿Qué haces? (1/2): ")

    if eleccion == "1":
        print("\n🎨 Descubres tu pasión por el arte y decides quedarte como curador. 🖼️ Final creativo.")
    elif eleccion == "2":
        print("\n📢 Te unes a una causa social y lideras un cambio en tu comunidad. ✊ Final transformador.")
    else:
        print("❌ Opción inválida.")
        ruta_urbana()

inicio()
