function toggleCode() {
    const codeBlock = document.getElementById('codeBlock');
    codeBlock.classList.toggle('expanded');
}

document.getElementById('dynamicButton').addEventListener('click', function() {
    alert('祝你生日快乐！🎂');
});
