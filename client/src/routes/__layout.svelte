<script>
    import Navbar from "../components/Navbar.svelte"
    import "../public/css/main.css"
    import "../public/css/Navbar.css"
    import "../public/css/Login.css"
</script>

<div class = "main">
    <Navbar/>
    <div class="main-container">
        <slot></slot>
    </div>
</div>