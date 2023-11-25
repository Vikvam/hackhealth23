<script>
    import {onMount} from "svelte";
    import {Label} from "flowbite-svelte";
    import Table from "$lib/components/Table.svelte";

    export let data;
    let slug = data.slug;

    let dgData;

    async function fetchData() {
        const response = await fetch("http://localhost:8000/dg/" + slug);
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    function renderTable() {

    }

    onMount(async () => {
        // dgData = await fetchData();
        // console.log("DGData", dgData)
    })
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