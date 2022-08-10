import { counter, makeToastNotification } from "/static/helper.js"

// script to show and hide modal to add new form
const formModal = document.querySelector(".form-modal-container");
const modalXButton = document.querySelector(".modal-x-button");
const modalCancelButton = document.querySelector(".modal-close-button");
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
        window.location = "/";
    }, 300);
})

modalCancelButton.addEventListener("click", () => {
    background.style.height = "80vh"
    formModal.style.opacity = "0"
    formModal.style.transform = "translate(-50%, -40%)"
    setTimeout(() => {
        window.location = "/";
    }, 300);
})

if (document.getElementById('ticket-modal-cancel-button') !== null) {
    document.getElementById('ticket-modal-cancel-button').addEventListener("click", () => {
        background.style.height = "80vh"
        formModal.style.opacity = "0"
        formModal.style.transform = "translate(-50%, -40%)"
        setTimeout(() => {
            window.location = "/show-tickets/" + document.getElementById('project_id').value;
        }, 300);
    })
}

if (document.getElementById('ticket-modal-x-button') !== null) {
    document.getElementById('ticket-modal-x-button').addEventListener("click", () => {
        background.style.height = "80vh"
        formModal.style.opacity = "0"
        formModal.style.transform = "translate(-50%, -40%)"
        setTimeout(() => {
            window.location = "/show-tickets/" + document.getElementById('project_id').value;
        }, 300);
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

const formDescriptionTextArea = document.querySelector(".form-description");

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

        if (document.querySelector(".dropdown-toggle") !== null) {

            const userDropdownSwitch = document.querySelector(".dropdown-toggle")

            const collaborateDropdown = document.querySelector("#collaborate-dropdown")

            userDropdownSwitch.addEventListener("click", () => {

                collaborateDropdown.classList.toggle("active")
            })
        }
        let collaboratorSelectOption = document.querySelectorAll('.user')

        collaboratorSelectOption.forEach(option => {
            option.textContent = option.textContent.slice(6, -3);
            option.setAttribute("value", option.textContent)
        })

        $('#select-collaborators').change(function() {
            $('#collaborate-data').val($('#collaborate-dropdown').val())
        })
    })
    //     if ($('selectpicker') !== null) {
    //         $('select').selectpicker();

//         $('.filter-option-inner-inner').click(function() {
//             $('.open').toggleClass("active")
//             $('.bs-searchbox').toggleClass("active")
//         })

//         let collaboratorSelectOption = document.querySelectorAll('.user')

//         collaboratorSelectOption.forEach(option => {
//             option.textContent = option.textContent.slice(6, -3);
//             option.setAttribute("value", option.textContent)
//         })

//         $('#select-collaborators').change(function() {
//             $('#collaborators-data').val($('#select-collaborators').val())
//         })

//         $('proceed-button').bind('submit', function(e) {

//             if ($('#select-collaborators') == ' ') {
//                 $('#collaborators-data').val('author')
//             }
//         })
//     }
// })