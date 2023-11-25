<script>
    import Navigation from "$lib/Navigation.svelte";
    import TailwindCSS from "$lib/TailwindCSS.svelte";
</script>


<Navigation/>

<div>
    <slot />
</div>


<style>
    div {
        display: grid;
        place-items: center;
        padding: 4rem;
    }
</style>