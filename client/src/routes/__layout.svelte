<script>
    import Navbar from "../components/Navbar.svelte"
    import "../public/css/style.css"
</script>

<div class = "main">
    <div class = "main-wrapper">
        <slot></slot>
    </div>
    <div class = "footer">
        <Navbar/>
    </div>
</div>