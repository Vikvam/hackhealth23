<script>
    import {onMount} from "svelte";
    import {Label} from "flowbite-svelte";
    import {CheckboxFormatter} from "slickgrid";
    import Table from "$lib/components/Table.svelte";

    export let data;
    let slug = data.slug;

    let mounted = false;

    let columns = [];
    let rows = [];

    async function fetchData() {
        const response = await fetch("http://localhost:8000/dg/" + slug);
        if (response.status > 400) {
            console.log("ERR"); // TODO
            return;
        }
        return response.json();
    }

    onMount(async () => {
        // const columns = {
        // TODO
        // }
        // const rows = await fetchData();
        columns = [
        {id: "title", name: "Title", field: "title"},
        {id: "duration", name: "Duration", field: "duration"},
        {id: "%", name: "% Complete", field: "percentComplete", width: 90},
        {id: "start", name: "Start", field: "start"},
        {id: "finish", name: "Finish", field: "finish"},
        {id: "effort-driven", name: "Effort Driven", field: "effortDriven", formatter: CheckboxFormatter}
    ];
        rows = [];
        for (let i = 0; i < 50; i++) {
        rows[i] = {
            id: i,
            title: "Task " + i,
            duration: "5 days",
            percentComplete: Math.round(Math.random() * 100),
            start: "01/01/2009",
            finish: "01/05/2009",
            effortDriven: (i % 5 == 0)
        };
    }
        mounted = true;
    })
</script>

<Label>
    <span>Biopsy ID:</span>
    {slug}
</Label>

{#if mounted}
    <Table columns={columns} rows={rows} />
}{/if}

<style>
    span {
        font-weight: bold;
    }
</style>