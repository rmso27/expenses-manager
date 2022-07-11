<script>

    // Check the status of connectivity with the BE
    fetch('http://127.0.0.1:5000/status').then((response) => {
        return response.json()
    }).then((result) => {
        console.table([result])
    }).catch(() => { // if no communication with the BE
        const result = {'server': 'FAILED', 'database': 'FAILED'}
        console.table([result])
    })

</script>