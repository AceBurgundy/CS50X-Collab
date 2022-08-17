document.querySelector("#collaborate").addEventListener("click", () => {
    document.querySelector(".collaborate-dropdown").classList.toggle("active")
})
date = new Date()

// deadline must be formated in a YYYY-MM-DD format and each of them are inside an element with className = 'deadline-date'
document.querySelectorAll(".deadline-date").forEach(deadline => {
    deadlineYear = deadline.textContent.split('-')[0]
    deadlineMonth = deadline.textContent.split('-')[1]
    deadlineDay = deadline.textContent.split('-')[2]

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