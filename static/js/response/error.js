const Error = (CONF) => {
    CONF.root.style.setProperty("--input-width", "100%");
    // start the error animation
    CONF.inputField.classList.add("invalid");
    // end the error animation
    setTimeout(() => {
        CONF.inputField.classList.remove("invalid");
    }, 600)
}

export default Error;