const toolbarOptions = [
  [{ 'size': ['normal'] }],

];

const quill_title = new Quill('#editor-title', {
  modules: {
    toolbar: toolbarOptions
  },
  theme: 'bubble'
});
quill_title.root.setAttribute('spellcheck', false)

const quill_description = new Quill('#editor-description', {
  modules: {
    toolbar: toolbarOptions
  },
  theme: 'bubble'
});
quill_description.root.setAttribute('spellcheck', false)
