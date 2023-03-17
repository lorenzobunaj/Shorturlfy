import Success from "./response/success.js";
import Error from "./response/error.js";

// manage the user interaction
const App = (CONF) => {
    if (CONF.inputButton.innerText === "SHORT") {
        Add(CONF);
    } else if (CONF.inputButton.innerText === "COPY") {
        navigator.clipboard.writeText(`short.urlfy.org/get?r=${CONF.inputField.value}`);
    }
}
// add function
const Add = (CONF) => {
    // fetch the add api
    fetch('/add', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "url" : CONF.inputField.value }) // take the url
    })
    .then(response => response.json())
    .then(response => {
        AddResponse(CONF, response["status"]); // send the response by server
    })
}
const AddResponse = (CONF, status) => {
    if ([0, 2, 3].includes(status)) { // status = error-status --> display error
        Error(CONF); 
    } else {
        Success(CONF, status); // status = refer --> display the refer
    }
}

export default App;