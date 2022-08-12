$(function() {
    $('a#calculate').bind('click', function() {
        $.post('projects/remove_collaborator', {
                current_project_id: $('input[name="current_project_id"]').val(),
                user_id: $('input[name="user_id"]').val()
            },
            function(data) {
                console.log(data.result);
            });
        returnfalse;
    });
});

document.querySelector(".collaborate") !== null ? console.log("yes") : console.log("no");


document.querySelector(".collaborate").addEventListener("click", () => {
    console.log("yes");
    document.querySelector(".collaborate-dropdown").classList.toggle("active")
})