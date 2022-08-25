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

export const makeToastNotification = function(Message) {
    let list = document.createElement('li');
    list.className = "message"
    list.innerHTML = Message

    if ($('.flashes') !== null) {
        $('.flashes').append(list)

        document.querySelectorAll(".message").forEach(toast => {

            toast.classList.toggle("active")

            setTimeout(() => {
                toast.classList.remove("active")
                setTimeout(() => {
                    document.querySelector('.flashes').removeChild(toast)
                }, 500)
            }, 2000);

        })
    }
}

export const togglePopper = function(popperInstance, button) {

    function show() {
        tooltip.setAttribute('data-show', '');

        // We need to tell Popper to update the tooltip position
        // after we show the tooltip, otherwise it will be incorrect
        popperInstance.update();
    }

    function hide() {
        tooltip.removeAttribute('data-show');
    }

    const showEvents = ['mouseenter', 'focus'];
    const hideEvents = ['mouseleave', 'blur'];

    showEvents.forEach((event) => {
        button.addEventListener(event, show);
    });

    hideEvents.forEach((event) => {
        button.addEventListener(event, hide);
    });
}

export const autoResize = function() {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
}

export const checkDate = function(classNames) {
    const months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    let date = new Date()

    // deadline must be formated in a YYYY-MM-DD format and each of them are inside an element with className = 'deadline-date'
    document.querySelectorAll(classNames).forEach(deadline => {
            let deadlineMonth = deadline.textContent.split('-')[1]

            if (deadlineMonth - (date.getMonth() + 1) == 1) {
                deadline.parentElement.parentElement.style.backgroundColor = '#de65656f'
                deadline.parentElement.parentElement.style.color = '#300e0e'
                deadline.parentElement.parentElement.children[0].style.color = '#300e0e'
            } else if (deadlineMonth - (date.getMonth() + 1) == 2) {
                deadline.parentElement.parentElement.style.backgroundColor = 'orange'
            } else {
                deadline.parentElement.parentElement.style.backgroundColor = '#82e5a073'
                deadline.parentElement.parentElement.style.color = '#164524'
                deadline.parentElement.parentElement.children[0].style.color = '#164524'
            }
        })
        // not working yet
}