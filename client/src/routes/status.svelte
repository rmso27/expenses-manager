<script>

    // Check the status of connectivity with the BE
    fetch('http://127.0.0.1:5000/status').then((response) => {
        return response.json()
    }).then((result) => {
        displayResult(result)
    }).catch(() => { // f no communication with the BE
        const result = {'server': 'FAILED', 'database': 'FAILED'}
        displayResult(result)
    })

    // Function to display the status results in the FE
    function displayResult(result) {
        document.getElementById("server").innerHTML = result['server']
        document.getElementById("database").innerHTML = result['database']
    }

</script>

<div class = "status-table">
    <div class = "status-table-wrapper">
        <div class = "core-status">
            <div class = "core-status-header">
                <h2>Core</h2>
            </div>
            <div class = "core-status-item">
                Server: <span id = "server"></span>
            </div>
            <div class = "core-status-item">
                Database: <span id = "database"></span>
            </div>
        </div>
    </div>
</div>