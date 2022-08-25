document.addEventListener("DOMContentLoaded", () => {
    if ($('.title').text() == 'TICKET #') {
        $('.title').text('TICKET # ' + $('.ticket_id').val())

        $('.aside .nav-child:first-child').remove();
    }
})

document.querySelectorAll('.ticket-tag-container').forEach(ticket => {
    if (ticket.children[0].textContent == 'Pending') {
        ticket.style.backgroundColor = '#de65656f'
        ticket.children[0].color = '#300e0e'
    } else if (ticket.children[0].textContent == 'Medium') {
        ticket.style.backgroundColor = 'orange'
    } else {
        ticket.style.backgroundColor = '#82e5a073'
        ticket.children[0]
    }
})

const commentBox = document.querySelector('.author-comment-message')
const commentBoxOptions = document.querySelector('.add-comment-options-container')

commentBox.addEventListener("click", () => {
    commentBoxOptions.style.display = 'flex'
})

document.querySelector('.cancel-comment').addEventListener("click", (e) => {
    e.preventDefault()
    commentBoxOptions.style.display = 'none'
})

document.querySelectorAll('.comment').forEach(comment => {
    comment.classList.add("hoverable")
})

document.querySelectorAll('.edit-comment').forEach(editButton => {
    editButton.addEventListener("click", () => {
        editButton.parentElement.parentElement.parentElement.classList.remove("hoverable")
        editButton.parentElement.parentElement.previousElementSibling.children[1].firstElementChild.children[1].children[1].style.display = 'flex'
        editButton.parentElement.parentElement.previousElementSibling.children[1].firstElementChild.firstElementChild.classList.add("active")
    })
})

document.querySelectorAll('.cancel-comment-edit').forEach(cancelButton => {
    cancelButton.addEventListener("click", () => {
        cancelButton.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.classList.add("hoverable")
        cancelButton.parentElement.style.display = 'none'
        cancelButton.parentElement.parentElement.previousElementSibling.classList.remove("active")
    })
})

commentBox.addEventListener('input', autoResize, false);

document.querySelectorAll('.menu-icon').forEach(commentOption => {
    commentOption.addEventListener("mouseover", () => {
        commentOption.nextElementSibling.classList.toggle("active")
    })
})

$(document).ready(function() {

    $('.comment-section').on('scroll', function() {
        if ($(this).scrollTop() + $(this).innerHeight() > $(this).innerHeight() + 50) {
            $('.scroll-top').addClass("active")
        } else {
            $('.scroll-top').removeClass("active")
        }
    })

    $(document).on("click", ".delete-comment", function(e) {
        e.preventDefault()
        let comment_id = $(this).attr('comment-id');
        let request = $.post("/delete-comment", {
            comment_id: comment_id
        });

        request.done(function(data) {
            makeToastNotification(data.success)
            $(`#comment${comment_id}`).remove()
        })
        request.fail(function(data) {
            makeToastNotification(data.failed)
        })
    })

    $(".add-comment").on('click', function(e) {
        e.preventDefault()
        let comment = $('.author-comment-message').val()
        let ticket_id = $('.ticket_id').val()
        let request = $.post(
            "/add-comment", {
                comment: comment,
                ticket_id: ticket_id
            }, "html")
        request.done(function(data) {
            $(data).insertAfter($('#add-comment-container'));
            $('.author-comment-message').val("")
        })
        request.fail(function() {
            makeToastNotification("Failed to add comment")
        })
    })
})