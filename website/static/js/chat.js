// automatic scroll to bottom of the chat box div -------------

const messageList = document.getElementById('message-list-box');
function scrollToBottom() {
    messageList.scrollTop = messageList.scrollHeight;
}

// Scroll to the bottom when the page is loaded
window.onload = scrollToBottom;

// auto-focousing the input of chat --------------

window.addEventListener('DOMContentLoaded', (event) => {
    const inputBox = document.getElementById('chat-message-input');
    // Function to focus the input box
    const focusInput = () => {
        inputBox.focus();
    };

    // Event listeners to focus the input box
    window.addEventListener('click', focusInput);
});


// send message on enter key press: -------------
document.addEventListener('DOMContentLoaded', () => {
    const inputBox = document.getElementById('chat-message-input');
    const sendButton = document.getElementById('submit');
    const form = document.querySelector('form');

    // Function to handle keypress event
    const handleKeyPress = (event) => {
        // Check if Enter key is pressed
        if (event.key === 'Enter') {
            // Trigger a click event on the send button
            sendButton.click();

            
            // Prevent default form submission behavior
            event.preventDefault();

        }
    };

    // Attach keypress event listener to input field
    inputBox.addEventListener('keypress', handleKeyPress);

    // // Prevent form submission
    // form.addEventListener('submit', (event) => {
    //     event.preventDefault();
    // });
});
