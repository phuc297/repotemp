
document.addEventListener('DOMContentLoaded', function () {

    const stickyBar = document.getElementById('sticky-bar')

    const triggerElement = document.querySelector('article')

    const footerOffset = 200

    function toggleStickyBar() {

        const triggerTop = triggerElement.getBoundingClientRect().top

        const triggerBottom = triggerElement.getBoundingClientRect().bottom

        const scrollBottom = window.innerHeight + window.scrollY

        const documentHeight = document.body.offsetHeight

        const shouldShow = triggerTop < window.innerHeight * 0.425 && triggerBottom > 50

        const shouldHide = scrollBottom + footerOffset >= documentHeight

        if (shouldShow && !shouldHide) {

            stickyBar.classList.remove('opacity-0', 'pointer-events-none')

        } else {

            stickyBar.classList.add('opacity-0', 'pointer-events-none')

        }

    }

    window.addEventListener('scroll', toggleStickyBar)

    toggleStickyBar()
    

    const form = document.getElementById("ql-editor-form");

    // Ngăn submit khi nhấn Enter trong form (trừ khi là textarea)
    form.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.target.tagName !== "TEXTAREA") {
        e.preventDefault();
      }
    });

    // Ngăn reload trang khi paste
    form.addEventListener("paste", function (e) {
      // Nếu đang paste vào phần tử không liên quan, thì ngăn mặc định
      if (!e.target.closest(".ql-editor")) {
        e.preventDefault();
      }
    });

})
