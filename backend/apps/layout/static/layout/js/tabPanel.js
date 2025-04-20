
document.addEventListener('DOMContentLoaded', function () {

	const tabs = document.querySelectorAll('.tab-item')

	const contents = document.querySelectorAll('.profile-tab-content')

	tabs.forEach((tab, index) => {

		tab.addEventListener('click', function (event) {

			event.preventDefault()

			tabs.forEach((t) => t.classList.remove('text-green-500', 'border-green-500', 'active', 'border-b-2'))

			contents.forEach((c) => c.classList.add('hidden'))

			this.classList.add('text-green-500', 'border-b-2', 'border-green-500', 'active')

			contents[index].classList.remove('hidden')

		})

	})

})