<script>

    // Function to test connectivity with the BE
    async function testRoute() {
        const response = await fetch('http://127.0.0.1:5000/test')
        const result = await response.json()

        return result
    }

    // Function to display test result in the FE
    function displayResult(result) {
        document.getElementById("result").innerHTML = result['response']
    }

    // Call testRoute function
    testRoute().then(result => {
        displayResult(result)
    })

</script>

<p id = "result"></p>
