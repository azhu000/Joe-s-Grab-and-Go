function handleButtonClick() {
    const submitButton = document.getElementsByClassName('btn-bid-submit');
    const inputElement = document.getElementsByClassName('input-field');
    submitButton[0].disabled = "true";
    inputElement[0].disabled = "true";
}