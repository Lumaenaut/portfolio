function toUpper() {
    const textarea = document.getElementById("text-area");
    textarea.value = textarea.value.toUpperCase();
}

function toLower() {
    const textarea = document.getElementById("text-area");
    textarea.value = textarea.value.toLowerCase();
}

function toProper() {
    const textarea = document.getElementById("text-area");
    textarea.value = textarea.value.toLowerCase().split(" ")
        .map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(" ")
}

function toSentence() {
    const textarea = document.getElementById("text-area");
    textarea.value = textarea.value.toLowerCase().replace(/(^\s*\w|[.!?]\s*\w)/g, c => c.toUpperCase());
}

function download(filename, text) {
    let element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

download("hello.txt", "This is the content of my file :)")