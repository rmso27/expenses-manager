<script>

    // Function to check the status of connectivity with the BE
    async function checkStatus() {
        const response = await fetch('http://127.0.0.1:5000/status')
        const result = await response.json()

        return result
    }

    // Function to display the status results in the FE
    function displayResult(result) {
        document.getElementById("server").innerHTML = result['server']
        document.getElementById("database").innerHTML = result['database']
    }

    // Call checkStatus function
    checkStatus().then(result => {
        displayResult(result)
    })

</script>

Server: <span id = "server"></span> <br />
Database: <span id = "database"></span>
