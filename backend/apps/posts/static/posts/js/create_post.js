
btnSave = document.querySelector('#btn-save')
btnNext = document.querySelector('#btn-next')
btnBack = document.querySelector('#btn-back')
btnPublish = document.querySelector('#btn-publish')

postMainContentElement = document.querySelector('#post-main-content')

postInfoElement = document.querySelector('#post-info')

btnNext.addEventListener('click', () => {

    if (quill_title.getText() == "\n") {
        alert("Please complete all required fields.")
        return
    }

    const quill_content = document.querySelector('#quill-id_content');
    const content_ql_editor = quill_content.querySelector('.ql-editor');

    const isEmpty = content_ql_editor.innerHTML.trim() === '<p><br></p>';

    if (isEmpty) {
        alert("Content is empty!")
        return
    }

    btnNext.classList.add('hidden')
    btnSave.classList.add('hidden')
    postMainContentElement.classList.add('hidden')


    btnBack.classList.remove('hidden')
    btnPublish.classList.remove('hidden')
    postInfoElement.classList.remove('hidden')

})

btnBack.addEventListener('click', () => {

    btnNext.classList.remove('hidden')
    btnSave.classList.remove('hidden')
    postMainContentElement.classList.remove('hidden')

    btnBack.classList.add('hidden')
    btnPublish.classList.add('hidden')
    postInfoElement.classList.add('hidden')

})

editorForm = document.querySelector('#ql-editor-form')
editorForm.addEventListener('submit', (event) => {

    event.preventDefault();

    const titleContent = Array.from(document.querySelectorAll('#editor-title .ql-editor p'))
        .map(p => p.innerText.trim())
        .join('\n');

    const descriptionContent = Array.from(document.querySelectorAll('#editor-description .ql-editor p'))
        .map(p => p.innerText.trim())
        .join('\n');

    console.log(titleContent)

    console.log(descriptionContent)

    document.querySelector('#id_description').value = descriptionContent;

    document.querySelector('#id_title').value = titleContent;

    editorForm.submit()

})