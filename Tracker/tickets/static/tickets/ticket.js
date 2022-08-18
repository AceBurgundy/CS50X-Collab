let ticket = document.querySelectorAll(".ticket");
let dropzone = document.querySelectorAll(".ticket-column-body");
let draggedTicket = null;

dropzone.forEach(thisZone => {
    thisZone.addEventListener("dragover", function(event) {
        event.preventDefault();
    })
    thisZone.addEventListener("dragenter", function() {
        console.log("Enter");
    })
    thisZone.addEventListener("dragleave", function() {
        console.log("Leave");
    })
    thisZone.addEventListener("drop", function() {
        this.appendChild(draggedTicket)
    })
});

ticket.forEach(thisTicket => {
    thisTicket.addEventListener("dragstart", function() {
        draggedTicket = this
    })
    thisTicket.addEventListener("dragend", function() {
        draggedTicket = null
    })
})

date = new Date()

document.querySelectorAll(".deadline-date").forEach(deadline => {
    deadlineYear = deadline.textContent.split('-')[0]
    deadlineMonth = deadline.textContent.split('-')[1]
    deadlineDay = deadline.textContent.split('-')[2]

    if (deadlineMonth - (date.getMonth() + 1) == 1) {
        deadline.parentElement.parentElement.style.backgroundColor = '#de65656f'
        deadline.parentElement.parentElement.style.color = '#300e0e'
        deadline.parentElement.parentElement.children[0].style.color = '#300e0e'
    } else if (deadlineMonth - (date.getMonth() + 1) == 2) {
        deadline.parentElement.style.backgroundColor = 'orange'
    } else {
        deadline.parentElement.parentElement.style.backgroundColor = '#82e5a073'
        deadline.parentElement.parentElement.style.color = '#164524'
        deadline.parentElement.parentElement.children[0].style.color = '#164524'
    }
})

document.addEventListener("DOMContentLoaded", () => {
    if ($('.title').text() == 'TICKET #') {
        $('.title').text('TICKET # ' + $('.ticket_id').val())

        $('.aside .nav-child:first-child').remove();
    }
})


window.onload = () => {
    document.querySelectorAll('.ticket-tag-container').forEach(ticket => {
        if (ticket.children[0].textContent == 'Pending') {
            ticket.style.backgroundColor = '#de65656f'
            ticket.children[0].color = '#300e0e'
        } else if (ticket.children[0].textContent == 'Medium') {
            ticket.style.backgroundColor = 'orange'
                // ticket.children[0]
        } else {
            ticket.style.backgroundColor = '#82e5a073'
            ticket.children[0]
        }
    })

    if (document.querySelector('.comment_author') !== null) {
        const author = document.querySelector('.comment_author')
        author.textContent = author.getAttribute("value")
    }

    if (document.querySelector('.author-comment-message') !== null) {
        document.querySelector('.author-comment-message').addEventListener("click", () => {
            document.querySelector('.add-comment-options-container').style.display = 'flex'
        })
    }

    if (document.querySelector('#cancel-comment') !== null) {
        document.querySelector('#cancel-comment').addEventListener("click", () => {
            document.querySelector('.add-comment-options-container').style.dsiplay = 'none'
        })
    }

    if (document.querySelector(".author-comment-message") !== null) {
        const formDescriptionTextArea = document.querySelector(".author-comment-message")
        formDescriptionTextArea.addEventListener("input", e => {

            formDescriptionTextArea.style.height = `${e.target.scrollHeight}px`
        })
    }

    if (document.querySelectorAll(".menu-icon") !== null) {
        const menuIcon = document.querySelectorAll(".menu-icon")

        menuIcon.forEach(menu => {
            menu.addEventListener("click", () => {
                menu.nextElementSibling.classList.toggle("active")
            })
        })
    }

    if (document.querySelector(".delete-comment") !== null) {
        $(".delete-comment").on("submit", function(e) {
            e.preventDefault()

            request = $.ajax({
                type: "POST",
                url: "/delete-comment",
                data: {
                    comment_id: comment_id
                },
                success: function(data) {
                    alert(data.success)
                },
                error: function(data) {
                    alert(data.failed)
                }
            });
        })
    }

    if (document.querySelector("#add-comment") !== null) {
        $(document).on('click', "#add-comment", function(e) {
            e.preventDefault()
            console.log($('.author-comment_message').text());
            request = $.ajax({
                type: "POST",
                url: "/add-comment",
                data: {
                    comment_message: $('.author-comment_message').val()
                },
                success: function(data) {
                    if (data.success) {
                        alert(data.success)
                    } else {
                        alert(data.failed)
                    }
                }
            });
        })
    }
}