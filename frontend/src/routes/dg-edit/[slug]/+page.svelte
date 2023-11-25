<script>
    import {Label} from "flowbite-svelte";
    import Table from "$lib/components/Table.svelte";

    export let data;
    let slug = data.slug;
</script>

<Label>
    <span>Biopsy ID:</span>
    {slug}
</Label>

<Table />

<style>
    span {
        font-weight: bold;
    }
</style>