import { checkDate, togglePopper } from "/static/helper.js"

if (document.querySelector(".collaborate") !== null) {
    let collaborateButton = document.querySelectorAll(".collaborate")

    collaborateButton.forEach(button => {
        button.addEventListener("click", () => {
            button.nextElementSibling.classList.toggle("active")
        })
    })
}

if (document.querySelector('#leave-project-button') !== null) {
    const leaveProjectButton = document.querySelector('#leave-project-button')
    const leaveProjectButtonTooltip = leaveProjectButton.nextElementSibling

    const popperInstance = Popper.createPopper(leaveProjectButton, leaveProjectButtonTooltip, {
        placement: 'left',
        modifiers: [{
            name: 'offset',
            options: {
                offset: [0, 8],
            },
        }, ],
    })
    togglePopper(popperInstance, leaveProjectButton)
}

checkDate('.deadline-date')