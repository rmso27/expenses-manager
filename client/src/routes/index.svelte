<script>

    async function testRoute() {
        const response = await fetch('http://127.0.0.1:5000/test')
        const result = await response.json()

        console.log(result)
    }

    testRoute()

</script>
