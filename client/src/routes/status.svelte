<script>

    // Check the status of connectivity with the BE
    fetch('http://127.0.0.1:5000/status').then(response => {
        return response.json()
    }).then(result => {displayResult(result)})

    // Function to display the status results in the FE
    function displayResult(result) {
        document.getElementById("server").innerHTML = result['server']
        document.getElementById("database").innerHTML = result['database']
    }

</script>

Server: <span id = "server"></span> <br />
Database: <span id = "database"></span>