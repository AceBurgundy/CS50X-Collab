window.addEventListener("load", () => {
    document.querySelectorAll(".message").forEach((message) => {

        message.textContent == '' ? message.remove() : message.classList.toggle("active")

        setTimeout(() => {
            message.classList.toggle("active")
        }, 2000);
    })
})

window.addEventListener("load", () => {

    document.querySelectorAll(".error").forEach((error) => {

        error.innerHTML = error.textContent.toString().replace("_", " ")
        error.classList.toggle("active")

        setTimeout(() => {
            error.classList.remove("active")
        }, 3000);
    })
})