
const script = document.getElementById('vote-script');

data = script.dataset

document.getElementById('upvote').addEventListener('click', () => {

    fetch(data.url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": window.csrfToken
        },
        body: JSON.stringify({ vote: 1 })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            upvote_element = document.getElementById('upvote')
            downvote_element = document.getElementById('downvote')

            if (data.vote_choice == 0) {
                upvote_element.classList.remove("bg-green-400", "text-white", "border-none")
            }
            else {
                upvote_element.classList.add("bg-green-400", "text-white", "border-none")
                downvote_element.classList.remove("bg-red-400", "text-white", "border-none")
            }
            document.getElementById('votes-count').innerHTML = data.votes
        })
        .catch(function (error) {
            console.log('Error: ', error)
        });
})

document.getElementById('downvote').addEventListener('click', () => {

    fetch(data.url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({ vote: -1 })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            downvote_element = document.getElementById('downvote')
            upvote_element = document.getElementById('upvote')

            if (data.vote_choice == 0) {
                downvote_element.classList.remove("bg-red-400", "text-white", "border-none")
            }
            else {
                upvote_element.classList.remove("bg-green-400", "text-white", "border-none")
                downvote_element.classList.add("bg-red-400", "text-white", "border-none")
            }
            document.getElementById('votes-count').innerHTML = data.votes
        })
        .catch(function (error) {
            console.log('Error: ', error)
        });
})