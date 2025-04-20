const conversationId = JSON.parse(document.getElementById('conversation-id').textContent);

const senderId = JSON.parse(document.getElementById('sender-id').textContent);

const receiverId = JSON.parse(document.getElementById('receiver-id').textContent);

const chatSocket = new WebSocket(
	'ws://'
	+ window.location.host
	+ '/ws/chat/'
	+ conversationId
	+ '/'
);

chatSocket.onmessage = function (e) {

	const data = JSON.parse(e.data);

	newmsg = ""

	if (data.sender_id == senderId) {

		newmsg = `
      <div class="flex items-start space-x-4 justify-end max-w-full">
      <div class="bg-green-500 text-white p-3 rounded-lg max-w-2/5">
      <p class="text-sm">${data.content}</p>
      </div>
      <img src="${data.avatar}" alt="User Avatar" class="h-8 w-8 rounded-full" />
      </div>`;

	}

	else {

		newmsg = `
      <div class="flex items-start space-x-4 max-w-2/5">
      <img src="${data.avatar}" alt="User Avatar" class="h-8 w-8 rounded-full" />
      <div class="bg-gray-400 text-white p-3 rounded-lg">
        <p class="text-sm">${data.content}</p>
      </div>
    </div>`

	}

	const messagesContainer = document.querySelector('[data-messages]');

	messagesContainer.insertAdjacentHTML('beforeend', newmsg)

	messagesContainer.scrollTop = messagesContainer.scrollHeight;

};

chatSocket.onclose = function (e) {

	console.error('Chat socket closed unexpectedly');

};

document.querySelector('#input-msg-content').focus();

document.querySelector('#input-msg-content').onkeyup = function (e) {

	if (e.key === 'Enter') {

		document.querySelector('#btn-send-msg').click();

	}

};

document.querySelector('#btn-send-msg').onclick = function (e) {

	e.preventDefault();

	const messageInputDom = document.querySelector('#input-msg-content');

	const content = messageInputDom.value;

	if (!content.trim()) return;

	chatSocket.send(JSON.stringify({
		'conversation_id': conversationId,
		'sender_id': senderId,
		'receiver_id': receiverId,
		'content': content
	}));

	messageInputDom.value = '';

};