
document.getElementById('btn-submit-comment').addEventListener('click', async () => {

    const commentContent = document.getElementById('text-comment').value

    if (!commentContent.trim()) {

        alert("Comment content cannot be empty!");

        return;

    }

    const script = document.getElementById('comment-script');

    const data = script.dataset;

    try {

        const response = await fetch(data.url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": window.csrfToken
            },
            body: JSON.stringify({
                post_id: data.post_id,
                profile_id: data.profile_id,
                content: commentContent
            })
        });

        const result = await response.json()

        if (result.success) {

            const newComment = `
                    <div class="flex mb-6">
                      <img class="w-14 h-14 rounded-full mr-4" src="${result.avatar}" alt="Avatar of User"/>
                      <div class="flex-1">
                        <p class="text-green-600 font-normal">${result.username}</p>
                        <p class="text-gray-600 text-sm mb-2">Posted on ${result.created_at}</p>
                        <p class="text-gray-800">${result.content}</p>
                      </div>
                    </div>
                    `;

            document.getElementById('comments-section').insertAdjacentHTML('afterbegin', newComment)

            document.getElementById('text-comment').value = ""

        } else {

            console.error("Error: ", result.error)

        }


    } catch (error) {

        console.error("Fetch error: ", error);

        alert("An error occurred when submitting the comment.")

    }

})

