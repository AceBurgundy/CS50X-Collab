import { counter } from "/static/helper.js"

// script to show and hide modal to add new form
const formModal = document.querySelector(".form-modal-container")
const modalXButton = document.querySelector(".modal-x-button")
const modalCancelButton = document.querySelector(".modal-close-button")
const background = document.getElementById('background')

window.addEventListener("DOMContentLoaded", () => {
    if ((document.querySelector(".error")) === null) {
        background.classList.toggle("active")
        formModal.classList.toggle("active")
    } else {
        formModal.style.transform = "translate(-50%, -50%)"
        background.style.transition = "-10ms"
        background.style.height = "100vh"
        formModal.style.transition = "-10ms"
    }
})

modalXButton.addEventListener("click", () => {
    background.style.height = "80vh"
    formModal.style.opacity = "0"
    formModal.style.transform = "translate(-50%, -40%)"
    setTimeout(() => {
        window.history.back()
    }, 300)
})

modalCancelButton.addEventListener("click", () => {
    background.style.height = "80vh"
    formModal.style.opacity = "0"
    formModal.style.transform = "translate(-50%, -40%)"
    setTimeout(() => {
        window.history.back()
    }, 300)
})

if (document.getElementById('ticket-modal-cancel-button') !== null) {
    document.getElementById('ticket-modal-cancel-button').addEventListener("click", () => {
        background.style.height = "80vh"
        formModal.style.opacity = "0"
        formModal.style.transform = "translate(-50%, -40%)"
        setTimeout(() => {
            window.location = "/show-tickets/" + document.getElementById('project_id').value
        }, 300)
    })
}

if (document.getElementById('ticket-modal-x-button') !== null) {
    document.getElementById('ticket-modal-x-button').addEventListener("click", () => {
        background.style.height = "80vh"
        formModal.style.opacity = "0"
        formModal.style.transform = "translate(-50%, -40%)"
        setTimeout(() => {
            window.location = "/show-tickets/" + document.getElementById('project_id').value
        }, 300)
    })
}
counter(
    document.getElementById("form-title"),
    document.getElementById("counter-for-title"),
    200
)

counter(
    document.getElementById("form-description"),
    document.getElementById("counter-for-description"),
    200
)

const formDescriptionTextArea = document.querySelector(".form-description")

formDescriptionTextArea.addEventListener("input", e => {
    formDescriptionTextArea.style.height = `${e.target.scrollHeight}px`
})

$('proceed-button').bind('submit', function(e) {
    e.preventDefault()
})

window.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector(".ticket-status") !== null) {
        document.querySelector(".ticket-status").value = window.location.search !== null ? window.location.search.substring(1).split('=')[1].replace("+", " ") : 'Pending'
        document.querySelector(".ticket-status").setAttribute("value", window.location.search !== null ? window.location.search.substring(1).split('=')[1].replace("+", " ") : 'Pending')
    }

    if (document.querySelector(".collaborate") !== null) {

        document.querySelector(".collaborate-toggle").addEventListener("click", () => {

            document.querySelector(".collaborate-dropdown").classList.toggle("active")
        })
    }
    let collaboratorSelectOption = document.querySelectorAll('.user')

    if (document.querySelector(".current-page-title").value == 'ticket-modal') {

        let chose = ""

        collaboratorSelectOption.forEach(option => {

            option.addEventListener("click", () => {
                let clickedUser = option.children[0].getAttribute('value').trim()

                if ($('#assign').attr('value') == "author") {
                    chose = clickedUser
                    $('#assign').attr('value', chose)
                    option.classList.add("active")
                } else if (clickedUser != chose) {
                    document.getElementById(chose).parentElement.parentElement.classList.remove("active")
                    chose = clickedUser
                    $('#assign').attr('value', chose)
                    option.classList.add("active")
                } else {
                    $('#assign').attr('value', "author")
                    option.classList.remove("active")
                }
            })
        })
    } else {
        let user = []

        collaboratorSelectOption.forEach(option => {

            option.addEventListener("click", () => {
                if (user.indexOf(option.outerText) < 0) {
                    user.push(option.children[0].getAttribute('value').trim())
                    option.classList.add("active")
                } else {
                    option.classList.remove("active")
                    user.splice(user.indexOf(option.outerText), 1)
                }

                $('#collaborate-data').attr('value', user)
            })
        })
    }
})