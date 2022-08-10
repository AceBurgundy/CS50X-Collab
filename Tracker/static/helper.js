// use default only on one function or class
export function counter(inputId, counterId, restriction) {
    /* Add function to any character counter you add in javascript

        inputId: the id of the input
        counterId: the id of the number which should change depending on the count
        restriction: <integer> adds a limit
    */
    inputId.addEventListener('input', () => {
        if (restriction === null) {
            restriction = counterId.children[0].textContent = inputId.value.length
        } else if (inputId.value.length <= restriction) {
            counterId.children[0].textContent = inputId.value.length
        }
    })

    window.addEventListener("load", () => {
        counterId.children[0].textContent = inputId.value.length
    })
}

export function eyeToggle(eyesContainerId, inputId, eyeId, eyeSlashId) {
    /* Add function to open and close eye icons in forms 
    
    eyesContainerId: container where all your eye icons are placed
    inputId: the id of the input
    eyeId: the id of the eye icon (open)
    eyeSlashId: the id of the eye icon (close)
    
    */
    eyesContainerId.addEventListener("click", () => {
        if (inputId.type == "text") {
            inputId.setAttribute("type", "password")
            eyeId.style.display = "none"
            eyeSlashId.style.display = "block"
        } else {
            inputId.setAttribute("type", "text")
            eyeId.style.display = "block"
            eyeSlashId.style.display = "none"
        }
    })

}

export function makeToastNotification(Message) {
    let block = document.createElement('div');
    block.className = "error"
    block.innerHTML = Message

    if ($('.error-list') !== null) {
        $('.error-list').appendChild(block)

        document.querySelectorAll(".error").forEach((error) => {

            error.classList.toggle("active")

            setTimeout(() => {
                error.classList.remove("active")
            }, 3000);
        })
    }
}