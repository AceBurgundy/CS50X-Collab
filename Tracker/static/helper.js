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

export const checkDate = function(classNames) {
    let date = new Date()

    // deadline must be formated in a YYYY-MM-DD format and each of them are inside an element with className = 'deadline-date'
    document.querySelectorAll(classNames).forEach(deadline => {
        const deadlineYear = deadline.textContent.split('-')[0]
        const deadlineMonth = deadline.textContent.split('-')[1]
        const deadlineDay = deadline.textContent.split('-')[2]

        if (deadlineMonth - (date.getMonth() + 1) == 1) {
            deadline.parentElement.style.backgroundColor = '#de65656f'
            deadline.parentElement.style.color = '#300e0e'
            deadline.parentElement.children[0].style.color = '#300e0e'
        } else if (deadlineMonth - (date.getMonth() + 1) == 2) {
            deadline.parentElement.style.backgroundColor = 'orange'
        } else {
            deadline.parentElement.style.backgroundColor = '#82e5a073'
            deadline.parentElement.style.color = '#164524'
            deadline.parentElement.children[0].style.color = '#164524'
        }
    })
}