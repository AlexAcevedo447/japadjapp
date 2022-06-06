var switcher = document.getElementById("paragraph")

const cambiar = () => {
    if (switcher.value == "Usuario y contraseña correctos") {
        p.classList.toggle("verde")
    } else if (switcher.value == "Usuario y contraseña incorrectos") {
        p.classList.toggle("rojo")
    } else {
        
    }
}

cambiar()