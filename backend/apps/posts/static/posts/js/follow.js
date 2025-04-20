
// Follow button in post page

function attachFollowEvent() {

  const data = document.currentScript.dataset;

  document.getElementById("btn-follow").addEventListener("click", () => {

    console.log(data.user)

    console.log(data.profile)

    var xhr = new XMLHttpRequest();

    xhr.open("POST", data.url, true);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.setRequestHeader("X-CSRFToken", window.csrfToken);

    xhr.onreadystatechange = function () {

      if (xhr.readyState === 4 && xhr.status === 200) {

        console.log("Success:", JSON.parse(xhr.responseText));

        document.getElementById("btn-follow").classList.add("hidden");

        document.getElementById("btn-unfollow").classList.remove("hidden")

      }

      else {

        console.log("Error:", "Error when follow profile");

      }

    };

    xhr.send(JSON.stringify({

      "user_profile_id": data.user,

      "profile_id": data.profile

    }));

  })


  document.getElementById("btn-unfollow").addEventListener("click", () => {

    console.log(data.user)

    console.log(data.profile)

    var xhr = new XMLHttpRequest();

    xhr.open("POST", data.url, true);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.setRequestHeader("X-CSRFToken", data.token);

    xhr.onreadystatechange = function () {

      if (xhr.readyState === 4 && xhr.status === 200) {

        console.log("Success:", JSON.parse(xhr.responseText));

        document.getElementById("btn-unfollow").classList.add("hidden");

        document.getElementById("btn-follow").classList.remove("hidden")

      }

      else {

        console.log("Error:", "Error when unfollow profile");

      }

    };

    xhr.send(JSON.stringify({

      "user_profile_id": data.user,

      "profile_id": data.profile

    }));

  })

}

attachFollowEvent()

